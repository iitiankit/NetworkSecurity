# 🛡️ Network Security - Phishing Website Detection using Machine Learning

An end-to-end Machine Learning project that detects phishing websites using URL and website security features. This project follows a production-ready MLOps architecture with modular ETL pipelines, model training, cloud integration, and FastAPI deployment.

---

## 🚀 Features

- End-to-End Machine Learning Pipeline
- Modular ETL Architecture
- Data Ingestion from MongoDB Atlas
- Data Validation using Schema Validation
- Data Transformation Pipeline
- Model Training & Evaluation
- Hyperparameter Tuning
- MLflow Experiment Tracking
- AWS S3 Integration for Model Artifacts
- FastAPI REST API
- Interactive Swagger Documentation
- Logging & Custom Exception Handling
- Production-Ready Project Structure

---

# 📌 Project Workflow

```text
                 MongoDB Atlas
                      │
                      ▼
              Data Ingestion
                      │
                      ▼
              Data Validation
                      │
                      ▼
           Data Transformation
                      │
                      ▼
              Model Training
                      │
                      ▼
          Best Model Selection
                      │
                      ▼
            Upload Artifacts
                 to AWS S3
                      │
                      ▼
             FastAPI Prediction API
                      │
                      ▼
                  End User
```

---

# 📂 Project Structure

```text
NetworkSecurity/
│
├── networksecurity/
│   ├── cloud/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │
│   ├── configuration/
│   ├── constants/
│   ├── entity/
│   ├── exception/
│   ├── logger/
│   ├── pipeline/
│   │   ├── training_pipeline.py
│   │   └── prediction_pipeline.py
│   │
│   └── utils/
│
├── templates/
├── static/
├── app.py
├── main.py
├── requirements.txt
├── setup.py
└── README.md
```

---

# 📊 Dataset

The dataset contains 30 URL and website security-related features used to classify websites as **Legitimate** or **Phishing**.

### Sample Features

- having_IP_Address
- URL_Length
- Shortining_Service
- Prefix_Suffix
- SSLfinal_State
- Domain_registeration_length
- HTTPS_token
- URL_of_Anchor
- Links_in_tags
- web_traffic
- Page_Rank
- Google_Index
- Statistical_report

### Target Variable

| Value | Class |
|------|-------|
| 1 | Legitimate Website |
| -1 | Phishing Website |

---

# ⚙️ ETL Pipeline

## 📥 Data Ingestion

- Reads data from MongoDB Atlas
- Exports dataset to Feature Store
- Splits dataset into Train/Test
- Stores ingestion artifacts

---

## ✅ Data Validation

- Schema Validation
- Missing Value Validation
- Data Drift Detection
- Dataset Integrity Checks

---

## 🔄 Data Transformation

- Feature Engineering
- Data Preprocessing
- Transformation Pipeline Creation
- Serialization of Preprocessor

---

## 🤖 Model Training

- Trains Multiple Machine Learning Models
- Hyperparameter Tuning
- Model Evaluation
- Best Model Selection
- Saves Model Artifacts

---

# 🌐 FastAPI Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Home Page |
| `/train` | Train Machine Learning Model |
| `/predict` | Predict Website Type |
| `/docs` | Swagger API Documentation |

---

# ☁️ Cloud Integration

## MongoDB Atlas

- Stores Raw Dataset
- Used as Data Source for ETL Pipeline

## AWS S3

Stores

- Trained Models
- Feature Store
- Preprocessor
- Pipeline Artifacts
- Logs

---

# 🛠️ Tech Stack

### Programming Language

- Python

### Backend

- FastAPI
- Uvicorn

### Machine Learning

- Scikit-Learn
- XGBoost
- CatBoost

### Database

- MongoDB Atlas

### Cloud

- AWS S3

### Experiment Tracking

- MLflow

### Data Processing

- Pandas
- NumPy

### Version Control

- Git
- GitHub

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/NetworkSecurity.git

cd NetworkSecurity
```

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
uvicorn app:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

# 📈 Machine Learning Pipeline

```text
Raw Dataset
     │
     ▼
Data Ingestion
     │
     ▼
Data Validation
     │
     ▼
Data Transformation
     │
     ▼
Model Training
     │
     ▼
Best Model Selection
     │
     ▼
Model Saved
     │
     ▼
Prediction API
```

---

# 📈 Prediction Flow

1. User submits website security features.
2. FastAPI receives the request.
3. Data is preprocessed using the saved transformation pipeline.
4. Trained model predicts whether the website is Legitimate or Phishing.
5. Prediction is returned through the API.

---

# 📌 Future Enhancements

- Docker Deployment
- GitHub Actions CI/CD
- Kubernetes Deployment
- Prometheus & Grafana Monitoring
- Automated Model Retraining
- Reverse Proxy with Nginx
- HTTPS Support

---

# 👨‍💻 Author

**Ankit Kumar**

B.Tech
Indian Institute of Technology (ISM), Dhanbad


---

⭐ If you found this project useful, consider giving it a **Star** on GitHub.
