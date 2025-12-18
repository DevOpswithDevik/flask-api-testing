![Build Status](https://github.com/DevOpswithDevik/flask-api-testing/actions/workflows/python-app.yml/badge.svg)

🚀 Flask API Automated Integration Testing
This project demonstrates a fully automated CI/CD pipeline that deploys a Python Flask API and executes integration tests using Postman and Newman.

🛠️ Project Components

API: Python Flask application (api.py).
Testing: Postman Collection (integration-tests.json).
Automation: GitHub Actions Workflow (python-app.yml).
Test Runner: Newman (Postman CLI).

🛑 Challenges & Problem Solving
During development, we encountered and resolved several critical technical hurdles:

1. YAML Syntax Errors (Services vs. Steps)
The Problem: We initially tried to run the API as a "Service," which led to persistent Unexpected value 'command' errors because of strict indentation rules in the YAML file.

The Solution: We moved the API startup to a standard workflow step. By using python api.py & (the & runs it in the background), we avoided the finicky service-level formatting entirely.

2. "Request URL is Empty" Error
The Problem: The tests failed on GitHub because the exported Postman collection didn't know where the server was located.

The Solution: We replaced hardcoded URLs in Postman with the variable {{baseURL}}. We then injected the local address (http://127.0.0.1:5000) during the CI run using Newman's --global-var flag.

3. Collection Export Issues
The Problem: The collection had a double file extension (.json.json) and the POST request was incorrectly configured as a GET request.

The Solution: We renamed the file for clarity, updated the HTTP methods in Postman, and performed a clean export using the Collection v2.1 format.

📊 CI/CD Workflow Summary
The GitHub Actions pipeline follows these steps:

Environment Setup: Installs Python 3.9 and Node.js 20.
Dependency Management: Installs Flask and Newman CLI.
Deployment: Launches the API in the background with a sleep 5 command to allow the server time to boot up.
Test Execution: Runs Newman against the live local endpoint.
Reporting: Displays a pass/fail summary table directly in the GitHub Actions console.

🏁 How to Run Locally

Install requirements: pip install Flask
Start the API: python api.py
Run tests: newman run integration-tests.json --global-var "baseURL=http://127.0.0.1:5000"