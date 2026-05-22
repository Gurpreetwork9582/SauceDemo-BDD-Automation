# SauceDemo BDD Automation

This project is a Selenium automation suite for [SauceDemo](https://www.saucedemo.com/). I built it to practice end-to-end UI testing with two styles:

- Pytest + Selenium tests from the `tests/` folder
<img width="1470" height="636" alt="Pytest report" src="https://github.com/user-attachments/assets/c6217565-fa10-4d83-b8f6-29c01bab185e" />

- Behave BDD scenarios from the `features/` folder
<img width="1170" height="176" alt="Behave" src="https://github.com/user-attachments/assets/ea069297-acb6-4ebc-8970-b45eacf0dd91" />


The tests cover common SauceDemo user flows such as logging in, adding products to the cart, removing an item, adding multiple items, and completing checkout.

## Tech Stack

- Python 3
- Selenium WebDriver
- Pytest
- Pytest HTML reports
- Pytest Order
- Behave BDD
- Chrome / ChromeDriver

## Project Structure

```text
.
├── features/
│   ├── checkout.feature
│   ├── environment.py
│   └── steps/
│       └── checkout_steps.py
├── locators/
│   └── Locators.py
├── tests/
│   ├── test_addingitem.py
│   ├── test_addingmultipleitem.py
│   ├── test_removingAnitem.py
│   └── test_Checkout.py
├── conftest.py
├── Login_auth.py
├── Logout_auth.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## What This Project Does

The Pytest suite runs browser automation against SauceDemo and validates:

- Login using the standard SauceDemo user
- Adding one product to the cart
- Removing a product from the cart
- Adding multiple products
- Completing checkout and verifying the order confirmation message

The Behave BDD suite describes the checkout journey in Gherkin:

```gherkin
Feature: Checkout
  Scenario: Complete checkout with items in the cart
```

## Setup

Clone the repository:

```bash
git clone <your-repo-url>
cd SauceDemo-BDD-Automation
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Make sure Google Chrome is installed. Selenium Manager should handle ChromeDriver automatically for modern Selenium versions.

## Run Pytest + Selenium Tests

To run the Pytest Selenium suite, use:

```bash
python3 -m pytest
```

Pytest will read `pytest.ini`, collect the tests from the `tests/` folder, and run files named `test_*.py`.

The project also generates an HTML report:

```text
report.html
```

Open `report.html` in a browser after the run to view the test report.

## Run Behave BDD Tests

To run the Behave BDD suite, use:

```bash
behave
```

Behave automatically looks inside the `features/` folder, runs the `.feature` files, and maps each Gherkin step to Python step definitions inside `features/steps/`.

You can also run the checkout feature directly:

```bash
behave features/checkout.feature
```

## Important Files

`locators/Locators.py` contains the shared SauceDemo locators used by the tests.

`conftest.py` contains Pytest fixtures for opening Chrome and logging in.

`Login_auth.py` handles SauceDemo login helper logic.

`features/environment.py` creates and closes the browser for Behave scenarios.

`features/steps/checkout_steps.py` contains the Selenium step definitions for the BDD checkout scenario.

`pytest.ini` stores Pytest configuration, including test discovery and report settings.

## Test Data

The project uses the public SauceDemo test credentials:

```text
Username: standard_user
Password: secret_sauce
```

Checkout form data used in the test:

```text
First name: Test_Firstname
Last name: Test_lastname
Postal code: E1A353
```

## Notes

- Run commands from the project root directory.
- If `python3 -m pytest` cannot find Selenium, activate your virtual environment first.
- If `behave` is not found, install the dependencies again with `python3 -m pip install -r requirements.txt`.
- Browser tests require an internet connection because they run against `https://www.saucedemo.com/`.
- `cookies.pkl`, `report.html`, and screenshots are generated runtime artifacts and may change after test runs.

## Example Commands

```bash
# Activate virtual environment
source venv/bin/activate

# Run all Pytest Selenium tests
python3 -m pytest

# Run Behave BDD tests
behave

# Run only the checkout BDD feature
behave features/checkout.feature
```
