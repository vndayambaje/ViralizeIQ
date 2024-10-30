# oad or build a sentiment model using Hugging Face’s transformers (e.g., BERT)
from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
class SentimentAnalyzer:
    def __init__(self):
        self.sentiment_pipeline = pipeline("sentiment-analysis")

    def analyze(self, text):
        return self.sentiment_pipeline(text)
