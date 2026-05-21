from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import pickle


class login_auth:
    def __init__(self, browser:WebDriver):
        self.browser = browser

    def login(self):
        self.browser.get("https://www.saucedemo.com/")
        if "inventory.html" in self.browser.current_url:
            return
        self.browser.find_element(By.CSS_SELECTOR, "[data-test='username']").send_keys("standard_user")
        self.browser.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("secret_sauce")
        self.browser.find_element(By.CSS_SELECTOR, "[data-test='login-button']").click()

    def save_cookie(self):
        with open("cookies.pkl","wb") as file:
            pickle.dump(self.browser.get_cookies(), file)

    def load_cookie(self):
        self.browser.get("https://www.saucedemo.com/")
        with open("cookies.pkl","rb") as file:
            cookies = pickle.load(file)

        for cookie in cookies:
            self.browser.add_cookie(cookie)

        self.browser.refresh()