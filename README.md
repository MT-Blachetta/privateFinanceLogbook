 
# Personal Finance Logbook (PFM) Backend API

[![Language](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-FastAPI-green.svg)](https://fastapi.tiangolo.com/)
[![Database](https://img.shields.io/badge/Database-PostgreSQL-blue.svg)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE) ## Overview

This project provides the backend API for a modern Personal Finance Management (PFM) application. It's designed to handle data related to income, expenses, categorization, recipients, and associated documents, serving as the central data hub for potential web and mobile (Android) frontends.

The API is built using Python with the high-performance FastAPI framework and leverages PostgreSQL for robust data storage. It aims to provide a clean, well-documented, and efficient interface for managing personal financial data.

## Features

### Core Functionality (Implemented & Planned)

* **User Management:**
    * [x] User Registration (Email/Password)
    * [ ] User Login (JWT Token Generation)
    * [ ] Get Current User (`/me`) endpoint
    * [ ] User Profile Updates
    * [ ] Password Management (Update, Reset - Planned)
* **Payment Items:** (Planned)
    * CRUD operations for tracking income and expenses.
    * Support for positive/negative amounts.
    * Date/Time tracking.
    * Linkage to Recipients, Categories, Invoices, and Images.
    * Handling of periodic/recurring payments.
* **Categorization:** (Planned)
    * User-defined Category Types (e.g., "Expenses", "Income", "Projects").
    * Hierarchical Categories within each type (e.g., Expenses > Household > Food).
    * CRUD operations for Types and Categories.
    * Automatic assignment of parent categories when a sub-category is tagged.
    * Flexible tagging of Payment Items with multiple categories.
* **Recipients:** (Planned)
    * CRUD operations for managing payees/payers (Name, Description, Address).
* **File Handling:** (Planned)
    * Upload and associate Invoice Documents (PDF, Images) with Payment Items.
    * Upload and associate Product/Service Images with Payment Items.
    * Secure storage using cloud services (e.g., S3, GCS).
* **API:**
    * [x] RESTful endpoints built with FastAPI.
    * [x] Automatic, interactive API documentation (Swagger UI & ReDoc).
    * [ ] Secure endpoints using JWT authentication.
    * [ ] Robust data validation using Pydantic.
    * [ ] Filtering and Pagination capabilities (Planned).

## Technology Stack

* **Backend Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **Programming Language:** [Python](https://www.python.org/) (3.10+)
* **Database:** [PostgreSQL](https://www.postgresql.org/)
* **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/) (Async support planned if needed)
* **Database Migrations:** [Alembic](https://alembic.sqlalchemy.org/)
* **Data Validation:** [Pydantic](https://pydantic-docs.helpmanual.io/)
* **Password Hashing:** [Passlib](https://passlib.readthedocs.io/) (with bcrypt)
* **Authentication:** [python-jose](https://python-jose.readthedocs.io/) (for JWT)
* **Server:** [Uvicorn](https://www.uvicorn.org/)
* **Containerization (Recommended):** [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)

## Features

### Core Functionality (Implemented & Planned)

* **User Management:**
    * [x] User Registration (Email/Password)
    * [ ] User Login (JWT Token Generation)
    * [ ] Get Current User (`/me`) endpoint
    * [ ] User Profile Updates
    * [ ] Password Management (Update, Reset - Planned)
* **Payment Items:** (Planned)
    * CRUD operations for tracking income and expenses.
    * Support for positive/negative amounts.
    * Date/Time tracking.
    * Linkage to Recipients, Categories, Invoices, and Images.
    * Handling of periodic/recurring payments.
* **Categorization:** (Planned)
    * User-defined Category Types (e.g., "Expenses", "Income", "Projects").
    * Hierarchical Categories within each type (e.g., Expenses > Household > Food).
    * CRUD operations for Types and Categories.
    * Automatic assignment of parent categories when a sub-category is tagged.
    * Flexible tagging of Payment Items with multiple categories.
* **Recipients:** (Planned)
    * CRUD operations for managing payees/payers (Name, Description, Address).
* **File Handling:** (Planned)
    * Upload and associate Invoice Documents (PDF, Images) with Payment Items.
    * Upload and associate Product/Service Images with Payment Items.
    * Secure storage using cloud services (e.g., S3, GCS).
* **API:**
    * [x] RESTful endpoints built with FastAPI.
    * [x] Automatic, interactive API documentation (Swagger UI & ReDoc).
    * [ ] Secure endpoints using JWT authentication.
    * [ ] Robust data validation using Pydantic.
    * [ ] Filtering and Pagination capabilities (Planned).

## Technology Stack

* **Backend Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **Programming Language:** [Python](https://www.python.org/) (3.10+)
* **Database:** [PostgreSQL](https://www.postgresql.org/)
* **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/) (Async support planned if needed)
* **Database Migrations:** [Alembic](https://alembic.sqlalchemy.org/)
* **Data Validation:** [Pydantic](https://pydantic-docs.helpmanual.io/)
* **Password Hashing:** [Passlib](https://passlib.readthedocs.io/) (with bcrypt)
* **Authentication:** [python-jose](https://python-jose.readthedocs.io/) (for JWT)
* **Server:** [Uvicorn](https://www.uvicorn.org/)
* **Containerization (Recommended):** [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)

## Project Structure

pfm-backend/
├── alembic/               # Alembic migration scripts
├── app/                   # Main application code
│   ├── api/               # API endpoint definitions (routers)
│   ├── core/              # Configuration, settings, security utils
│   ├── crud/              # Create, Read, Update, Delete database logic
│   ├── db/                # Database models (SQLAlchemy), session management
│   └── schemas/           # Pydantic data validation schemas
├── tests/                 # Automated tests (pytest) - [TODO]
├── .env                   # Local environment variables (GIT IGNORED!)
├── .env.example           # Example environment variables
├── .gitignore             # Specifies intentionally untracked files that Git should ignore
├── requirements.txt       # Python dependencies
├── alembic.ini            # Alembic configuration
├── Dockerfile             # Instructions to build the Docker image - [TODO]
└── docker-compose.yml     # Define services for local development (App + DB) - [TODO]

## Prerequisites

Before you begin, ensure you have the following installed:

* **Python:** Version 3.10 or higher.
* **PostgreSQL:** A running PostgreSQL server (version 12+ recommended).
* **Git:** For cloning the repository.
* **Docker & Docker Compose (Recommended):** For an easier setup and consistency across environments.

## Installation & Setup (Local Development)

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd pfm-backend
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Linux/macOS
    python -m venv venv
    source venv/bin/activate

    # Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    * Copy the example environment file:
        ```bash
        cp .env.example .env
        ```
    * **Edit the `.env` file** with your actual database credentials, a strong `SECRET_KEY`, and any other necessary settings.
        * **Important:** The `.env` file contains sensitive information and is listed in `.gitignore`. **Do not commit it to version control.**
        * Generate a strong secret key using `openssl rand -hex 32` or a similar tool.

5.  **Set up PostgreSQL Database:**
    * Ensure your PostgreSQL server is running.
    * Create the database user specified in your `.env` file (e.g., `pfm_user`).
    * Create the database specified in your `.env` file (e.g., `pfm_app_db`) and grant privileges to the user.
        ```sql
        -- Example SQL commands (run as PostgreSQL superuser like 'postgres')
        CREATE USER pfm_user WITH PASSWORD 'supersecretpassword';
        CREATE DATABASE pfm_app_db OWNER pfm_user;
        -- You might need to grant additional privileges depending on your setup
        ```

6.  **Run Database Migrations:**
    * Apply the latest database schema changes using Alembic:
        ```bash
        alembic upgrade head
        ```
    * This command reads `alembic.ini` (which should ideally get DB connection info from your environment or `.env`) and applies migrations found in the `alembic/versions` directory.

## Running the Application

Once the setup is complete, you can run the FastAPI development server:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

--reload: Enables auto-reload on code changes. Ideal for development.
--host 0.0.0.0: Makes the server accessible on your network.
--port 8000: Runs the server on port 8000.
The API will be available at http://localhost:8000.

Database Migrations (Alembic)
Alembic is used to manage database schema changes.

Creating a new migration:
After making changes to your SQLAlchemy models in app/db/models/, generate a new migration script:

Bash

alembic revision --autogenerate -m "Describe your changes here"
Review the generated script in alembic/versions/ before applying.

Applying migrations:
To apply all pending migrations to your database:

Bash

alembic upgrade head
Downgrading migrations:
To revert the last migration:

Bash

alembic downgrade -1
API Documentation
Once the server is running, interactive API documentation is automatically generated by FastAPI:

Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc
Use these interfaces to explore available endpoints, view request/response schemas, and test the API directly from your browser.

Simple Usage Guide / Tutorial
This guide demonstrates how to use the API, focusing on the currently available user creation endpoint.

Goal: Create a new user account via the API.

Steps:

Ensure the backend server is running (see "Running the Application").

Navigate to the Swagger UI documentation in your browser: http://localhost:8000/docs.

Locate the "Users" section and expand the POST /api/v1/users/ endpoint.

Click the "Try it out" button on the right side of the endpoint description.

Edit the "Request body" JSON:
Modify the example JSON to include the email, password, and optionally the full name for the new user.

JSON

{
  "email": "[email address removed]",
  "full_name": "Test User",
  "is_active": true, // Optional, defaults to true
  "is_superuser": false, // Optional, defaults to false
  "password": "aSecurePassword123"
}
Click the "Execute" button.

Observe the response:

Successful Creation: You should receive a 201 Created status code. The "Response body" will contain the details of the newly created user (excluding the password), including their unique id.
Error (e.g., User Exists): If a user with that email already exists, you'll get a 400 Bad Request status code, and the response body will contain an error message like:
JSON

{
  "detail": "The user with this email already exists in the system."
}
Next Steps (Authentication):

Currently, only user creation is implemented without authentication. Future steps will involve:

Implementing a /login/token endpoint.
Sending credentials (email/password) to /login/token to receive a JWT access token.
Including this access_token in the Authorization header (e.g., Authorization: Bearer <your_token>) for all subsequent requests to protected endpoints (like creating payment items, categories, etc.).
Running Tests
[TODO: Add instructions on how to run automated tests, likely using pytest.]

Bash

# Example (once tests are added)
# pytest
Contributing
Contributions are welcome! Please follow these general guidelines:

Fork the repository.
Create a new branch for your feature or bugfix (git checkout -b feature/my-new-feature).
Make your changes.
Write tests for your changes (if applicable).
Ensure code follows basic style guidelines (e.g., use a formatter like Black).
Commit your changes (git commit -am 'Add some feature').
Push to the branch (git push origin feature/my-new-feature).
Create a new Pull Request.
Please open an issue first to discuss significant changes.

License:
This project is licensed under the MIT License.

To make this README fully functional:

Add a LICENSE file: Choose an open-source license (MIT is common and permissive) and add the corresponding license text to a file named LICENSE in the project root.
Create .env.example: Create this file in the project root and copy the variable names from your .env file, but without the secret values (or with placeholder examples).
Ini, TOML

# .env.example
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_SERVER=localhost
POSTGRES_PORT=5432
POSTGRES_DB=your_db_name

# Generate with 'openssl rand -hex 32' and keep secret in .env
SECRET_KEY=placeholder_change_in_real_env
Update Placeholders: Fill in the [TODO] sections (like Testing, Docker) as you implement those parts.
Replace <your-repository-url> with the actual URL when you host it.
