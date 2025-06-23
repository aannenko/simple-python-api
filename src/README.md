# Stage 1: Flask
This is the initial stage of development, it focuses on building a minimal [Flask Web API](https://flask.palletsprojects.com/en/stable/quickstart/). The goal here is to keep the codebase simple and highlight the basics of Flask.

## Project Structure
- `app.py`: Main entry point for the Flask application.
- `Models/`: Contains data models (e.g., `sightseeing.py`, `sightseeing_page.py`).
- `Services/`: Contains service logic (e.g., `sightseeing_service.py`).
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
- Clone this repository using git and switch to the branch "1_flask" or simply download this branch as a zip
- Open `src/` folder in Visual Studio Code
- In VSCode press `Ctrl+Shift+P` and select:
    1. "Python: Create Environment..."
    2. "Venv"
    3. Your Python installation
    4. Check "requirements.txt" and click "OK" button

At this point you should have `.venv` created and dependencies from `requirements.txt` installed.

#### Run the application
In VSCode, press F5 to run the application.<br/>
Open the file `app.http` and try sending requests from it to your app.