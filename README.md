# ALX Travel App (alx_travel_app)

This is the backend service for the ALX Travel App, a platform for travel listings. This repository contains the foundational setup (Milestone 1) for the project, built with Django and Django REST Framework.

## 📍 Milestone 1: Setup and Database

This initial milestone includes:
* **Django Project**: A production-ready project structure with a `listings` app.
* **Database**: Configured to connect to a **MySQL** database.
* **Secure Configuration**: Uses `django-environ` to manage all secret keys and settings via a `.env` file.
* **API Documentation**: Automatic API docs generation at `/swagger/` using `drf-yasg`.
* **CORS**: `django-cors-headers` is installed and configured to allow cross-origin requests.
* **Async Tasks**: `Celery` is installed, ready for future background task configuration.

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing.

### 1. Prerequisites

Before you begin, ensure you have the following installed on your system:
* [Python 3.10+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/downloads)
* A running **MySQL** server.

**Important:** You must manually create an empty database in MySQL *before* running the application.
```sql
-- Example command in your MySQL shell:
CREATE DATABASE alx_travel_db;
2. Installation
Clone the repository:

Bash

git clone <your-repository-url>
cd alx_travel_app
Create and activate a virtual environment:

Bash

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
Install the dependencies:

Bash

pip install -r requirements.txt
3. Configuration
This project uses a .env file to manage all environment variables.

Create a file named .env in the project root (next to manage.py).

Copy the contents of the template below into your new .env file and fill in your values.

.env Template:

Ini, TOML

# ===================================
# Django Settings
# ===================================
# (Generate your own key for production)
SECRET_KEY=your-strong-random-secret-key-here
DEBUG=True

# ===================================
# Database Settings (MySQL)
# ===================================
# (This MUST match the database you created in MySQL)
DB_NAME=alx_travel_db
DB_USER=root
DB_PASSWORD=your_actual_password
DB_HOST=127.0.0.1
DB_PORT=3306
4. Running the Application
Apply the database migrations: This will create the default Django tables (like auth, admin, etc.) in your MySQL database.

Bash

python manage.py migrate
Run the development server:

Bash

python manage.py runserver
The server will be running at http://127.0.0.1:8000/

📚 API Documentation (Swagger)
Once the server is running, you can view the live, auto-generated API documentation in your browser.

Swagger UI: http://127.0.0.1:8000/swagger/

ReDoc: http://127.0.0.1:8000/redoc/

(Currently, the documentation will only show basic endpoints until API Views are added to the listings app.)