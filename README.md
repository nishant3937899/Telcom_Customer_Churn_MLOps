# 🚀 Telcom_Customer_Churn_MLOPs

An end-to-end **MLOps project** for predicting telecom customer churn using machine learning, deployed on the cloud with real-time and batch inference capabilities.

---
## 🎥 Demo Videos  

- 📊 **Batch Prediction (CSV Upload):**  
 ![Batch Prediction Demo](https://raw.githubusercontent.com/nishant3937899/Telcom_Customer_Churn_MLOps/b74162860c7f0239d13e6192a230e1fe37fd5f7c/vids/csv_rec.gif)


- ⚡ **Single Prediction (Web App):**  
  ![Single Prediction Demo](https://raw.githubusercontent.com/nishant3937899/Telcom_Customer_Churn_MLOps/b74162860c7f0239d13e6192a230e1fe37fd5f7c/vids/rec.gif) 

---


## 🌐 Live Application  
👉 http://3.108.193.123:8080  

---

## 📌 Problem Statement  

Customer churn is a major challenge in the telecom industry. Businesses need to proactively identify customers who are likely to leave so they can take targeted retention actions.  

This project builds a machine learning system to **predict churn risk based on customer demographics, service usage, and billing patterns**.

---

## ⚙️ Key Features  

- 🔹 **End-to-End MLOps Pipeline**  
  Data Ingestion → Validation → Transformation → Model Training → Prediction → Deployment  

- 🔹 **Real-Time Inference**  
  Interactive web interface to predict churn for individual customers  

- 🔹 **Batch Prediction via CSV**  
  Upload datasets and get predictions at scale with visual summaries  

- 🔹 **Interactive Visualization**  
  Displays churn vs non-churn distribution for uploaded data  

- 🔹 **Cloud Deployment (AWS)**  
  Deployed and accessible via a public endpoint  

---

## 🧠 Model Details  

- **Algorithm:** Logistic Regression  
- **Library:** Scikit-learn  
- **Why this model?**  
  Logistic Regression provides strong performance on structured/tabular data while remaining interpretable and efficient for deployment.

---

## ⚔️ Challenges & Learnings  

### 🚧 Handling Imbalanced Data  

One of the biggest challenges in this project was dealing with class imbalance. Multiple strategies were tested:

---

### 🔹 Attempt 1: GridSearch + Balanced Class Weights  
- Recall: 0.90  
- F1 Score: 0.88  

**Observation:**  
The model achieved high recall but became overly aggressive, struggling to correctly classify non-churn customers (Class 0 recall dropped to 0.58).

---

### 🔹 Attempt 2: SMOTE (Synthetic Oversampling)  
- Recall: 0.89  
- F1 Score: 0.88  

**Observation:**  
SMOTE slightly degraded overall balance (Class 0 recall: 0.61), showing that synthetic data does not always improve performance.

---

### 🔹 Attempt 3: Manual Class Weight Tuning `{0: 1.62, 1: 1}`  
- Recall: 0.83  
- F1 Score: 0.86  
- Precision: 0.89  

**Result:**  
Achieved a more balanced trade-off:
- Improved precision (fewer false positives)  
- Better Class 0 recall (0.73)  
- Maintained strong churn detection (83%)  

👉 This approach provided the most practical balance for real-world deployment.

---

## 🛠️ Tech Stack  

- Python  
- Pandas, NumPy  
- Scikit-learn  
- MLflow  
- Flask  
- Plotly  
- Matplotlib, Seaborn  
- Joblib  
- PyYAML  
- docker
---

## 🏗️ Project Structure  



---

## ⚠️ Limitations & Future Improvements  

- Add prediction probability and confidence score  
- Include model explainability (e.g., SHAP values)  
- Improve UI/UX for better user experience  
- Add monitoring and logging for production readiness    

---

## 👤 Author  

**Nishant Chandra Verma**  

---
