import fitz
import openai
import logging
import tiktoken

class PDFSummarizer:
  def __init__(self, pdf_path, api_key, system_prompt, model="gpt-4o", max_tokens=5000):
    self.pdf_path = pdf_path
    self.api_key = api_key
    self.model = model
    self.max_tokens = max_tokens
    self.system_prompt = system_prompt

    openai.api_key = self.api_key
    self.client = openai.OpenAI(api_key=self.api_key)
    self.tokenizer = tiktoken.encoding_for_model("gpt-4")

  def extract_text(self):
    """Extract text from the PDF using PyMuPDF."""
    logging.info(f"Extracting text from: {self.pdf_path}")
    doc = fitz.open(self.pdf_path)
    return "".join([page.get_text() for page in doc])

  def split_text(self, text):
    """Split text into token-based chunks."""
    logging.info("Splitting text into chunks...")
    words = text.split()
    chunks = []
    current_chunk = []
    current_tokens = 0

    for word in words:
      token_count = len(self.tokenizer.encode(word))
      if current_tokens + token_count > self.max_tokens:
        chunks.append(" ".join(current_chunk))
        current_chunk = [word]
        current_tokens = token_count
      else:
        current_chunk.append(word)
        current_tokens += token_count

    if current_chunk:
      chunks.append(" ".join(current_chunk))

    logging.info(f"Created {len(chunks)} chunks.")
    return chunks

  def send_prompt(self, system_prompt, user_prompt):
    """Send a prompt to the OpenAI API and return the response."""
    response = self.client.chat.completions.create(
      model=self.model,
      messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
      ],
      temperature=0.3
    )
    return response.choices[0].message.content.strip()

  def summarize_chunk(self, chunk, index, total):
    """Summarize a single chunk into one sentence."""
    logging.info(f"Summarizing chunk {index + 1}/{total}...")
    prompt = (
      "Summarize the following scientific text in one clear and informative sentence:\n\n"
      f"{chunk}\n\nOne-sentence summary:"
    )
    return self.send_prompt(self.system_prompt, prompt)

  def summarize_all_chunks(self, chunks):
    """Generate one-sentence summary for each chunk."""
    summaries = []
    for i, chunk in enumerate(chunks):
      summary = self.summarize_chunk(chunk, i, len(chunks))
      summaries.append(summary)
    return summaries

  def summarize_concisely(self, paragraph):
    """Summarize the paragraph of chunk summaries into a concise final summary."""
    logging.info("Generating final concise summary...")
    prompt = (
      "Here is a paragraph made of one-sentence summaries of chunks of a scientific paper. "
      "Write a concise paragraph that captures the core ideas clearly:\n\n"
      f"{paragraph}\n\nConcise summary:"
    )
    return self.send_prompt(self.system_prompt, prompt)

  def run(self):
    """Execute the full summarization pipeline."""
    full_text = self.extract_text()
    chunks = self.split_text(full_text)
    summaries = self.summarize_all_chunks(chunks)
    combined = " ".join(summaries)
    final = self.summarize_concisely(combined)
    logging.info("Summarization completed.")
    return final