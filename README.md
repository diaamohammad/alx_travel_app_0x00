# ALX Travel App (alx_travel_app_0x00)

This is the backend service for the ALX Travel App. This repository contains **Milestone 2**, which focuses on building the core database structure and populating it with test data.

## 📍 Milestone 2: Database Modeling & Seeding

This milestone builds on the first by adding:

* **Database Models**: `Listing`, `Booking`, and `Review` models created in `listings/models.py`.
* **Serializers**: `ModelSerializers` for `Listing`, `Booking`, and `Review` to translate data to/from JSON.
* **Data Seeding**: A custom management command (`seed.py`) using `Faker` to populate the database with realistic test data.

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
CREATE DATABASE your_database_name;
2. Installation
Clone the repository:

Bash

git clone https://github.com/diaamohammad/alx_travel_app_0x00.git
cd alx_travel_app_0x00
Create and activate a virtual environment:

Bash

# For Windows
python -m venv venv
.\venv\Scripts\activate
Install the dependencies: (This now includes faker)

Bash

pip install -r requirements.txt
3. Configuration
This project uses a .env file to manage all environment variables.

Create a file named .env in the project root (next to manage.py).

Copy the contents of the template below into your new .env file.

Important: You must replace the placeholder values (like your_database_name, your_db_user, etc.) with your actual MySQL credentials.

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
# (Replace these with your own database credentials)
DB_NAME=your_database_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=127.0.0.1
DB_PORT=3306
4. Running the Application
Apply the database migrations: This will create the new Listing, Booking, and Review tables in your database.

Bash

python manage.py makemigrations listing
python manage.py migrate
Seed the database (Optional but Recommended): This will run the seed.py command to populate your new tables with fake data for testing.

Bash

python manage.py seed
Run the development server:

Bash

python manage.py runserver
The server will be running at http://127.0.0.1:8000/