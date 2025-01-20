import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from preprocess import clean_text

# CSV File Path (Relative or Absolute)
file_path = 'phishing_emails.csv'

# Check if CSV Exists
if os.path.exists(file_path):
    print("File found. Proceeding to read.")
    data = pd.read_csv(file_path)
    
    # Print column names for debugging
    print("Columns in the CSV file:", data.columns)
    
    # Handle Empty File
    if data.empty:
        print("CSV file is empty. Please add data.")
        exit()
else:
    print("CSV file not found. Check the path.")
    exit()

# Preprocess Email Data
data.dropna(inplace=True)

# Make sure the correct column name is used for email content
if 'Email Content' in data.columns:
    data['Email Content'] = data['Email Content'].apply(clean_text)
else:
    print("Error: 'Email Content' column not found in dataset.")
    exit()

# Feature Extraction
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(data['Email Content'])
y = data['Label']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Model
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate Model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Predict Email Function
def predict_email(email):
    email = clean_text(email)
    vectorized_email = vectorizer.transform([email])
    prediction = model.predict(vectorized_email)
    return prediction[0]



