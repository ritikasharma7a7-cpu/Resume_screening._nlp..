# 📄 Resume Screening System

An NLP and Machine Learning based web application that analyzes resume text and predicts the most relevant job category.

## 📌 Project Overview

The Resume Screening System automates the initial resume screening process by extracting text from uploaded resumes, preprocessing the content, converting it into numerical features using TF-IDF, and predicting the job category using a trained Machine Learning model.

The application is built using Streamlit, providing a simple interface for uploading resumes and viewing prediction results.

## ✨ Features

- Upload resumes in PDF or TXT format
- Extract text from PDF and TXT files
- Clean and preprocess resume text
- Convert resume text into TF-IDF features
- Predict the most relevant job category
- Display screening results through an interactive Streamlit interface

## 🛠️ Technologies Used

- **Python** – Application development
- **NLP** – Resume text preprocessing
- **TF-IDF** – Feature extraction from resume text
- **Scikit-learn** – Machine Learning model
- **PDFPlumber** – PDF text extraction
- **NLTK** – Natural Language Processing
- **Streamlit** – Web application and user interface

## ⚙️ Workflow

```text
Resume Upload
      ↓
Text Extraction
      ↓
Text Cleaning & Preprocessing
      ↓
TF-IDF Feature Extraction
      ↓
Trained ML Model
      ↓
Job Category Prediction

🎯 Job Categories
The trained model classifies resumes into 25 job categories, including:

Data Science
Python Developer
Java Developer
Mechanical Engineer
Civil Engineer
Electrical Engineering
Business Analyst
HR
DevOps Engineer
Database
Testing
Web Designing
Network Security Engineer
SAP Developer
And more

📁 Project Structure
Resume_Screening
│
├── app.py
├── clf.pkl
├── tfidf.pkl
├── requirements.txt
├── .gitattributes
└── README.md

app.py – Streamlit application
clf.pkl – Trained Machine Learning model
tfidf.pkl – TF-IDF vectorizer
requirements.txt – Project dependencies
.gitattributes – Git LFS configuration
README.md – Project documentation

▶️ Run Locally
```bash
pip install -r requirements.txt

streamlit run app.py

🌐 Live Demo
https://resumescreeningnlp-w4u25vp2hsd8vg92u4kspr.streamlit.app/