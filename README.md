# Sportsify Pipeline

## Overview
The Sportsify Pipeline project is designed to create a data pipeline that fetches sports data from the Sportsify API, processes it through a neural network, and serves the predictions via a web application. This project utilizes a small 4-layer neural network to analyze sports data and provide insights.

## Project Structure
The project is organized into several directories and files:

- **src/**: Contains the main source code for the project.
  - **api/**: Handles API interactions with the Sportsify API.
    - `sportsify_client.py`: Contains the `SportsifyClient` class for fetching and parsing sports data.
  - **pipeline/**: Manages the data flow from the API to the neural network.
    - `data_pipeline.py`: Contains the `DataPipeline` class for data fetching, cleaning, and sending to the model.
  - **model/**: Implements the neural network.
    - `neural_network.py`: Contains the `NeuralNetwork` class for building, training, and predicting with the model.
  - **web/**: Sets up the web application.
    - `app.py`: Contains the Flask application for serving predictions.
  - **utils/**: Provides utility functions for data processing and evaluation.
    - `helpers.py`: Contains helper functions like `calculate_accuracy` and `log_results`.

- **tests/**: Contains unit tests for the project components.
  - `test_api.py`: Tests for the `SportsifyClient` class.
  - `test_pipeline.py`: Tests for the `DataPipeline` class.
  - `test_model.py`: Tests for the `NeuralNetwork` class.
  - `test_web.py`: Tests for the Flask application.

- **.github/**: Contains CI/CD configuration.
  - **workflows/**: Defines the CI/CD pipeline using GitHub Actions.
    - `ci-cd.yml`: Automates testing and deployment.

- **requirements.txt**: Lists the dependencies required for the project.

- **.gitignore**: Specifies files and directories to be ignored by Git.

## Setup Instructions
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/sportsify-pipeline.git
   cd sportsify-pipeline
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Implement the classes and methods as described in the respective files.
2. Write unit tests in the `tests` directory to ensure functionality.
3. Configure the CI/CD pipeline in `.github/workflows/ci-cd.yml` to automate testing and deployment.
4. Deploy the application to `coryrove.com/marchmadness` following the deployment steps outlined in this README.

## Contribution Guidelines
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch and create a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.