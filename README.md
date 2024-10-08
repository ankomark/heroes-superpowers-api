# heroes-superpowers-api
## Heroes and Superpowers API

This project is an API built to manage and track heroes and their superpowers. It includes endpoints to create, read, and update heroes and their associated superpowers. The API is developed using **Flask** and **SQLAlchemy**, and tested via **Postman**.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [How to Run the Application](#how-to-run-the-application)
- [Database](#database)
- [API Endpoints](#api-endpoints)
- [Testing the API with Postman](#testing-the-api-with-postman)
- [Contributing](#contributing)
- [Author](#Author)

## Features

- Create, Read, Update operations for heroes and their superpowers.
- Manage a list of heroes and their unique abilities.
- API for tracking heroes, with validation to ensure data integrity.
- Fully tested using Postman collection for all routes.

---

## Technologies Used

- **Flask**: Micro web framework for Python used to build the API.
- **Flask-SQLAlchemy**: ORM to interact with the database.
- **Flask-Migrate**: Database migration tool.
- **SQLite**: Lightweight database for development.
- **Postman**: Used to test and interact with the API.

---

## Setup Instructions

1. **Clone the Repository**
   
   ```bash
   git clone https://github.com/SharonMawiaJohn/heroes-superpowers-api.git
   cd heroes-superpowers-api

2. **Create a Virtual Environment**

Create a virtual environment to keep dependencies isolated.

    pipenv install ; pipenv shell

3. **Set Up Environment Variables**

    Create a .env file in the root of the project and add the following environment variables:

    FLASK_APP=app.py
    FLASK_ENV=development
    SQLALCHEMY_DATABASE_URI=sqlite:///heroes.db
    SQLALCHEMY_TRACK_MODIFICATIONS=False

4. **Initialize the Database**

    Apply migrations to create the database schema:

        flask db init
        flask db migrate -m "Initial migration"
        flask db upgrade head
        python3 seed.py
        export FLASK_APP=app.py
        export FLASK_RUN_PORT=5555

## how-to-run-the-application
    
1. Run the Flask Development Server

    Start the server using Flask's built-in development server:
    
        python3 app.py

2. The server should start on http://127.0.0.1:5555. You can now interact with the API using Postman or any other API client.
    For example http://127.0.0.1:5555/heroes to view heroes.

## database

This project uses SQLite for database management. The database stores information about heroes and their superpowers
¬


## api-endpoints

    a. GET /heroes
    Description: Retrieves a list of all heroes with their IDs, names, and super names.
    Response: Returns a JSON array containing all heroes.

    b. GET /heroes/
    Description: Retrieves a specific hero by their id and includes the hero's associated powers.
    Successful Response:
    If the Hero exists, it returns a JSON object with the hero's details and their associated powers.

    c. GET /powers
    Description: Retrieves a list of all powers.
    Response: Returns a JSON array containing all powers

    d. GET /powers/
    Description: Retrieves a specific power by its id.
    Successful Response:
    If the Power exists, returns a JSON object.

    e. PATCH /powers/
    Description: Updates an existing Power by its id.
    Request Body: Accepts an object in the body of the request.

    f. POST /hero_powers
    Description: Creates a new HeroPower that associates a Hero with a Power and defines the strength of the power.
    Request Body: Accepts an object in the body of the request.

## testing-the-api-with-postman

1. Postman Setup in VS Code
    
If you have the Postman extension installed in VS Code, follow these steps to use it:

    a. Open Postman in VS Code
    Go to the Postman panel in VS Code. You should be able to access it from the sidebar or search for "Postman" using the command palette (Ctrl + Shift + P).

    b. Import the Postman Collection
    In the Postman console, go to the Import option (usually a button at the top).
    Select the .json file of the Postman collection you downloaded, and import it.
    The imported collection will display the required endpoints for your API.

2. Testing the Endpoints

Once the collection is imported, you can start testing the API. Here's how to proceed:

    a. GET Requests

        For example, to test the GET /heroes endpoint:
        Select the GET /heroes request from the imported collection.
        Click the Send button.
        You should see a response with a JSON array of all heroes.

    b. GET /
    Requests

        To test fetching a hero by ID, select GET /heroes/:id.
        In Postman, replace :id with an actual hero ID (e.g., 1).
        Send the request to see the response.
        If the hero exists, you’ll get the hero's details along with their associated powers. If not, you’ll get a "Hero not found" error.

    c. PATCH Requests

        To test updating a power's description:
        Select the PATCH /powers/:id request.

        Set the :id parameter to the ID of the power you want to update.

        Go to the Body section and select raw, then set the format to JSON.

        Provide the JSON payload, such as:

        {
        "description": "Updated Power Description"
        }

        Send the request to test the update. If successful, you’ll see the updated power.

    d. POST Requests

        For creating a new HeroPower:
        Select the POST /hero_powers request.

        In the Body section, input the required JSON payload:

        {
        "strength": "Average",
        "power_id": 1,
        "hero_id": 3
        }

        Send the request. If successful, you’ll get a response with the newly created HeroPower.

4. Check Status Codes and Responses

    Successful Requests: You should see HTTP status codes like 200 OK or 201 Created along with the corresponding JSON data in the response.
    Unsuccessful Requests: If there's an issue (like trying to fetch a non-existent hero), you’ll see the appropriate error response, such as 404 Not Found.

5. Testing Validation Errors

    To check how the API handles validation errors, try sending invalid data in the PATCH or POST requests. For example, submit an invalid strength value in the POST /hero_powers request to trigger the validation error response.

6. Debugging Issues

    If something doesn’t work, check the terminal where Flask is running to see if there are any error messages or stack traces.
    Ensure the URL is correct and matches the Flask server’s port.


## contributing

    Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

    Fork the repository.
    Create a new feature branch.
    Make your changes and commit them.
    Push to your branch and submit a pull request.
    Please make sure your code adheres to the project's style guidelines and is fully tested.

## Author

    Sharon John