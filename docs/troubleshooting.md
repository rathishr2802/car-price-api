# 🔧 Deployment Troubleshooting Guide

## Overview

This document lists the issues encountered during the deployment of the Car Price Prediction API on AWS EC2 and the solutions used to resolve them.

---

# Issue 1: Scikit-learn Version Mismatch

## Error

```text
ModuleNotFoundError: No module named '_loss'
```

## Cause

The Machine Learning model was trained using a different version of Scikit-learn than the version installed on the EC2 instance.

## Solution

- Verified the Scikit-learn version used during model training.
- Installed the matching Scikit-learn version on the deployment server.
- Restarted the application.

---

# Issue 2: Ubuntu Compatibility

## Problem

Installing dependencies on a newer Ubuntu/Python combination caused package installation issues.

## Solution

- Created a new EC2 instance using **Ubuntu Server 24.04 LTS**.
- Reinstalled the project and dependencies.

---

# Issue 3: FastAPI Application Did Not Start

## Problem

Running

```bash
python app.py
```

did not start the API server.

## Cause

FastAPI applications should be served using an ASGI server such as Uvicorn.

## Solution

Started the application using:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

---

# Issue 4: API Not Accessible from Browser

## Problem

The API worked locally but could not be accessed using the EC2 public IP.

## Cause

Port **8000** was not allowed in the EC2 Security Group.

## Solution

Added the following inbound rule:

| Type | Port | Source |
|------|------|--------|
| Custom TCP | 8000 | 0.0.0.0/0 |

---

# Issue 5: Deployment Verification

The following commands were used to verify that the application was running correctly.

Check the API locally:

```bash
curl http://127.0.0.1:8000/
```

Expected response:

```json
{
  "message": "Car Price Prediction API is Ready!"
}
```

Verify that Uvicorn is listening on port 8000:

```bash
sudo ss -tulpn | grep 8000
```

Expected output:

```text
0.0.0.0:8000
```

---

# Lessons Learned

During this deployment, I gained practical experience with:

- FastAPI deployment
- AWS EC2 configuration
- Linux command-line operations
- Python virtual environments
- Scikit-learn dependency management
- EC2 Security Groups
- REST API deployment and verification

These challenges provided valuable hands-on experience in deploying Machine Learning applications to the cloud.
