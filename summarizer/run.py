import os
import logging
import argparse
from datetime import datetime
from summarizer import PDFSummarizer

def slugify(text):
  """Simple slugify for filenames/URLs."""
  return (
    text.lower()
    .replace(" ", "-")
    .replace("_", "-")
    .replace(".pdf", "")
    .replace("/", "-")
  )

def create_post_content(title, summary, date):
  """Generate Hugo markdown content with front matter."""
  front_matter = (
    "---\n"
    f"title: \"{title}\"\n"
    f"date: {date.isoformat()}\n"
    "draft: false\n"
    "tags: [summary, paper]\n"
    "---\n\n"
  )
  return front_matter + summary + "\n"

def summarize_pdf_file(pdf_path, api_key, system_prompt, output_dir):
  """Summarize a single PDF and save markdown post."""
  summarizer = PDFSummarizer(
    pdf_path=pdf_path,
    api_key=api_key,
    system_prompt=system_prompt
  )
  logging.info(f"Summarizing PDF: {pdf_path}")
  summary = summarizer.run()

  pdf_basename = os.path.basename(pdf_path)
  title = pdf_basename.replace(".pdf", "").replace("_", " ").replace("-", " ").title()
  date = datetime.utcnow()

  md_content = create_post_content(title, summary, date)

  os.makedirs(output_dir, exist_ok=True)
  filename = f"{date.strftime('%Y-%m-%d')}-{slugify(pdf_basename)}.md"
  output_path = os.path.join(output_dir, filename)

  with open(output_path, "w", encoding="utf-8") as f:
    f.write(md_content)

  logging.info(f"Hugo markdown post created at: {output_path}")

def main():
  parser = argparse.ArgumentParser(description="Summarize PDFs in a folder and create Hugo posts.")
  parser.add_argument("pdf_dir", help="Directory containing PDF files")
  parser.add_argument("--api_key", required=True, help="OpenAI API key")
  parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
  parser.add_argument("--output_dir", default="content/posts", help="Directory to save markdown posts")

  args = parser.parse_args()

  logging.basicConfig(
    level=logging.INFO if args.verbose else logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
  )

  SYSTEM_PROMPT = "You're an assistant summarizing scientific documents."

  pdf_files = [f for f in os.listdir(args.pdf_dir) if f.lower().endswith(".pdf")]

  if not pdf_files:
    logging.warning(f"No PDF files found in {args.pdf_dir}")
    return

  for pdf_file in pdf_files:
    pdf_path = os.path.join(args.pdf_dir, pdf_file)
    summarize_pdf_file(pdf_path, args.api_key, SYSTEM_PROMPT, args.output_dir)

if __name__ == "__main__":
  main()