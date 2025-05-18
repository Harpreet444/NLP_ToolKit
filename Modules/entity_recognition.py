import spacy

class EntityRecognizer:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_md")
    
    def get_entities(self, text):
        doc = self.nlp(text)
        return [(ent.text, ent.label_) for ent in doc.ents]
    

# e = EntityRecognizer()
# text = "Apple is looking at buying U.K. startup for $1 billion"
# o=e.get_entities(text)
# print(o)
