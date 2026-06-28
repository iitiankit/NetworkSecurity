🛡️ Network Security - Phishing Website Detection System

A production-ready Machine Learning project that detects phishing websites using URL and website-related security features. The project follows an end-to-end MLOps architecture with modular ETL pipelines, model training, experiment tracking, cloud storage, and FastAPI deployment.

📌 Overview

Phishing attacks remain one of the most common cybersecurity threats. This project predicts whether a website is Legitimate or Phishing using 30+ handcrafted security features extracted from URLs and website metadata.

The project is built following software engineering best practices with separate components for data ingestion, validation, transformation, model training, prediction, logging, exception handling, and cloud integration.

✨ Features
End-to-End Machine Learning Pipeline
Modular ETL Architecture
Data Validation using predefined schema
Data Transformation Pipeline
Automated Model Training
Hyperparameter Tuning
Experiment Tracking
MongoDB Atlas Integration
AWS S3 Artifact Storage
FastAPI REST API
Interactive Swagger Documentation
Logging & Custom Exception Handling
Production-ready Project Structure
🏗️ Project Architecture
                MongoDB Atlas
                      │
                      ▼
             Data Ingestion Pipeline
                      │
                      ▼
             Data Validation Pipeline
                      │
                      ▼
          Data Transformation Pipeline
                      │
                      ▼
             Model Training Pipeline
                      │
                      ▼
          Trained Model & Artifacts
                      │
              Upload to AWS S3
                      │
                      ▼
              FastAPI Prediction API
                      │
                      ▼
                   End User
📂 Project Structure
NetworkSecurity/
│
├── networksecurity/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── training_pipeline.py
│   │   ├── prediction_pipeline.py
│   │
│   ├── cloud/
│   ├── entity/
│   ├── exception/
│   ├── logger/
│   ├── utils/
│   └── configuration/
│
├── templates/
├── static/
├── app.py
├── main.py
├── requirements.txt
└── README.md
📊 Dataset

The dataset consists of 31 features describing various URL and website characteristics.

Example Features:

Feature	Description
having_IP_Address	Whether URL contains IP address
URL_Length	Length of URL
Shortining_Service	Presence of URL shortening service
having_At_Symbol	Contains '@' symbol
Prefix_Suffix	Presence of '-' in domain
SSLfinal_State	SSL certificate validity
Domain_registeration_length	Domain registration duration
HTTPS_token	HTTPS token usage
URL_of_Anchor	Anchor tag analysis
Links_in_tags	Links inside HTML tags
web_traffic	Website popularity
Google_Index	Indexed by Google
Page_Rank	Website Page Rank
Statistical_report	Blacklist status
Result	Target variable
Target Variable
Value	Meaning
-1	Phishing Website
1	Legitimate Website
⚙️ ETL Pipeline
1️⃣ Data Ingestion
Reads data from MongoDB Atlas
Exports data into Feature Store
Splits dataset into Train/Test
Stores ingestion artifacts
2️⃣ Data Validation
Schema validation
Missing value checks
Data drift detection
Dataset integrity verification
3️⃣ Data Transformation
Feature preprocessing
Pipeline creation
Train/Test transformation
Serialization using Pickle
4️⃣ Model Training
Trains multiple Machine Learning models
Hyperparameter tuning
Model evaluation
Best model selection
Artifact generation
🤖 Machine Learning Workflow
Raw Data
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
🌐 FastAPI Endpoints
Endpoint	Description
/	Home Page
/train	Trigger Model Training Pipeline
/predict	Predict Website Category
/docs	Swagger UI Documentation
☁️ Cloud Integration
MongoDB Atlas
Stores raw phishing dataset
Used as the primary data source
AWS S3

Stores:

Trained Models
Preprocessing Objects
Pipeline Artifacts
Feature Store
Logs
🛠️ Tech Stack
Programming Language
Python
Backend
FastAPI
Uvicorn
Machine Learning
Scikit-Learn
XGBoost
CatBoost
Database
MongoDB Atlas
Cloud
AWS S3
Data Processing
Pandas
NumPy
Experimentation
MLflow
Version Control
Git
GitHub
🚀 Installation

Clone the repository

git clone https://github.com/yourusername/NetworkSecurity.git

cd NetworkSecurity

Create virtual environment

python -m venv venv

Activate environment

Windows

venv\Scripts\activate

Linux

source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Run FastAPI

uvicorn app:app --reload

Visit

http://127.0.0.1:8000/docs
📈 Prediction Pipeline
User submits website features
FastAPI receives request
Preprocessor transforms input
Trained model performs inference
Prediction returned to user
📌 Future Improvements
Docker Containerization
CI/CD with GitHub Actions
Kubernetes Deployment
Real-time Monitoring
Prometheus & Grafana
Automated Model Retraining
User Authentication
HTTPS & Reverse Proxy with Nginx

👨‍💻 Author

Ankit Kumar

B.Tech, Chemical Engineering
IIT (ISM) Dhanbad