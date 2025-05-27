# train_model.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Sample dataset (safe and phishing)
data = {
    'text': [
        "Click here to verify your account now.",
        "You have won a $1000 gift card!",
        "Your order has been shipped.",
        "Meeting scheduled at 10 AM tomorrow.",
        "Urgent: Account access limited!",
        "Invoice attached. Please confirm receipt.",
        "Your password expires in 1 day, click to renew.",
        "Team lunch at 1 PM today."
    ],
    'label': [1, 1, 0, 0, 1, 0, 1, 0]  # 1 = Phishing, 0 = Safe
}

df = pd.DataFrame(data)

# Vectorize text
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

# Train model
model = MultinomialNB()
model.fit(X, y)

# Save model & vectorizer
with open("phishing_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model and vectorizer saved.")
