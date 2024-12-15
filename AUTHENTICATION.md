# Authentication Setup

## Overview
This API uses token-based authentication provided by Django REST Framework SimpleJWT. Users must authenticate to access protected endpoints.

---

## Endpoints

1. **Obtain Token**
   - **URL**: `/api/token/`
   - **Method**: POST
   - **Request Body**:
     ```json
     {
         "username": "string",
         "password": "string"
     }
     ```
   - **Response**:
     ```json
     {
         "access": "access_token",
         "refresh": "refresh_token"
     }
     ```

2. **Refresh Token**
   - **URL**: `/api/token/refresh/`
   - **Method**: POST
   - **Request Body**:
     ```json
     {
         "refresh": "refresh_token"
     }
     ```
   - **Response**:
     ```json
     {
         "access": "new_access_token"
     }
     ```

---

## How to Test
1. Obtain an access token via `/api/token/`.
2. Use the token in the `Authorization` header for secured endpoints:
