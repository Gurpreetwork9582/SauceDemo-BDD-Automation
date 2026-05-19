from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestAddingMultipleitem:
    def test_adding_multiple_item(self, login:WebDriver):
        wait = WebDriverWait(login, 10)

        menu_btn=login.find_element(By.CSS_SELECTOR, Locators.MENU_HAMBURGER_BTN)
        menu_btn.click()

        All_items=wait.until(
            EC.element_to_be_selected(
                (By.CSS_SELECTOR, Locators.MENU_ALL_ITEMS)
                )
            )
        All_items.click()