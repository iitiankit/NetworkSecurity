# 🛡️ Network Security - Phishing Website Detection

An end-to-end Machine Learning project for detecting phishing websites using URL and website security features. The project follows a modular architecture with data ingestion, validation, transformation, model training, prediction pipeline, FastAPI deployment, and cloud database integration.

---

## 🚀 Live Demo

**Application**

http://52.91.170.57

**API Documentation (Swagger)**

http://52.91.170.57/docs

---

## 📌 Features

- End-to-End Machine Learning Pipeline
- Modular Project Architecture
- Data Ingestion from MongoDB Atlas
- Data Validation
- Data Transformation
- Model Training & Evaluation
- Prediction Pipeline
- FastAPI REST API
- Interactive Swagger Documentation
- Logging & Custom Exception Handling
- Production Deployment on AWS EC2
- Nginx Reverse Proxy
- Systemd Service Management

---

#  Architecture

```text
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
                    Trained Model (.pkl)
                           │
                           ▼
                  FastAPI Prediction API
                           │
                 Nginx Reverse Proxy
                           │
                           ▼
                      AWS EC2 Server
                           │
                           ▼
                          User
```

---

# 📂 Project Structure

```text
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
│   │   └── prediction_pipeline.py
│   │
│   ├── entity/
│   ├── configuration/
│   ├── constants/
│   ├── exception/
│   ├── logger/
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

The dataset contains **30 website security features** used to classify websites as **Legitimate** or **Phishing**.

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
- Google_Index
- Page_Rank
- Statistical_report

### Target Variable

| Value | Meaning |
|------|---------|
| 1 | Legitimate Website |
| -1 | Phishing Website |

---

# ⚙️ Machine Learning Pipeline

## 📥 Data Ingestion

- Reads data from MongoDB Atlas
- Creates feature store
- Train-Test split

---

## ✅ Data Validation

- Schema Validation
- Missing Value Checks
- Dataset Integrity Validation

---

## 🔄 Data Transformation

- Data Preprocessing
- Feature Engineering
- Pipeline Serialization

---

## 🤖 Model Training

- Multiple ML Algorithms
- Hyperparameter Tuning
- Model Evaluation
- Best Model Selection

---

# 🌐 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Home Page |
| `/train` | Train Model |
| `/predict` | Predict Website Category |
| `/docs` | Swagger Documentation |

---

# ☁️ Deployment

The application is deployed on **AWS EC2** using a production-ready architecture.

### Deployment Stack

- AWS EC2
- Ubuntu Server
- FastAPI
- Uvicorn
- Nginx
- Systemd
- MongoDB Atlas

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

- AWS EC2

### Web Server

- Nginx

### Service Manager

- Systemd

### Data Processing

- Pandas
- NumPy

### Version Control

- Git
- GitHub

---

# 🚀 Installation

Clone Repository

```bash
git clone https://github.com/iitiankit/NetworkSecurity.git

cd NetworkSecurity
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Application

```bash
uvicorn app:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

# 🚀 AWS Deployment

The application has been deployed on an AWS EC2 instance.

Deployment Steps

- Launch EC2 Instance
- Install Python & Dependencies
- Clone GitHub Repository
- Create Virtual Environment
- Install Requirements
- Configure MongoDB Atlas
- Run FastAPI with Uvicorn
- Configure Systemd Service
- Configure Nginx Reverse Proxy
- Deploy Application

---

# 📈 Prediction Flow

```text
User
 │
 ▼
FastAPI API
 │
 ▼
Preprocessor
 │
 ▼
Trained Model
 │
 ▼
Prediction
```

---

# 📌 Future Enhancements

- AWS S3 for Model Artifacts
- MLflow Model Registry
- Docker Containerization
- GitHub Actions CI/CD
- HTTPS using Let's Encrypt
- Custom Domain
- Prometheus & Grafana Monitoring

---

# 👨‍💻 Author

**Ankit Kumar**

B.Tech
Indian Institute of Technology (ISM), Dhanbad

GitHub: https://github.com/iitiankit


---

⭐ If you found this project useful, please consider giving it a **Star** on GitHub.
