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

To configure this project for development or production, follow these steps:

### 1. Use the .env file as a Template

Start by changing the variables inside the "your.env" file. It's a sample file reflecting all the required environment variables for this project. After setting the values inside this file, simply rename it to .env
Note that "your.env" is just a sample which ultimately should be renamed to .env in order for this app to run properly.

### 2. Choose Your Environment Mode

Inside .env, set the DEBUG variable to True or False depending on your intended environment; either development or production.

All settings are controlled via the ".env" file which exists at the project root:

This file has the following variables which must be set before starting the app.

DEBUG=True or False
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=yourpassword
DB_HOST=localhost  # Use 'db' instead of 'localhost' when running inside Docker
DB_PORT=5432

### Note that the values are not to be quoted and there shouldn't be a whitespace at the left and right side of the equal sign.

DEBUG=True enables development mode with live reload.
DEBUG=False switches to production mode with Gunicorn.

## Installation with Docker 

For using the containerized version of the app you need to set DB_HOST=db

After setting the rest of the variables in .env, simply run:
```
docker-compose up --build
```

## Installation Without Docker 

After cloning the repo, go through the following steps

1) Make your virtual environment:
```
python -m venv venv
```

2) Activate the virtual environment:
windows users:
```
.\venv\Scripts\activate
```

MacOS or Linux users:
```
source venv/bin/activate
```

3) install the required packages:
```
pip install -r requirements.txt
```

4) install postgresql on your machine.

5) make a database and a postgresql user and give the user the required privileges:
Customize the following command based on your .env file

a) Open psql:
```
psql -U postgres
```

b) Create the user:
```
CREATE USER your_user WITH PASSWORD 'your_password';
```

c) Create the database:
```
CREATE DATABASE your_database OWNER your_user;
```

d) Grant privileges:
```
GRANT ALL PRIVILEGES ON DATABASE your_database TO your_user;
```

e) Grant more privileges in order for tests to work:
```
ALTER USER your_user CREATEDB;
```

6) Go to the root of the project where "manage.py" exists and run:
```
python manage.py makemigrations
```

7) migrate:
```
python manage.py migrate
```

8) And finally run the server:
```
python manage.py runserver
```

🧪 Running Tests

Run the full test suite inside Docker:
```
docker-compose run web pytest
```

local users who don't like docker:
```
pytest
```

📚 API Documentation
After running the server, you can go to http://localhost:8000/api/v1/swagger/ to explore the API using Swagger UI.

And as always enjoy coding.