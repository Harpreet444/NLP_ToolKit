from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class Translator:
    def __init__(self):
        self.model_name = "Helsinki-NLP/opus-mt-en-hi"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
    
    def translate(self, text):
        inputs = self.tokenizer(text, return_tensors="pt")
        outputs = self.model.generate(**inputs)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)