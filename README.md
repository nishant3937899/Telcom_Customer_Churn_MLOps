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
Try it yourself:
- Enter customer details for real-time prediction  
- Upload a CSV file for batch prediction  

📥 A sample dataset is available directly in the app (“Demo Datasets” link below the upload section)
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
- Recall 1: 0.90
- Recall 0: 0.53  
- F1 Score: 0.88  

**Observation:**  
The model achieved high recall but became overly aggressive, struggling to correctly classify non-churn customers (Class 0 recall dropped to 0.53).

---

### 🔹 Attempt 2: SMOTE (Synthetic Oversampling)  
- Recall 1: 0.89
- Recall 0: 0.60 
- F1 Score: 0.88  

**Observation:**  
SMOTE slightly degraded overall balance (Class 0 recall: 0.60), showing that synthetic data does not always improve performance.

---

### 🔹 Attempt 3: Manual Class Weight Tuning `{0: 1.62, 1: 1}`  
- Recall 1: 0.83
- Recall 0: 0.74 
- F1 Score: 0.86  
- Precision: 0.89  

**Result:**  
Achieved a more balanced trade-off:
- Improved precision (fewer false positives)  
- Better Class 0 recall (0.74)  
- Maintained strong churn detection (83%)  

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
```
Telcom_Customer_Churn_MLOps/
├──artifacts/                   
├── config/
│   └── config.yaml
├── logs/
│   └── running_logs.log
├── research/
│   ├── 1_data_ingestion.ipynb
│   ├── 2_data_validation.ipynb
│   ├── 3_feature_engineering_&_tranformation.ipynb
│   ├── 4_model_trainer.ipynb
│   └── trial_evaluation.ipynb
├── src/
│   └── MLOps_project/
|       ├── __init__.py
│       ├── components/
|       |   ├── __init__.py
│       │   ├── data_ingestion.py
│       │   ├── data_validation.py
│       │   ├── featureEngineering_transformaiton.py
│       │   └── model_trainer.py
│       ├── config/
|       |   ├── __init__.py
│       │   └── configuration.py
│       ├── pipeline/
|       |   ├── __init__.py
│       │   ├── perdiction.py
│       │   ├── stage_01_data_ingestion.py
│       │   ├── stage_02_data_validation.py
│       │   ├── stage_03_feat_engine_transform.py
│       │   └── stage_04_model_training.py
│       └── utils/
|           ├── __init__.py 
│           └── common.py
├── templates/
│   ├── index.html
│   ├── result.html
│   └── resultcsv.html
├── vids/
|   ├── csv_rec.gif
|    └── rec.gif
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.Docker.md
├── README.md
├── app.py
├── compose.yaml
├── main.py
├── mlflow.db
├── params.yaml
├── requirements.txt
├── schema.yaml
├── setup.py
└── templates.py
```
---

## ⚡ How to Run the Project  

```bash
# 1. Clone the repository
gh repo clone nishant3937899/Telcom_Customer_Churn_MLOps
cd Telcom_Customer_Churn_MLOPs

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run training pipeline (data ingestion → transformation → model training)
python main.py

# 4. Start the web application
python app.py
```
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
