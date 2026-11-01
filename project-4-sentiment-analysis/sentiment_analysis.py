"""Product review sentiment analysis using NLTK, TF-IDF and Naive Bayes."""
import argparse
import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def setup_nltk():
    for item in ["punkt", "punkt_tab", "stopwords", "wordnet", "omw-1.4"]:
        nltk.download(item, quiet=True)

setup_nltk()
STOP_WORDS = set(stopwords.words("english"))
LEMMATIZER = WordNetLemmatizer()

def preprocess_text(text):
    """Lowercase, tokenize, remove punctuation/stop words, and lemmatize."""
    text = re.sub(r"[^a-z\\s]", " ", str(text).lower())
    tokens = word_tokenize(text)
    return [
        LEMMATIZER.lemmatize(token)
        for token in tokens
        if token not in STOP_WORDS and len(token) > 1
    ]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="reviews.csv")
    parser.add_argument("--review", help="Optional review to classify")
    args = parser.parse_args()

    data = pd.read_csv(args.data).dropna(subset=["review", "sentiment"])
    data["sentiment"] = data["sentiment"].str.strip().str.title()
    data = data[data["sentiment"].isin(["Positive", "Negative"])]
    if data["sentiment"].nunique() != 2:
        raise ValueError("Dataset must contain Positive and Negative labels.")

    X_train, X_test, y_train, y_test = train_test_split(
        data["review"], data["sentiment"], test_size=0.25,
        random_state=42, stratify=data["sentiment"]
    )

    vectorizer = TfidfVectorizer(
        tokenizer=preprocess_text, preprocessor=None,
        token_pattern=None, lowercase=False
    )
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    model = MultinomialNB()
    model.fit(X_train_tfidf, y_train)
    predictions = model.predict(X_test_tfidf)

    print(f"Dataset records: {len(data)}")
    print(f"Accuracy: {accuracy_score(y_test, predictions):.2%}")
    print("\\nClassification report:")
    print(classification_report(y_test, predictions, zero_division=0))
    print("Confusion matrix (Negative, Positive):")
    print(confusion_matrix(y_test, predictions, labels=["Negative", "Positive"]))

    if args.review:
        review = args.review
    else:
        print("\\nEnter a review to classify. Type 'exit' to stop.")
        while True:
            review = input("\\nReview: ").strip()
            if review.lower() == "exit":
                break
            if not review:
                print("Please enter review text.")
                continue
            show_prediction(review, vectorizer, model)

def show_prediction(review, vectorizer, model):
    features = vectorizer.transform([review])
    label = model.predict(features)[0]
    confidence = max(model.predict_proba(features)[0]) * 100
    print(f"Predicted sentiment: {label} (model confidence: {confidence:.1f}%)")

if __name__ == "__main__":
    main()
