import streamlit as st
import pickle
import re
import pdfplumber

# page title
st.set_page_config(
    page_title="Resume Screening App",
    page_icon="📄",
    layout="wide"
)


# -------------------- LOAD MODEL --------------------

@st.cache_resource
def load_models():
    clf = pickle.load(open("clf.pkl", "rb"))
    tfidfd = pickle.load(open("tfidf.pkl", "rb"))
    return clf, tfidfd


clf, tfidfd = load_models()

# CLEAN RESUME -


def cleanResume(txt):

    txt = re.sub(r"http\S+\s*", " ", txt)
    txt = re.sub(r"RT|cc", " ", txt)
    txt = re.sub(r"#\S+", " ", txt)
    txt = re.sub(r"@\S+", " ", txt)
    txt = re.sub(r"[^\x00-\x7F]", " ", txt)
    txt = re.sub(r"\s+", " ", txt)

    return txt.strip()

# -------------------- READ RESUME --------------------


def read_resume(uploaded_file):

    file_bytes = uploaded_file.read()

    if uploaded_file.name.lower().endswith(".pdf"):

        resume_text = ""

        with pdfplumber.open(uploaded_file) as pdf:

            for page in pdf.pages:

                text = page.extract_text()

                if text:
                    resume_text += text + "\n"

        return resume_text

    else:

        try:
            return file_bytes.decode("utf-8")
        except UnicodeDecodeError:
            return file_bytes.decode("latin-1")


# -------------------- CATEGORY MAPPING --------------------

category_mapping = {
    15: "Java Developer",
    23: "Testing",
    8: "DevOps Engineer",
    20: "Python Developer",
    24: "Web Designing",
    12: "HR",
    13: "Hadoop",
    3: "Blockchain",
    10: "ETL Developer",
    18: "Operations Manager",
    6: "Data Science",
    22: "Sales",
    16: "Mechanical Engineer",
    1: "Arts",
    7: "Database",
    11: "Electrical Engineering",
    14: "Health and Fitness",
    19: "PMO",
    4: "Business Analyst",
    9: "DotNet Developer",
    2: "Automation Testing",
    17: "Network Security Engineer",
    21: "SAP Developer",
    5: "Civil Engineer",
    0: "Advocate"
}


# -------------------- MAIN APP --------------------

def main():

    # Header
    st.title("📄 Resume Screening App")

    st.write(
        "An NLP and Machine Learning based system "
        "for automatic resume job-category classification."
    )

    st.divider()

    # -------------------- TWO COLUMN LAYOUT --------------------

    left, right = st.columns([1, 1.4], gap="large")

    # ==================== LEFT SIDE ====================

    with left:

        st.subheader("🔍 About the System")

        st.write(
            "This application analyzes resume text and predicts "
            "the most relevant job category using NLP, TF-IDF "
            "feature extraction and a trained Machine Learning model."
        )

        st.divider()

        st.subheader("⚙️ How It Works")

        st.write("📄 **1. Upload Resume**")
        st.caption(
            "Upload a resume in PDF or TXT format."
        )

        st.write("🧹 **2. Text Processing**")
        st.caption(
            "Resume text is cleaned and converted into TF-IDF features."
        )

        st.write("🤖 **3. ML Prediction**")
        st.caption(
            "The trained classifier predicts the relevant job category."
        )

        st.divider()

        st.subheader("🛠️ Technologies")

        st.write("• Python")
        st.write("• NLP")
        st.write("• TF-IDF")
        st.write("• Machine Learning")
        st.write("• Streamlit")

    # ==================== RIGHT SIDE ====================

    with right:

        st.subheader("📤 Upload Resume")

        uploaded_file = st.file_uploader(
            "Choose a PDF or TXT file",
            type=["pdf", "txt"]
        )

        if uploaded_file is None:

            st.info(
                "👆 Upload a resume to start screening."
            )

        else:

            st.success(
                "Resume uploaded successfully!"
            )

            try:

                resume_text = read_resume(uploaded_file)

            except Exception:

                st.error(
                    "Unable to read the uploaded resume."
                )

                return

            if not resume_text.strip():

                st.error(
                    "No readable text found in this resume."
                )

                return

            # Clean text
            cleaned_resume = cleanResume(resume_text)

            # TF-IDF
            input_features = tfidfd.transform(
                [cleaned_resume]
            ).toarray()

            # Prediction
            prediction_id = clf.predict(
                input_features
            )[0]

            # Category
            category_name = category_mapping.get(
                int(prediction_id),
                "Unknown"
            )

            st.divider()

            # Result
            st.subheader("🎯 Screening Result")

            st.metric(
                "Predicted Job Category",
                category_name
            )

            st.success(
                f"Predicted Job Category: {category_name}"
            )

            st.divider()

            # Resume information
            st.subheader("📊 Resume Information")

            col1, col2 = st.columns(2)

            with col1:

                st.write("**File Name**")
                st.write(uploaded_file.name)

            with col2:

                st.write("**Text Extracted**")
                st.write(f"{len(resume_text)} characters")

    # -last
    st.divider()

    st.caption(
        "Resume Screening System | NLP + TF-IDF + Machine Learning + Streamlit"
    )

# -- RUN --


if __name__ == "__main__":
    main()
