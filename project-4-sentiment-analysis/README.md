 Product Review Sentiment Analysis

## Overview
An NLP and machine-learning project that classifies unstructured product reviews as **Positive** or **Negative**.

## Objectives
- Tokenize review text.
- Remove English stop words.
- Lemmatize words using NLTK.
- Convert text into numerical features using TF-IDF.
- Train a Multinomial Naive Bayes classifier.
- Predict the sentiment of new reviews.

## Files
| File | Description |
|---|---|
| `reviews.csv` | 50 fictional labeled product reviews |
| `sentiment_analysis.py` | Preprocessing, TF-IDF, model training, evaluation and prediction |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

## Dataset columns
- `review_id`: unique review number
- `review`: product review text
- `sentiment`: Positive or Negative

The sample data is fictional and intended for learning. It is small, so its evaluation score is not a measure of real-world model performance.

## Workflow
`Raw text → Cleaning → Tokenization → Stop-word removal → Lemmatization → TF-IDF → Naive Bayes → Prediction`

## Requirements
- Python 3.9+
- Internet connection on the first run to download NLTK language resources

## Run the project

1. Open a terminal in this folder.
2. Create a virtual environment (recommended):

   **Windows**
   ```bash
   python -m venv venv
   venv\\Scripts\\activate
   ```

3. Install libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. Run:
   ```bash
   python sentiment_analysis.py
   ```

5. Enter a review when prompted. Type `exit` to quit.

Classify one review directly:
```bash
python sentiment_analysis.py --review "The product is excellent and works perfectly"
```

Use a different CSV:
```bash
python sentiment_analysis.py --data another_reviews.csv
```
The CSV must contain `review` and `sentiment` columns.

## Model evaluation
The program displays accuracy, precision, recall, F1-score, and a confusion matrix on a held-out test set. TF-IDF is fitted only on the training data to avoid test-data leakage.

## Future improvements
- Use a larger real-world labeled review dataset.
- Compare Naive Bayes with a Linear SVM classifier.
- Add a Neutral sentiment class.
- Build a simple Streamlit or Flask interface.
- Save the trained model for reuse.

## Author
Add your name here.

## License
For educational purposes.
