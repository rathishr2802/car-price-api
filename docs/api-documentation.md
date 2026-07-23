# 📘 API Documentation

## Base URL

```
http://YOUR_PUBLIC_IP:8000
```

---

## Health Check

### Endpoint

```
GET /
```

### Description

Returns a message indicating that the API is running successfully.

### Sample Response

```json
{
    "message": "Car Price Prediction API is Ready!"
}
```

---

## Predict Car Price

### Endpoint

```
POST /predict
```

### Description

Predicts the estimated price of a car based on the provided input features.

### Request Body

Example:

```json
{
    "year": 2018,
    "present_price": 7.5,
    "kms_driven": 35000,
    "fuel_type": "Petrol",
    "seller_type": "Dealer",
    "transmission": "Manual",
    "owner": 0
}
```

### Response

```json
{
    "predicted_price": 5.82
}
```

---

## Interactive API Documentation

FastAPI automatically provides Swagger UI.

Open:

```
http://YOUR_PUBLIC_IP:8000/docs
```

There you can:

- Test endpoints
- View request schemas
- View response schemas
- Execute API calls directly from the browser
