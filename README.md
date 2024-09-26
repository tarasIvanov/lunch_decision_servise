
# Lunch Decision Service

This is a Django-based web application designed to help users decide where to have lunch. It leverages Django REST framework and JWT for authentication.

PC: I was not familiar with technologies like Django, DWF, JWT and Docker. I was preparing to write a program using Flask and libraries of the type (werkzeug, sqlalchemy.orm), because the vacancy indicated that these technologies are also in demand. Nevertheless, I did what I could and will finish this task in some time

## Features

- User authentication with JWT
- Restaurant management
- RESTful API endpoints

## Requirements

- Python 3.x
- Django 5.1.1
- PostgreSQL

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/dimasik142/lunch_decision_service.git
    cd lunch_decision_service
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the PostgreSQL database and update the `DATABASES` settings in `lunch_decision_service/settings.py` accordingly.

5. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

6. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

7. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage

- Access the admin panel at `http://127.0.0.1:8000/admin/` to manage restaurants.
- Use the API endpoints to interact with the application.

## Settings

- `DEBUG`: Set to `False` in production.
- `SECRET_KEY`: Keep this secure in production.
- `ALLOWED_HOSTS`: Add your domain here in production.
