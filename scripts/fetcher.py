import os
import json
import feedparser
import urllib.parse as up
import urllib.request as ur
from datetime import datetime, timezone
from collections import defaultdict

class ArxivFetcher:
    def __init__(self, topics, output_dir="content/posts", cache_file="fetched_papers.json", max_results=None):
        self.topics = topics
        self.output_dir = output_dir
        self.cache_file = cache_file
        self.max_results = max_results
        self.fetched_ids = self.load_cache()
        os.makedirs(self.output_dir, exist_ok=True)

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

    def format_paper_entry(self, entry):
        arxiv_id = entry.id.split('/abs/')[-1]
        title = entry.title.strip()
        authors = ', '.join(author.name for author in entry.authors)
        summary = entry.summary.strip().replace('\n', ' ')
        pdf_link = next((link.href for link in entry.links if link.type == "application/pdf"), "")
        published = datetime.strptime(entry.published, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).strftime("%B %d, %Y at %I:%M %p UTC")

        return f"""<details>
<summary><strong>{title}</strong> by {authors}</summary>

- **Published**: {published}  
- **PDF**: [Download PDF]({pdf_link})  
- **arXiv ID**: {arxiv_id}  
- **Summary**: {summary}

</details>
"""

    def fetch_and_save(self):
        new_data = defaultdict(list)

        for topic in self.topics:
            print(f"\nFetching topic: {topic}")
            url = self.build_query_url(topic)
            feed = feedparser.parse(ur.urlopen(url).read())

            for entry in feed.entries:
                arxiv_id = entry.id.split('/abs/')[-1]
                if arxiv_id in self.fetched_ids:
                    continue

                self.fetched_ids.add(arxiv_id)
                new_data[topic].append(self.format_paper_entry(entry))

        self.save_cache()

        for topic, new_entries in new_data.items():
            slug = topic.lower().replace(" ", "-")
            filepath = os.path.join(self.output_dir, f"{slug}.md")
            frontmatter = ''

            if os.path.exists(filepath):
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                # Keep the existing frontmatter + title, insert new entries after it
                parts = content.split("#", 1)
                if len(parts) > 1:
                    header = parts[0] + "#" + parts[1].split('\n', 1)[0] + "\n\n"
                    old_entries = content[len(header):]
                else:
                    header = frontmatter
                    old_entries = ""
            else:
                header = frontmatter
                old_entries = ""

            new_markdown = header + "\n".join(new_entries) + "\n\n" + old_entries

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_markdown)

            print(f"Updated: {filepath}")