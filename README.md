# 🚗 Car Price Prediction API

A Machine Learning-powered REST API built using **FastAPI** and deployed on **AWS EC2 (Ubuntu 24.04 LTS)**.

This project predicts the estimated price of a used car based on various vehicle attributes using a trained Scikit-learn Machine Learning model. The model is exposed through a FastAPI REST API and hosted on AWS EC2 for public access.

---

# 📖 Project Overview

The goal of this project is to demonstrate the complete Machine Learning deployment lifecycle, including:

- Machine Learning model integration
- REST API development using FastAPI
- AWS EC2 cloud deployment
- Linux server configuration
- Public API hosting
- API documentation using Swagger UI

This project serves as a portfolio project showcasing practical Machine Learning deployment skills.

---

# ✨ Features

- 🚀 Machine Learning-based car price prediction
- ⚡ FastAPI REST API
- 📖 Interactive Swagger UI
- ☁️ AWS EC2 Deployment
- 🔄 JSON Request & Response
- 📦 Scikit-learn Model Integration
- 🌐 Publicly Accessible API
- 🐧 Ubuntu Linux Server Deployment

---

# 🛠 Tech Stack

## Programming Language

- Python

## Machine Learning

- Scikit-learn
- Pandas
- NumPy
- Joblib

## Backend

- FastAPI
- Uvicorn

## Cloud

- AWS EC2
- Ubuntu 24.04 LTS

## Version Control

- Git
- GitHub

---

# 📂 Project Structure

```text
car-price-api/
│
├── app.py
├── requirements.txt
├── car_price_model.pkl
├── scaler.pkl
├── features.pkl
├── README.md
├── .gitignore
├── docs/
│   ├── aws-deployment.md
│   ├── project-architecture.md
│   └── troubleshooting.md
│
└── screenshots/
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/car-price-api.git

cd car-price-api
```

---

## Create Virtual Environment

```bash
python3 -m venv venv
```

---

## Activate Virtual Environment

Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

---

# 🌐 API Endpoints

## Home Endpoint

**GET /**

Returns

```json
{
    "message": "Car Price Prediction API is Ready!"
}
```

---

## Prediction Endpoint

**POST /predict**

Accepts vehicle information as input and returns the predicted car price.

---

# 📖 API Documentation

Swagger UI

```
http://13.60.188.130:8000/docs
```

API Home

```
http://13.60.188.130:8000/
```

> **Note:** This URL may change if the EC2 instance is stopped and restarted without an Elastic IP.

---

# ☁️ AWS EC2 Deployment

The application has been successfully deployed on an AWS EC2 Ubuntu 24.04 LTS instance.

Deployment process included:

- Launching an EC2 Ubuntu instance
- Connecting via SSH
- Uploading the project
- Creating a Python virtual environment
- Installing project dependencies
- Running FastAPI using Uvicorn
- Configuring AWS Security Group
- Opening TCP Port 8000
- Verifying public API access

Detailed deployment guide is available in:

```
docs/aws-deployment.md
```

---

# 🏗 System Architecture

```text
                User
                  │
                  ▼
         FastAPI REST API
                  │
                  ▼
      Machine Learning Model
                  │
                  ▼
       Scikit-learn Prediction
                  │
                  ▼
          JSON Response
```

---

# 📷 Project Screenshots

## API Home

![API Home](screenshots/api-home.png)

---

## Swagger UI

![Swagger UI](screenshots/swagger-ui.png)

---

## Prediction Result

![Prediction](screenshots/prediction.png)

---

## AWS EC2 Instance

![EC2 Instance](screenshots/ec2-instance.png)

---

## AWS Security Group

![Security Group](screenshots/security-group.png)

---

## FastAPI Running on EC2

![Terminal](screenshots/terminal.png)

---

# 🔧 Challenges Faced During Deployment

During deployment, several real-world issues were encountered and resolved:

- Resolved Scikit-learn version compatibility issues.
- Fixed `ModuleNotFoundError: No module named '_loss'` caused by mismatched library versions.
- Migrated deployment to Ubuntu 24.04 LTS for improved package compatibility.
- Configured FastAPI to run with Uvicorn instead of executing `app.py` directly.
- Configured AWS Security Group to allow inbound traffic on TCP Port 8000.
- Verified API accessibility using local and public endpoints.

These troubleshooting steps provided practical experience in deploying Machine Learning applications in a cloud environment.

---

# 🚀 Future Improvements

- Docker Containerization
- Nginx Reverse Proxy
- HTTPS using Let's Encrypt
- Elastic IP
- Custom Domain
- CI/CD using GitHub Actions
- Docker Compose
- AWS Load Balancer
- CloudWatch Monitoring

---

# 📚 Documentation

Additional documentation is available in the `docs` directory.

- AWS Deployment Guide
- Project Architecture
- Troubleshooting Guide

---

# 👨‍💻 Author

**Rathish Rajinikanth**

- GitHub: https://github.com/YOUR_GITHUB_USERNAME
- LinkedIn: https://www.linkedin.com/in/YOUR_LINKEDIN_PROFILE
- Portfolio: https://YOUR_PORTFOLIO_LINK

---

# ⭐ Support

If you found this project helpful, consider giving the repository a ⭐ on GitHub.

Thank you for visiting!
