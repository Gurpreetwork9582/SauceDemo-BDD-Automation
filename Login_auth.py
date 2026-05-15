from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle


class login_auth(): 
    def login(self):
        self.browser = webdriver.Chrome()
        self.browser.get("https://www.saucedemo.com/")
        self.browser.find_element(By.CSS_SELECTOR, "[data-test=\"username\"]").click()
        self.browser.find_element(By.CSS_SELECTOR, "[data-test=\"username\"]").send_keys("standard_user")
        self.browser.find_element(By.CSS_SELECTOR, "[data-test=\"password\"]").click()
        self.browser.find_element(By.CSS_SELECTOR, "[data-test=\"password\"]").send_keys("secret_sauce")
        self.browser.find_element(By.CSS_SELECTOR, "[data-test=\"login-button\"]").click()

    def save_cookie(self):
        with open("cookies.pkl","wb") as file:
            pickle.dump(self.browser.get_cookies(), file)

    def load_cookie(self):
        with open("cookies.pkl","rb") as file:
            cookies=pickle.load(file)

        for cookie in cookies:
            self.browser.add_cookie(cookie)