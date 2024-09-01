# API Endpoints Documentation

## Overview

This document provides a detailed overview of the API endpoints available for user authentication, property management, tenant management, rental payment monitoring, and email notifications.

## Base URL

http://127.0.0.1:8000/myapi/



## Endpoints

### 1. User Authentication and Management

- **Register a New User**
  - **Endpoint**: `/register/`
  - **Method**: POST
  - **Description**: Registers a new user in the system.
  - **Request Body**:
    ```json
    {
      "username": "string",
      "password": "string",
      "email": "string"
    }
    ```
  - **Response**:
    - `201 Created`: User successfully registered.
    - `400 Bad Request`: Validation error.

- **Log In a User**
  - **Endpoint**: `/login/`
  - **Method**: POST
  - **Description**: Logs in a user and returns a JWT token.
  - **Request Body**:
    ```json
    {
      "username": "string",
      "password": "string"
    }
    ```
  - **Response**:
    - `200 OK`: Returns JWT token.
    - `401 Unauthorized`: Invalid credentials.

- **Retrieve User Profile**
  - **Endpoint**: `/profile/`
  - **Method**: GET
  - **Description**: Retrieves the profile of the logged-in user.
  - **Response**:
    - `200 OK`: Returns the user profile.
    - `401 Unauthorized`: User not authenticated.

- **Refresh Access Token**
  - **Endpoint**: `/refresh/`
  - **Method**: POST
  - **Description**: Refreshes the user's access token using a valid refresh token.
  - **Request Body**:
    - `refresh` (string): The refresh token obtained during the initial authentication.
  - **Response**:
    - `200 OK`: Returns a new access token.
    - `400 Bad Request`: The request was malformed or missing required fields.
    - `401 Unauthorized`: Invalid or expired refresh token.


### 2. Property Management

- **List All Properties**
  - **Endpoint**: `/properties/`
  - **Method**: GET
  - **Description**: Lists all properties associated with the logged-in user.
  - **Response**:
    - `200 OK`: Returns a list of properties.
    - `401 Unauthorized`: User not authenticated.


- **Create a New Property**
  - **Endpoint**: `/properties/`
  - **Method**: POST
  - **Description**: Creates a new property for the logged-in user.
  - **Request Body**:
    ```json
    {
      "property_name": "string",
      "address": "string",
      "description": "string",
      "type": "string",
      "units": "integer",
      "rental_cost": "number",
      "property_image": "string (base64 encoded image or image file path)"
    }
    ```
  - **Response**:
    - `201 Created`: Property created successfully.
    - `400 Bad Request`: Validation error.
    - `401 Unauthorized`: User not authenticated.


- **Retrieve Property Details**
  - **Endpoint**: `/properties/<id>/`
  - **Method**: GET
  - **Description**: Retrieves details of a specific property by its ID.
  - **Response**:
    - `200 OK`: Returns property details.
    - `404 Not Found`: Property not found.
    - `401 Unauthorized`: User not authenticated.

- **Update Property Details**
  - **Endpoint**: `/properties/<id>/`
  - **Method**: PUT
  - **Description**: Updates details of a specific property by its ID.
  - **Request Body**:
    ```json
    {
      "property_name": "string",
      "address": "string",
      "description": "string",
      "type": "string",
      "units": "integer",
      "rental_cost": "number",
      "property_image": "string (base64 encoded image or image file path)"
    }
    ```
  - **Response**:
    - `200 OK`: Property updated successfully.
    - `400 Bad Request`: Validation error.
    - `404 Not Found`: Property not found.
    - `401 Unauthorized`: User not authenticated.

- **Delete a Property**
  - **Endpoint**: `/properties/<id>/`
  - **Method**: DELETE
  - **Description**: Deletes a specific property by its ID.
  - **Response**:
    - `204 No Content`: Property deleted successfully.
    - `404 Not Found`: Property not found.
    - `401 Unauthorized`: User not authenticated.
    - `403 Forbidden`: User does not have permission to delete the property.


### 3. Tenant Management

- **List All Tenants**
  - **Endpoint**: `/properties/<id>/tenants/`
  - **Method**: GET
  - **Description**: Lists all tenants associated with a specific property by its ID.
  - **Response**:
    - `200 OK`: Returns a list of tenants.
    - `404 Not Found`: Property not found.
    - `401 Unauthorized`: User not authenticated.

