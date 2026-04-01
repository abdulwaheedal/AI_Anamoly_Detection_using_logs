import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import IsolationForest
import joblib
import os

print("Loading dataset...")

df = pd.read_csv("data/block_features.csv")

X_text = df["template_sequence"]

# TF-IDF
tfidf = TfidfVectorizer(
    max_features=1000,
    ngram_range=(1,2),
    min_df=2
)

X = tfidf.fit_transform(X_text)

print("Training Isolation Forest...")

model = IsolationForest(
    n_estimators=200,
    contamination='auto',
    random_state=42
)

model.fit(X)

# Create model folder
os.makedirs("models", exist_ok=True)

# Save model + vectorizer
joblib.dump(model, "models/isolation_forest.pkl")
joblib.dump(tfidf, "models/tfidf.pkl")

print("✅ Model saved successfully!")