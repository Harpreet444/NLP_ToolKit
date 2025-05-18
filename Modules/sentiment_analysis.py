from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )
    
    def analyze(self, text):
        return self.analyzer(text)[0]
    
c = SentimentAnalyzer()
text = "I love programming!"
o = c.analyze(text)
print(o)