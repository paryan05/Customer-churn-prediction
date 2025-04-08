# 📊 Customer Churn Prediction

A machine learning-based system to predict customer churn in the telecom sector using logistic regression. The project includes data preprocessing, model training, evaluation, and deployment using a **Streamlit** web application with both manual and CSV input support.

---

## 👥 Team Members

- **Aryan Prajapati** (Enrolment No: 12202130501005)  
- **Diya Desai** (Enrolment No: 12202130501015)

> Project submitted in partial fulfillment of the requirements for the degree of B.Tech in Computer Engineering  
> **G H Patel College of Engineering & Technology** (CVM University)  
> **Academic Year:** 2024–25 (Even Term)  
> **Course:** Artificial Intelligence and Machine Learning (202046702)  
> **Guide:** Prof. Tejas Patel

---

## 🚀 Project Overview

Customer churn — the process of losing customers — is a major concern for telecom companies. This project applies machine learning to proactively identify customers likely to discontinue service.

Using the **Telco Customer Churn dataset**, a **logistic regression** model was trained and evaluated, then deployed via a **Streamlit** application that offers:

- Interactive churn prediction via form inputs  
- Batch prediction with CSV file uploads  
- Probability-based output and downloadable results

---

## 🧠 Features

- ✅ Logistic Regression classifier with ~80% accuracy  
- 📈 Evaluated using precision, recall, and ROC-AUC  
- 🔍 Cleaned and preprocessed dataset (null handling, one-hot encoding, normalization)  
- 🖥️ Streamlit UI for real-time predictions  
- 📁 Supports CSV upload for batch processing  
- 📤 Downloadable output for predictions  

---

## 🗂️ Project Structure

```
├── app.py                    # Streamlit web app
├── best_model.pkl           # Trained model file
├── data_preprocessing.ipynb # Preprocessing steps
├── model_training.ipynb     # Training and saving the model
├── model_evaluation.ipynb   # Evaluation metrics and visualizations
└── README.md                # Project documentation
```

---

## ⚙️ System Requirements

### 💻 Hardware

- Processor: Intel i5 or higher  
- RAM: 8 GB minimum  
- Disk Space: ~500 MB  

### 🧪 Software

- Python 3.8+  
- Jupyter Notebook  
- Streamlit  
- Web browser (for interface)

### 📦 Python Libraries

Install dependencies with:

```bash
pip install pandas numpy scikit-learn joblib streamlit
```

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App

```bash
streamlit run app.py
```

### 4. Use the Web Interface

- Fill out the form for **individual predictions**  
- Upload a **CSV file** for batch predictions  
- **Download the result** as a CSV file  

---

## 📈 Model Performance

| Metric     | Score     |
|------------|-----------|
| Accuracy   | ~80%      |
| Precision  | High      |
| Recall     | Balanced  |
| ROC-AUC    | Reliable  |

- The model was trained on **70%** of the dataset and tested on the remaining **30%**  
- Special care was taken to **reduce false negatives** (customers predicted to stay but actually churn)

---

## ✅ Results

- ✅ Successfully developed a **logistic regression** model  
- ✅ Built a **functional and user-friendly** Streamlit interface  
- ✅ Enabled **CSV uploads and downloads** for batch operations  
- ✅ Achieved **reliable performance** suitable for business applications  

---

## 📌 Future Enhancements

- 🔁 Integrate **advanced models** like Random Forest, XGBoost, or Neural Networks  
- 📊 Enhance the **UI with dashboards** and richer customer insights  
- 🌐 Enable **real-time API deployment**  
- 📁 Add support for **multiple datasets** and domains  

---

## 📜 License

This project is for academic and educational purposes only.  
All rights reserved to the authors and G H Patel College of Engineering & Technology.
