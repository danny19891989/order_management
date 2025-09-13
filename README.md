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

__Note that the values are not to be quoted and there shouldn't be a whitespace at the left and right side of the equal sign.__

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

1) __Make your virtual environment:__
```
python -m venv venv
```

2) __Activate the virtual environment:__
_windows users:_
```
.\venv\Scripts\activate
```

_MacOS or Linux users:_
```
source venv/bin/activate
```

3) __install the required packages:__
```
pip install -r requirements.txt
```

4) __install postgresql on your machine.__

5) __make a database and a postgresql user and give the user the required privileges:__

Customize the following commands based on your .env file

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

6) __Go to the root of the project where "manage.py" exists and run:__
```
python manage.py makemigrations
```

7) __migrate:__
```
python manage.py migrate
```

8) __And finally run the server:__
```
python manage.py runserver
```

## 🧪 Running Tests

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

_And as always enjoy coding._