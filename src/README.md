# Stage 5: Tests
This is the fifth stage of development, which adds unit tests for services, models, dtos, and also integration tests for the whole API using [pytest](https://docs.pytest.org/en/stable). The goal is to keep the codebase simple and showcase basic unit testing concepts.

## Project Structure
- `app.py`: Main entry point for the Flask application. Ensures that dependency injection is configured and the database is created and seeded on startup.
- `routes/`: Contains the route handlers for the API (e.g. `sightseeing_routes.py`).
- `models/`: Contains data models (e.g., `sightseeing.py`). `sightseeing.py` is now a SQLAlchemy ORM model.
- `dto/`: Contains Data Transfer Objects (DTOs) used to define the structure of data returned or consumed by the API endpoints (e.g. `sightseeing_page.py`).
- `services/`: Contains service logic (e.g., `sightseeing_service.py`). All data access is now via SQLAlchemy and the database. The `SightseeingService` class now accepts a `sessionmaker[Session]` parameter in its constructor, which is automatically provided by the dependency injection container when an instance of `SightseeingService` is created.
- `database/`: Contains database setup and seeding logic (`db.py`).
- `configuration/`: Contains a simple `AppConfig` class which holds the application's configuration.
- `dependencyinjection/`: Contains the logic that registers app configuration and services in a dependency injection container (`di.py`).
- `tests/`: Contains unit and integration tests covering services, models, DTOs and route handlers.
- `app.http`: Example HTTP requests for testing the API.

#### Unit test notes
- Tests are organized per module in files named `test_{folder}_{module}.py` or `test_{folder}_{module}_{suffix}.py`.
- After creating the virtual environment and installing dependencies, run tests from the terminal:
  - `pytest tests` - full test suite
  - `pytest tests/test_routes_sightseeing_routes.py` - single file
  - `pytest tests/test_routes_sightseeing_routes.py::test_crud_happy_path` - single test
- In VSCode open the Testing view (Ctrl+Shift+P → type "show testing" → select "View: Show Testing" or use the Testing sidebar) to run or debug individual tests.

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
1. Clone this repository using git and switch to the branch "5_tests" or simply download this branch as a zip
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