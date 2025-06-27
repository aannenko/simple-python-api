# Stage 2: SQLAlchemy and SQLite
This is the second stage of development, focusing on integration of the existing [Flask Web API](https://flask.palletsprojects.com/en/stable/quickstart/) with [SQLAlchemy](https://docs.sqlalchemy.org/en/20/orm/quickstart.html) and [SQLite](https://sqlite.org/). The goal is to keep the codebase simple and showcase basic interaction with databases.

## Project Structure
- `app.py`: Main entry point for the Flask application. Handles API routes and ensures the database is created and seeded on startup.
- `Models/`: Contains data models (e.g., `sightseeing.py`). `sightseeing.py` is now a SQLAlchemy ORM model.
- `DTO/`: Contains Data Transfer Objects (DTOs) used to define the structure of data returned or consumed by the API endpoints (e.g. `sightseeing_page.py`).
- `Services/`: Contains service logic (e.g., `sightseeing_service.py`). All data access is now via SQLAlchemy and the database.
- `Database/`: Contains database setup (`db.py`) and seeding logic (`seed.py`).
- `app.http`: Example HTTP requests for testing the API.

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
1. Clone this repository using git and switch to the branch "2_sqlalchemy" or simply download this branch as a zip
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

#### Database setup and seeding
- The database is automatically created and seeded with initial sightseeing data when you start the app.
- If you want to reseed or reset the database, you can run the seeding logic manually (see `Database/seed.py`).

#### Run the application
In VSCode press F5 to run the application.<br/>
Open the file `app.http` and try sending requests from it to your app.
