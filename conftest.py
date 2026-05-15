from selenium import webdriver
import pytest

@pytest.fixture
def browser_open():
    browser = webdriver.Chrome()
    browser.get("https://www.selenium.dev/selenium/web/web-form.html")
    yield browser
    browser.quit()
