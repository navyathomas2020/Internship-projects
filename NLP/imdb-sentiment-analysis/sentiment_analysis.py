import pandas as pd
import numpy as np
import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load dataset
data = pd.read_csv("IMDB Dataset.csv")

# Stopwords
stop_words = set(stopwords.words('english'))

# Text preprocessing function
def clean_text(text):

    # Convert to lowercase
    text = text.lower()

    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)

    # Remove special characters
    text = re.sub(r'[^a-zA-Z]', ' ', text)

    # Tokenization
    words = word_tokenize(text)

    # Remove stopwords
    words = [word for word in words if word not in stop_words]

    return ' '.join(words)

# Apply preprocessing
data['clean_review'] = data['review'].apply(clean_text)

# Convert sentiment labels
data['sentiment'] = data['sentiment'].map({
    'positive': 1,
    'negative': 0
})

# TF-IDF Vectorization
tfidf = TfidfVectorizer(max_features=5000)

X = tfidf.fit_transform(data['clean_review']).toarray()

y = data['sentiment']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LogisticRegression()

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

# Classification Report
report = classification_report(y_test, y_pred)

print("Model Accuracy:\n")
print(accuracy)

print("\nConfusion Matrix:\n")
print(cm)

print("\nClassification Report:\n")
print(report)