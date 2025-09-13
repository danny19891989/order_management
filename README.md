# 🛠️ Order Management API

A modular, secure, and scalable Django REST Framework project for managing orders with role-based access control, JWT authentication, and Swagger documentation. Built for both rapid development and production deployment using Docker.

---

## 🚀 Features

- 🔐 JWT-based authentication via `rest_framework_simplejwt`
- 👥 Role-based access control for customers, managers, and unauthenticated users
- 📦 Modular architecture with separate `userauth` and `orders` apps
- 🧪 Pytest-powered test suite with custom fixtures
- 🐳 Dockerized for seamless development and deployment
- 📘 Swagger UI integration for interactive API docs

---

## ⚙️ Environment Configuration

Setup Instructions

To configure this project for development or production, follow these steps:
🔹 1. Use your.env as a Template

Start by copying the provided your.env file. It contains all the required environment variables for this project.

🔹 2. Choose Your Environment Mode

Inside .env, set the DEBUG variable based on your intended environment:
Development Mode or Production Mode

All settings are controlled via a single `.env` file at the project root:

```env
DEBUG=True or False
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=yourpassword
DB_HOST=localhost  # Use 'db' when running inside Docker
DB_PORT=5432


DEBUG=True enables development mode with live reload
DEBUG=False switches to production mode with Gunicorn


🐳 Docker Setup
🔹 Build and Run (Development)
bash

docker-compose up --build

    Uses python manage.py runserver

    Mounts local code as a volume for live editing

    Reads from .env to configure Django and PostgreSQL

🔹 Build and Run (Production)

Update .env by:
DEBUG=False
DB_HOST=db

Then run:
docker-compose up --build

Uses gunicorn for production-grade serving

No volume mount (for performance and isolation)

🧪 Running Tests

Run the full test suite inside Docker:
docker-compose run web pytest

Or locally:
pytest

📚 API Documentation
More importantly you can go to http://localhost:8000/swagger after running the server to explore the API using Swagger UI.