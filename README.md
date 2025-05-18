# NLP Suite - Offline Natural Language Processing Toolkit

![Demo Screenshot](./assets/screenshot.jpg)

A multilingual NLP pipeline with offline capabilities for text processing tasks.

## Features
- **Text Summarization** - Generate concise English summaries
- **Translation** - English to Hindi translation
- **Entity Recognition** - Identify named entities
- **Sentiment Analysis** - Detect sentiment with confidence scores
- **Offline First** - Local model execution
- **Modern UI** - Streamlit-powered interface

## Installation
```bash
# Clone repository
git clone https://github.com/yourusername/nlp-suite.git
cd nlp-suite

# Install dependencies
pip install -r requirements.txt

# Download models
python setup_models.py

# Link spaCy model
python -m spacy link ./models/en_core_web_md en_core_web_md  
