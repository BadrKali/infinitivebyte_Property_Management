# property management system

## Overview

This is the backend for a property management system, built with Django and Django REST Framework. The project includes authentication, property management, tenant management, and payment recording functionalities.

## Features

- User registration and authentication
- Property management (create,edit,list, delete)
- Tenant management (add,edit,delete)
- Payment recording for tenants

## Installation

### Prerequisites

- Python 3.8+
- Django 4.x
- Django REST Framework

### Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

## API Documentation

For a detailed explanation of the API endpoints and their usage, please refer to [API documentation](https://github.com/BadrKali/infinitivebyte_Property_Management_Application/blob/main/backend/api-endpoints.md).

This documentation provides comprehensive information about:
- Available endpoints
- Request methods
- Required parameters
- Response formats
- Authentication requirements

