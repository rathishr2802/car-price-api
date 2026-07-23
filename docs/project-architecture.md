# 🏗️ Project Architecture

## Overview

The Car Price Prediction API follows a simple Machine Learning deployment architecture.

```
                User
                  │
                  ▼
        HTTP Request (JSON)
                  │
                  ▼
             FastAPI Server
                  │
                  ▼
        Data Preprocessing
          (Feature Scaling)
                  │
                  ▼
      Trained Machine Learning Model
                  │
                  ▼
        Predicted Car Price
                  │
                  ▼
           JSON Response
```

---

## Components

### Client

The client sends vehicle information through an HTTP request.

Examples:

- Swagger UI
- Web Application
- Postman
- Python Requests

---

### FastAPI

FastAPI receives the request, validates the input, and forwards the processed data to the Machine Learning model.

---

### Scaler

The saved scaler (`scaler.pkl`) transforms the input data into the same format used during model training.

---

### Machine Learning Model

The trained model (`car_price_model.pkl`) predicts the estimated car price.

---

### Response

The prediction is returned as a JSON response to the client.

Example:

```json
{
    "predicted_price": 825000
}
```

---

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Scikit-learn
- Joblib
- AWS EC2
- Ubuntu Linux
- REST API
