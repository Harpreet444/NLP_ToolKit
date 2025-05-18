from transformers import pipeline

class TextSummarizer:
    def __init__(self):
        self.model = pipeline(
            "summarization",
            model="facebook/bart-large-cnn",
            min_length=30,
            max_length=130
        )
    
    def summarize(self, text):
        return self.model(text)[0]['summary_text']