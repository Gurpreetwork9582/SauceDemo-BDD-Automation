from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver



class logout_auth:
    def __init__(self, browser:WebDriver):
        self.browser = browser
        
    def logout(self):
        self.browser.find_element(By.ID,"react-burger-menu-btn").click()
        self.browser.find_element(By.CSS_SELECTOR, "[data-test='logout-sidebar-link']").click()
        