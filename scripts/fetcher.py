import os
import json
import feedparser
import urllib.parse as up
import urllib.request as ur
from datetime import datetime, timezone

class ArxivFetcher:
  def __init__(self, topics, output_dir="content", cache_file="fetched_papers.json", max_results=None):
    self.topics = topics
    self.output_dir = output_dir
    self.cache_file = cache_file
    self.max_results = max_results
    self.fetched_ids = self.load_cache()

  def load_cache(self):
    if os.path.exists(self.cache_file):
      with open(self.cache_file, 'r') as f:
        return set(json.load(f))
    return set()

  def save_cache(self):
    with open(self.cache_file, 'w') as f:
      json.dump(list(self.fetched_ids), f, indent=2)

  def build_query_url(self, search_term):
    base_url = "http://export.arxiv.org/api/query?"
    african_filter = "(Africa OR \"African languages\")"
    query = {
      "search_query": f"all:{search_term} AND {african_filter}",
      "start": 0,
      "sortBy": "submittedDate",
      "sortOrder": "descending"
    }
    if self.max_results:
      query["max_results"] = self.max_results
    
    return base_url + up.urlencode(query)

  def fetch_and_save(self):
    for topic in self.topics:
      print(f"\nFetching topic: {topic}")
      url = self.build_query_url(topic)
      feed = feedparser.parse(ur.urlopen(url).read())

      topic_dir = os.path.join(self.output_dir, topic.lower().replace(" ", "-"))
      os.makedirs(topic_dir, exist_ok=True)

      for entry in feed.entries:
        arxiv_id = entry.id.split('/abs/')[-1]
        if arxiv_id in self.fetched_ids:
          continue

        self.fetched_ids.add(arxiv_id)

        title = entry.title.strip()
        authors = ', '.join(author.name for author in entry.authors)
        summary = entry.summary.strip().replace('\n', ' ')
        pdf_link = next((link.href for link in entry.links if link.type == "application/pdf"), "")
        
        published = datetime.strptime(
          entry.published, "%Y-%m-%dT%H:%M:%SZ"
        ).replace(
          tzinfo=timezone.utc
        ).strftime("%B %d, %Y at %I:%M %p UTC")

        filename = f"{topic_dir}/{arxiv_id.replace('/', '-')}.md"
        with open(filename, "w", encoding="utf-8") as f:
          f.write(f"---\n")
          f.write(f"title: \"{title}\"\n")
          f.write(f"date: {published}\n")
          f.write(f"authors: \"{authors}\"\n")
          f.write(f"arxiv_id: \"{arxiv_id}\"\n")
          f.write(f"pdf: \"{pdf_link}\"\n")
          f.write(f"topic: \"{topic}\"\n")
          f.write(f"---\n\n")
          f.write(f"{summary}\n")

        print(f"Saved: {filename}")

    self.save_cache()