- **Add a New Tenant**
  - **Endpoint**: `/properties/<id>/tenants/`
  - **Method**: POST
  - **Description**: Adds a new tenant to a specific property.
  - **Request Body**:
    ```json
    {
      "name": "string",
      "email": "string",
      "phone_number": "string",
      "unit": "string"
    }
    ```
  - **Response**:
    - `201 Created`: Tenant added successfully.
    - `400 Bad Request`: Validation error.
    - `404 Not Found`: Property not found.
    - `401 Unauthorized`: User not authenticated.


- **Retrieve Tenant Details**
  - **Endpoint**: `/tenants/<id>/`
  - **Method**: GET
  - **Description**: Retrieves details of a specific tenant by their ID.
  - **Response**:
    - `200 OK`: Returns tenant details.
    - `404 Not Found`: Tenant not found.
    - `401 Unauthorized`: User not authenticated.

- **Update Tenant Details**
  - **Endpoint**: `/tenants/<id>/`
  - **Method**: PUT
  - **Description**: Updates details of a specific tenant by their ID.
  - **Request Body**:
    ```json
    {
      "name": "string",
      "email": "string",
      "phone_number": "string",
      "unit": "string"
    }
    ```
  - **Response**:
    - `200 OK`: Tenant updated successfully.
    - `400 Bad Request`: Validation error.
    - `404 Not Found`: Tenant not found.
    - `401 Unauthorized`: User not authenticated.

- **Delete a Tenant**
  - **Endpoint**: `/tenants/<id>/`
  - **Method**: DELETE
  - **Description**: Deletes a specific tenant by their ID.
  - **Response**:
    - `204 No Content`: Tenant deleted successfully.
    - `404 Not Found`: Tenant not found.
    - `401 Unauthorized`: User not authenticated.
    - `403 Forbidden`: User does not have permission to delete this tenant.


### 4. Rental Payments Monitoring

- **List All Payments by a Tenant**
  - **Endpoint**: `/tenants/<id>/payments/`
  - **Method**: GET
  - **Description**: Lists all payments made by a specific tenant.
  - **Response**:
    - `200 OK`: Returns a list of payments.
    - `404 Not Found`: Tenant not found.
    - `401 Unauthorized`: User not authenticated.

- **Record a New Payment**
  - **Endpoint**: `/tenants/<id>/payments/`
  - **Method**: POST
  - **Description**: Records a new payment for a specific tenant.
  - **Request Body**:
    ```json
    {
      "amount": "number",
      "date_paid": "date",
      "is_settled": "boolean",
    }
    ```
  - **Response**:
    - `201 Created`: Payment recorded successfully.
    - `400 Bad Request`: Validation error.
    - `404 Not Found`: Tenant not found.
    - `401 Unauthorized`: User not authenticated.

- **Retrieve Payment Details**
  - **Endpoint**: `/payments/<id>/`
  - **Method**: GET
  - **Description**: Retrieves details of a specific payment by its ID.
  - **Response**:
    - `200 OK`: Returns payment details.
    - `404 Not Found`: Payment not found.
    - `401 Unauthorized`: User not authenticated.

- **Update Payment Details**
  - **Endpoint**: `/payments/<id>/`
  - **Method**: PUT
  - **Description**: Updates details of a specific payment by its ID.
  - **Request Body**:
    ```json
    {
      "amount": "number",
      "date_paid": "date",
      "is_settled": "boolean",
    }
    ```
  - **Response**:
    - `200 OK`: Payment updated successfully.
    - `400 Bad Request`: Validation error.
    - `404 Not Found`: Payment not found.
    - `401 Unauthorized`: User not authenticated.

- **Delete a Payment**
  - **Endpoint**: `/payments/<id>/`
  - **Method**: DELETE
  - **Description**: Deletes a specific payment record by its ID.
  - **Response**:
    - `204 No Content`: Payment deleted successfully.
    - `404 Not Found`: Payment not found.
    - `401 Unauthorized`: User not authenticated.

### 5. Email Notifications

- **Trigger a Mock Email Notification**
  - **Endpoint**: `/tenants/<id>/notify/`
  - **Method**: POST
  - **Description**: Triggers a mock email notification
