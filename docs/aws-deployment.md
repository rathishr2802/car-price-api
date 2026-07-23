# 🚀 AWS EC2 Deployment Guide

## Overview

This document explains how the Car Price Prediction API was deployed on an AWS EC2 Ubuntu server using FastAPI and Uvicorn.

---

# Deployment Environment

| Service | Details |
|----------|---------|
| Cloud Provider | Amazon Web Services (AWS) |
| Compute Service | EC2 |
| Operating System | Ubuntu Server 24.04 LTS |
| Backend Framework | FastAPI |
| ASGI Server | Uvicorn |
| Programming Language | Python |
| Machine Learning Library | Scikit-learn |

---

# Step 1: Launch EC2 Instance

- Log in to the AWS Console.
- Navigate to **EC2**.
- Click **Launch Instance**.
- Choose **Ubuntu Server 24.04 LTS**.
- Select an appropriate instance type (for example, `t2.micro`).
- Create or select an existing key pair.
- Launch the instance.

---

# Step 2: Connect to the Instance

Connect to the EC2 instance using SSH.

Example:

```bash
ssh -i your-key.pem ubuntu@YOUR_PUBLIC_IP
```

---

# Step 3: Upload the Project

Upload the project files to the EC2 instance.

The project includes:

- app.py
- requirements.txt
- car_price_model.pkl
- scaler.pkl
- features.pkl

---

# Step 4: Create a Virtual Environment

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

# Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Step 6: Start the FastAPI Server

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

Expected output:

```text
INFO: Started server process
INFO: Waiting for application startup.
INFO: Application startup complete.
INFO: Uvicorn running on http://0.0.0.0:8000
```

---

# Step 7: Configure the AWS Security Group

Edit the EC2 Security Group and add an inbound rule.

| Type | Protocol | Port | Source |
|------|----------|------|--------|
| Custom TCP | TCP | 8000 | 0.0.0.0/0 |

This allows external users to access the API.

---

# Step 8: Verify the Deployment

API Home:

```
http://YOUR_PUBLIC_IP:8000/
```

Expected response:

```json
{
  "message": "Car Price Prediction API is Ready!"
}
```

Swagger Documentation:

```
http://YOUR_PUBLIC_IP:8000/docs
```

---

# Deployment Summary

The application is successfully deployed on AWS EC2 and is publicly accessible through the FastAPI endpoints.

The deployment demonstrates:

- Machine Learning model deployment
- FastAPI REST API development
- AWS EC2 cloud hosting
- Linux server configuration
- Public API deployment
- Security Group configuration
