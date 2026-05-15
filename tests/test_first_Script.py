from selenium.webdriver.common.by import By
from selenium import webdriver

def test_title(browser_open):
    title = browser_open.title
    assert "Web form" in title

    browser_open.implicitly_wait(0.5)

    text_box = browser_open.find_element(by=By.NAME, value="my-text")
    submit_button = browser_open.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    submit_button.click()

    

