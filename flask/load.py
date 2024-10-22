import tensorflow_hub as hub
import mlflow.pyfunc
import joblib

mlflow.set_tracking_uri("http://mlflow:5000")

use_model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
model_uri = "models:/bert_logistic_reg/Production"
model = mlflow.sklearn.load_model(model_uri)
mlb = joblib.load('./flask/models/mlb_500T.pkl')
