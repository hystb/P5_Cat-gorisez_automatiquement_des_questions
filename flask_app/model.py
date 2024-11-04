import re
from load import use_model, mlb, model
import numpy as np


class Model_api:
    def __init__(self):
        self.embedding_text = None
        return

    def clean_dl(self, text):
        text = text.lower()
        text = re.sub(r'(?<!\bc)(\+|#)', '', text)
        text = re.sub(r'[^a-z\s\+#]', '', text)
        return text

    def transform(self, text):
        text = self.clean_dl(text)
        embedding_text = use_model([text])
        return embedding_text

    def predict(self, text):
        embeddings = self.transform(text)
        top_n = 10
        probabilities = model.predict_proba(embeddings.numpy())
        top_indices = np.argsort(probabilities[0])[::-1][:top_n]
        top_tags = mlb.classes_[top_indices]
        top_probs = probabilities[0][top_indices]
        tags = [{'tag': tag, 'probability': prob}
                for tag, prob in zip(top_tags, top_probs)]
        return tags


model_api = Model_api()
