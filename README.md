# DemoQA Automation Project
This project contains automated tests for the DemoQA website using Python, Selenium WebDriver, and Behave (Cucumber for Python).

## Setup
1. Install Python 3.x from https://www.python.org/downloads/
2. Install required packages:
   pip install selenium behave webdriver-manager allure-behave pytest
3. Install Allure command-line tool:
- For Windows: `scoop install allure`
- For macOS: `brew install allure`

## Running Tests
To run all tests:
behave features/demoqa.feature


To generate Allure reports:
   allure generate allure-results -o allure-report --clean
   allure open allure-report

## Module Explanations
### 1. demoqa.feature
  Scenario: Create user, generate token, and rent books
    Given I create a new user
    When I generate a token for the user
    Then I confirm the user is authorized
    And I list available books
    And I rent two random books
    Then I verify the user details with rented books

### 2. demoqa_steps.py
The demoqa_steps.py file is part of a Cucumber test automation framework. Here's a simplified explanation of what it does:
It defines three main steps for a test scenario:
"Given" step: Given I create a new user.
"When" step: I generate a token for the user.
"Then" step: I verify the user details with rented books.

### 3. api_client.py
The api_client.py file defines a simple APIClient class that provides a convenient way to make HTTP requests to an API. 

### 4. base_page.py
The base_page.py file defines a BasePage class that provides a foundation for implementing the Page Object Model in Selenium test automation. Here's a simplified explanation of what it does:
1- It imports necessary Selenium WebDriver components for wait conditions and expected conditions.
2- The BasePage class is initialized with a WebDriver instance.
3- It provides four main methods:
wait_for_element(): Waits for an element to be present on the page.
click(): Waits for an element to be clickable and then clicks it.
input_text(): Waits for an element, clears its content, and enters new text.
get_text(): Waits for an element and retrieves its text content.
These methods encapsulate common Selenium WebDriver operations with built-in waits, making it easier to interact with web elements across different pages in a more reliable way. This class serves as a base for creating specific page object classes, promoting code reuse and maintainability in test automation projects.

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
├── requirements.txt
├── pytest.ini
├── environment.py
├── behave.ini
└── README.md