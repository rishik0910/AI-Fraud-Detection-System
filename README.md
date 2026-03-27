# AI-Powered Phishing and Fraud Detection System

## Project Overview
This project presents a machine learning-based system for detecting phishing and fraudulent messages. It uses natural language processing techniques to analyze text input and classify it as either safe or fraudulent.

The system also includes a web-based interface for real-time interaction and prediction.

---

## Features
- Text-based fraud detection
- URL safety analysis
- Machine learning-based classification
- Confidence-based predictions
- Explainable results (keyword-based)
- History storage using database
- Interactive user interface using Streamlit

---

## Technologies Used
- Python
- Scikit-learn
- Pandas
- NumPy
- Streamlit
- SQLite

---

## Machine Learning Approach
- Text vectorization using TF-IDF
- Classification using Logistic Regression
- Model evaluation using accuracy and confusion matrix


fraud_detection_project/
│── app.py
│── model.py
│── utils.py
│── url_checker.py
│── explain.py
│── database.py
│── dataset.csv
│── model.pkl
│── vectorizer.pkl
│── AI_Fraud_Detection_Analysis.ipynb


---

## How to Run the Project

### Step 1: Navigate to project folder
cd fraud_detection_project

### Step 2: Train the model
python model.py

### Step 3: Run the application
python -m streamlit run app.py

---

## Example Usage
- Input: "Click here to verify your bank account"  
  Output: Fraud

- Input: "Hello, how are you?"  
  Output: Safe

---

## Conclusion
This project demonstrates how machine learning and natural language processing can be applied to detect phishing and fraudulent content in real-time systems.

Future improvements can include:
- Using larger datasets
- Applying advanced models like Random Forest or Deep Learning
- Deploying as a cloud-based application

---

## Author
Rishik 
---

## Project Structure
