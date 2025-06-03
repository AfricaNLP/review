from fetcher import ArxivFetcher

topics = ["machine translation", "sentiment analysis", "hate speech", "named entity recognition"]
fetcher = ArxivFetcher(topics=topics, output_dir="content")
fetcher.fetch_and_save()