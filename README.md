# Scale-It Project

Welcome to the Scale-It project! This repository contains a Python application designed to help you scale the replicas according to the Provided API emulating load.

## Table of Contents
- [Prerequisites](#pre-requisites)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Starting the App](#installation)
- [Usage](#usage)
- [Things I would do differently in a production environment](#things-i-would-do-differently-in-a-production-environment)


## Pre-requisites

- Python 3.10 or higher
- Application Provided by Vimeo to emulate load should be running 

## Project Structure

```shell
   ── app
   │   ├── core
   │   ├── tests
   │   └── utils
   └── venv
   ```


## Configuration
The following configuration parameters are configurable via environment variables : 

- `BASE_URL` (Default: "http://localhost:8123"): The base URL for the application.
- `TARGET_CPU_USAGE` (Default: 0.80): The target CPU usage threshold.
- `POLL_INTERVAL_SECONDS` (Default: 5): The polling interval in seconds.
- `RETRY_ATTEMPTS` (Default: 3): The number of retry attempts.
- `RETRY_DELAY` (Default: 1): The delay in seconds between retry attempts.

Set the .env file. Take inspiration from the .env.template file.


## Starting the App

Before you can start using Scale-It, you'll need to set up your environment. Here are the steps to get you started:

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/kshitijcode/scale-it.git
   cd scale-it
   ```
2. Changing Permissions for the script to run:

   ```shell
   chmod +x start_app.sh
   ``` 
3. Run the script to install the dependencies and start the app:

   ```shell
   ./start_app.sh
   ```
The above script also runs the unit tests and generates the html test report in the core directory.

This script runs on a Mac/Linux machine. For Windows, please run the commands manually.


## Running Unit Tests

To run the unit tests, run the following command inside the virtual environment:

```shell
   cd app
   python -m pytest tests/ --html=report.html 
  ```


## Things I would do differently in a production environment

- Add more unit tests to cover all the code paths.
- Run Linting and Static Code Analysis on the codebase as part of CI Process.
- Run the unit tests and generate the coverage report as part of CI Process.
- Run the integration tests as part of CI Process.
- I would add a CI/CD pipeline to automate the deployment process.
- Automate and Manage the secrets using a Vault/Key Store.
- Create a Dockerfile to containerize the application.
 