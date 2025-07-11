import joblib
from sentence_transformers import SentenceTransformer

# Load encoder and classifier
encoder = SentenceTransformer("intfloat/multilingual-e5-large")
clf = joblib.load("pt_model.joblib")

# Predict
text = "Seu texto de exemplo aqui"
embedding = encoder.encode([text])
prediction = clf.predict(embedding)

print(prediction[0])  # Output: 'yes', 'no', or 'unclear'