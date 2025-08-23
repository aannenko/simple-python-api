# Stage 2: SQLAlchemy and SQLite
This is the second stage of development, focusing on integration of the existing [Flask Web API](https://flask.palletsprojects.com/en/stable/quickstart/) with [SQLAlchemy](https://docs.sqlalchemy.org/en/20/orm/quickstart.html) and [SQLite](https://sqlite.org/). The goal is to keep the codebase simple and showcase basic interaction with databases.

## Project Structure
- `app.py`: Main entry point for the Flask application. Ensures the database is created and seeded on startup.
- `routes/`: Contains the route handlers for the API (e.g. `sightseeing_routes.py`).
- `models/`: Contains data models (e.g., `sightseeing.py`). `sightseeing.py` is now a SQLAlchemy ORM model.
- `dto/`: Contains Data Transfer Objects (DTOs) used to define the structure of data returned or consumed by the API endpoints (e.g. `sightseeing_page.py`).
- `services/`: Contains service logic (e.g., `sightseeing_service.py`). All data access is now via SQLAlchemy and the database.
- `database/`: Contains database setup and seeding logic (`db.py`).
- `app.http`: Example HTTP requests for testing the API.

#### Database notes
- The database is automatically created and seeded with initial sightseeing data when you start the app.

## Getting started
To run and debug this application, you will need:

#### Applications
- [Python](https://www.python.org/downloads/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Git](https://git-scm.com/) (optional)

#### Visual Studio Code extensions
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python): Python language support, linting, and debugging.
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance): Fast, feature-rich language support for Python.
- [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client): Send HTTP requests directly from VS Code (useful for .http files).

#### Prepare environment
1. Clone this repository using git and switch to the branch "2_database" or simply download this branch as a zip
2. Open `src/` folder in Visual Studio Code
3. In VSCode press `Ctrl+Shift+P` and select:
    1. "Python: Create Environment..."
    2. "Venv"
    3. Your Python installation
    4. Check "requirements.txt" and click "OK" button

At this point you should have `.venv` created and dependencies from `requirements.txt` installed.

What VSCode did for you is similar to the following sequence of commands:
```powershell
python -m venv .venv
python -m pip install -r requirements.txt
```

#### Run the application
In VSCode press F5 to run the application.<br/>
Open the file `app.http` and try sending requests from it to your app.