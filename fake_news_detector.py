import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample training data
news = [
    "Breaking news government announces new policy",
    "Scientists discover new planet",
    "You won lottery click here now",
    "Secret trick makes you rich",
    "Elections were held peacefully",
    "Market growth slows this quarter"
]

labels = [0, 0, 1, 1, 0, 0]  # 0 = Real, 1 = Fake

vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(news)

model = MultinomialNB()
model.fit(X, labels)

pickle.dump((vectorizer, model), open("fake_news_model.pkl", "wb"))

def predict(text):
    v, m = pickle.load(open("fake_news_model.pkl", "rb"))
    vec = v.transform([text])
    prob = m.predict_proba(vec)[0]
    label = "FAKE 🚨" if prob[1] > prob[0] else "REAL ✅"
    return label, max(prob)

if __name__ == "__main__":
    print("🧠 Fake News Detector — Day 76\n")
    msg = input("Enter news article: ")
    label, conf = predict(msg)
    print(f"\nResult: {label}")
    print(f"Confidence: {conf*100:.2f}%")
