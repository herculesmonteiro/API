# DemoQA Automation Project
This project contains automated tests for the DemoQA website using Python, Selenium WebDriver, and Behave (Cucumber for Python).

## Setup
1. Install Python 3.x from https://www.python.org/downloads/
2. Install required packages:
    pip install selenium behave webdriver-manager allure-behave
    pip install selenium behave webdriver-manager allure-behave pytest
3. Install Allure command-line tool:
- For Windows: `scoop install allure`
- For macOS: `brew install allure`

## Running Tests
To run all tests:
behave

To generate Allure reports:
   allure generate allure-results -o allure-report --clean
   allure open allure-report

## Module Explanations
  Scenario: Create user, generate token, and rent books
    Given I create a new user
    When I generate a token for the user
    Then I confirm the user is authorized
    And I list available books
    And I rent two random books
    Then I verify the user details with rented books

## Project Structure
project/
│
├── features/
│ ├── steps/
│ │ └── demoqa_steps.py
│ └── demoqa.feature
│
├── pages/
│ ├── base_page.py
│
├── utils/
│ └── api_client.py
│
├── data/
│ └── form_data.txt
│
├── requirements.txt
├── pytest.ini
├── environment.py
├── behave.ini
└── README.md