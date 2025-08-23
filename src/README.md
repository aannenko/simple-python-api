# Stage 3: Dependency Injection using Inject
This is the third stage of development, which integrates the [`inject`](https://github.com/ivankorobkov/python-inject) module into the existing solution that already contains Flask and SQLAlchemy code. The goal is to keep the codebase simple and showcase basic dependency injection concepts.

## Project Structure
- `app.py`: Main entry point for the Flask application. Ensures that dependency injection is configured and the database is created and seeded on startup.
- `routes/`: Contains the route handlers for the API (e.g. `sightseeing_routes.py`).
- `models/`: Contains data models (e.g., `sightseeing.py`). `sightseeing.py` is now a SQLAlchemy ORM model.
- `dto/`: Contains Data Transfer Objects (DTOs) used to define the structure of data returned or consumed by the API endpoints (e.g. `sightseeing_page.py`).
- `services/`: Contains service logic (e.g., `sightseeing_service.py`). All data access is now via SQLAlchemy and the database. The `SightseeingService` class now accepts a `sessionmaker[Session]` parameter in its constructor, which is automatically provided by the dependency injection container when an instance of `SightseeingService` is created.
- `database/`: Contains database setup and seeding logic (`db.py`).
- `dependencyinjection/`: Contains the logic that registers services in a dependency injection container (`di.py`).
- `app.http`: Example HTTP requests for testing the API.

#### Dependency Injection notes
- [`inject`](https://github.com/ivankorobkov/python-inject) is a dependency injection (DI) container, we use it to register our services and their dependencies, internally it builds a dependency graph of these services, e.g. it knows that to create a `SightseeingService` it needs a `sessionmaker[Session]`, which in turn needs SQLAlchemy's `Engine`.
- `di.py` contains a method `configure_inject` which we call from `app.py` to register our services: first the `Engine`, then `sessionmaker[Session]`, and finally `SightseeingService`.
- Then in the endpoint methods of `app.py` we create instances of `SightseeingService` by simply calling `inject.instance(SightseeingService)` — all dependencies are resolved automatically.
- As the application grows, new services and their dependencies can be added to the DI container, keeping the codebase modular and maintainable.

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
1. Clone this repository using git and switch to the branch "3_dependency_injection" or simply download this branch as a zip
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