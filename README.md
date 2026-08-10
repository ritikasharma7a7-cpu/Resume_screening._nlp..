# 📄 Resume Screening System

An NLP and Machine Learning based web application that analyzes resume text and predicts the most relevant job category.

## 📌 Project Overview

The Resume Screening System automates the initial screening of resumes by extracting resume text, preprocessing the content, converting it into TF-IDF features, and predicting the job category using a trained Machine Learning model.

The application provides a simple Streamlit interface where users can upload a resume and view the predicted job category.

## ✨ Features

- Upload resumes in PDF or TXT format
- Extract and clean resume text
- Convert text into TF-IDF features
- Predict job category using Machine Learning
- Interactive Streamlit web interface

## 🛠️ Technologies Used

- Python
- NLP
- TF-IDF
- Scikit-learn
- PDFPlumber
- Streamlit

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
```

## 🎯 Job Categories

The model classifies resumes into 25 predefined job categories, including:

- Data Science
- Python Developer
- Java Developer
- Mechanical Engineer
- Civil Engineer
- Electrical Engineering
- Business Analyst
- HR
- DevOps Engineer
- Testing
- Web Designing
- Database
- Network Security Engineer
- SAP Developer
- And more

## 📁 Project Structure

```text
Resume_Screening
│
├── app.py
├── clf.pkl
├── tfidf.pkl
├── requirements.txt
├── .gitattributes
└── README.md
```

## ▶️ Run Locally

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 🌐 Live Demo

[🔗 Open Resume Screening App](https://resumescreeningnlp-w4u25vp2hsd8vg92u4kspr.streamlit.app/)

## 👩‍💻 Author

**Ritika Sharma**