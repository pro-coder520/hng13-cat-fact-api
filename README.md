
# Django Profile API with Cat Facts

This is a simple RESTful API built with Django and Django REST Framework. It provides a single endpoint `/me` that returns static user profile information along with a dynamic, randomly fetched cat fact from an external API.

This project serves as a practical example of:

  * Building a basic API endpoint with Django REST Framework.
  * Consuming a third-party API (`https://catfact.ninja/fact`).
  * Formatting JSON responses.
  * Handling external API errors gracefully.
  * Generating dynamic data like UTC timestamps.

## Features

  - **GET `/me` Endpoint**: A single endpoint to retrieve profile data.
  - **Dynamic Data**: Fetches a new cat fact and the current UTC timestamp for every request.
  - **Structured JSON Response**: Returns data in a consistent and well-defined JSON format.
  - **Error Handling**: Gracefully handles potential network errors or failures when communicating with the Cat Facts API.

## Technology Stack

  - **Backend**: Python 3, Django
  - **API Framework**: Django REST Framework
  - **HTTP Client**: Python `requests` library

## Prerequisites

Before you begin, ensure you have the following installed on your system:

  - Python 3.8+
  - `pip` (Python package installer)
  - `venv` (for creating virtual environments)

## Setup and Installation

Follow these steps to get the project running locally.

**1. Clone the repository:**

```bash
git clone https://github.com/your-username/profile_api.git
cd profile_api
```

**2. Create and activate a virtual environment:**

This isolates the project's dependencies from your global Python installation.

  - **On macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
  - **On Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

**3. Install dependencies:**

The `requirements.txt` file contains all the necessary Python packages.

```bash
pip install -r requirements.txt
```

> **Note**: If you don't have a `requirements.txt` file, you can create one from your project with `pip freeze > requirements.txt` after installing `django`, `djangorestframework`, and `requests`.

**4. Run database migrations:**

Although we are not using a database for this specific endpoint, it's a standard step in setting up a Django project.

```bash
python manage.py migrate
```

**5. Personalize your information:**

Open `user_profile/views.py` and update the `user_data` dictionary with your personal information.

```python
# user_profile/views.py

...
    # 1. Prepare your personal information
    user_data = {
        "email": "youremail@example.com", # <-- Change this
        "name": "Your Full Name",        # <-- Change this
        "stack": "Python/Django"         # <-- Change this
    }
...
```

## Running the Application

Once the setup is complete, start the Django development server:

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoint Documentation

### Get Profile Information

  - **Endpoint**: `GET /me`
  - **Description**: Retrieves static user profile information and a dynamic cat fact.
  - **Method**: `GET`
  - **Headers**:
      - `Content-Type: application/json`

-----

#### **Success Response (200 OK)**

The endpoint returns a JSON object with the user's details, a timestamp, and a cat fact. The `timestamp` and `fact` fields are regenerated on every request.

**Example Response:**

```json
{
  "status": "success",
  "user": {
    "email": "youremail@example.com",
    "name": "Your Full Name",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-19T14:05:22.123456Z",
  "fact": "Cats have over 20 muscles that control their ears."
}
```

-----

#### **Error Handling**

If the external Cat Facts API (`https://catfact.ninja/fact`) is unavailable or returns an error, the endpoint will not fail. Instead, it will return a `200 OK` status with a fallback message in the `fact` field.

**Example Response (when Cat Facts API fails):**

```json
{
  "status": "success",
  "user": {
    "email": "youremail@example.com",
    "name": "Your Full Name",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-19T14:08:10.987654Z",
  "fact": "Failed to fetch a cat fact due to a network error."
}
```

## Running with Environment Variables (Best Practice)

For a more production-ready setup, you should not hardcode personal information in the source code. Instead, use environment variables.

1.  Create a `.env` file in the project's root directory:

    ```
    USER_EMAIL="your_actual_email@example.com"
    USER_NAME="Your Actual Name"
    USER_STACK="Python/Django"
    ```

2.  Install a library to read the `.env` file, like `python-dotenv`:

    ```bash
    pip install python-dotenv
    ```

3.  Modify `user_profile/views.py` to load these variables:

    ```python
    # user_profile/views.py
    import os
    from dotenv import load_dotenv
    # or use: from decouple import config

    # Load environment variables from .env file
    load_dotenv() # if using decouple, no need for this

    # ... inside get_my_profile view ...
    user_data = {
        "email": os.getenv("USER_EMAIL", "default@example.com"),
        "name": os.getenv("USER_NAME", "Default User"),
        "stack": os.getenv("USER_STACK", "Default Stack")
    }
    # ...
    ```

4.  Add `.env` to your `.gitignore` file to prevent committing sensitive information.