# Stage 4: App configuration
This is the fourth stage of development, which adds the usage of [`ConfigParser`](https://docs.python.org/3/library/configparser.html) and makes the application read its configuration from `config.ini` during startup. This stage also shows how well app configuration integrates with dependency injection. The goal is to keep the codebase simple and showcase basic app configuration concepts.

## Project Structure
- `app.py`: Main entry point for the Flask application. Ensures that dependency injection is configured and the database is created and seeded on startup.
- `routes/`: Contains the route handlers for the API (e.g. `sightseeing_routes.py`).
- `models/`: Contains data models (e.g., `sightseeing.py`). `sightseeing.py` is now a SQLAlchemy ORM model.
- `dto/`: Contains Data Transfer Objects (DTOs) used to define the structure of data returned or consumed by the API endpoints (e.g. `sightseeing_page.py`).
- `services/`: Contains service logic (e.g., `sightseeing_service.py`). All data access is now via SQLAlchemy and the database. The `SightseeingService` class now accepts a `sessionmaker[Session]` parameter in its constructor, which is automatically provided by the dependency injection container when an instance of `SightseeingService` is created.
- `database/`: Contains database setup and seeding logic (`db.py`).
- `configuration/`: Contains a simple `AppConfig` class which holds the application's configuration.
- `dependencyinjection/`: Contains the logic that registers app configuration and services in a dependency injection container (`di.py`).
- `app.http`: Example HTTP requests for testing the API.

#### Application configuration notes
- The application's configuration is managed by the `AppConfig` class, located in the `app_config` module.
- When we create an instance of `AppConfig`, it reads configuration values from `config.ini` and stores them into its attributes. These values are then accessible throughout the application.
- Additionally, we can set the environment variable `SIGHTSEEINGS_ENVIRONMENT`. When this variable is set, the `AppConfig` instance will store its value in the `self.environment` attribute and attempt to load additional configuration from the file `f"config.{self.environment}.ini"`. If this environment-specific file exists, its values will supplement or override those from the base `config.ini`.
- In `di.py`, we create an instance of `AppConfig` and register it as a singleton in our dependency injection (DI) container. Then when we are configuring the database session with `sessionmaker(...)`, this singleton instance is resolved from the container, and its database connection string is passed to `sessionmaker(...)`.

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
1. Clone this repository using git and switch to the branch "4_configuration" or simply download this branch as a zip
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