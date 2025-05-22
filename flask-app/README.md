# Flask App

This is a simple Flask application structured using Blueprints for modularity. 

## Project Structure

```
flask-app
├── app
│   ├── __init__.py
│   ├── main
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── templates
│   │       └── main
│   │           └── index.html
│   └── templates
├── run.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd flask-app
   ```
3. Create a virtual environment:
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
5. Install the required packages:
   ```
   pip install Flask
   ```

## Running the Application

To run the application, execute the following command:
```
python run.py
```

The application will be accessible at `http://127.0.0.1:5000/`.

## Features

- Modular structure using Blueprints.
- Simple route that renders an HTML template.

## License

This project is licensed under the MIT License.