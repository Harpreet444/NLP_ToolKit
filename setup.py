import os
import spacy
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import pipeline as hf_pipeline

MODEL_DIR = "Models"
os.makedirs(MODEL_DIR, exist_ok=True)

# Set environment variables for model storage
os.environ["TRANSFORMERS_CACHE"] = MODEL_DIR
os.environ["XDG_CACHE_HOME"] = MODEL_DIR

def download_models():
    # Text Summarization
    hf_pipeline("summarization", model="facebook/bart-large-cnn")

    # Translation (English to Hindi)
    AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-hi")
    AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-hi")

    # Sentiment Analysis
    hf_pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

    # SpaCy English model for NER
    spacy.cli.download("en_core_web_md", direct=False)
    
    print("All models downloaded successfully!")

if __name__ == "__main__":
    download_models()
    # Move spaCy model to model directory manually after download
    print("Note: Move spaCy model from site-packages to models directory if needed")