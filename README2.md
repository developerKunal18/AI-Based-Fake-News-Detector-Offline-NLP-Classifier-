# 🧠 Fake News Detector

## 💡 Overview
The **Fake News Detector** is an offline Python application that uses **Machine Learning and Natural Language Processing (NLP)** to determine whether a news article is **REAL** or **FAKE**.

It mimics the behavior of modern fact-checking and misinformation detection systems used by media platforms and cybersecurity teams.

---

## 🚀 Features

### 📰 News Classification
- Classifies news as:
  - **REAL ✅**
  - **FAKE 🚨**

### 🧠 Machine Learning Model
- Uses **TF-IDF vectorization**
- Uses **Naive Bayes classifier**
- Trains and saves model locally

### 📊 Confidence Score
- Displays how confident the model is in its prediction

### 💾 Model Persistence
- Stores trained model in `fake_news_model.pkl`
- Reuses model for future predictions

### 🌐 Fully Offline
- No APIs
- No internet required
- No cloud services

---

## 🧠 Concepts & Technologies Used
- Python
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Naive Bayes Classifier
- Machine Learning Pipelines
- Pickle Model Storage
- Cybersecurity & Media Intelligence

---

## 📦 Installation

Install dependency:
```bash
pip install scikit-learn
