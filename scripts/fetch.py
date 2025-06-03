from fetcher import ArxivFetcher

topics = ["machine translation", "sentiment analysis", "llm evaluation"]
fetcher = ArxivFetcher(topics=topics, output_dir="content")
fetcher.fetch_and_save()