from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import pytest


class TestAddingMultipleitem:
    @pytest.mark.order(3)
    def test_adding_multiple_item(self, login:WebDriver):
        wait = WebDriverWait(login, 10)
        '''
        menu_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.MENU_HAMBURGER_BTN))
        )
        login.execute_script("arguments[0].click();", menu_btn)

        self.All_items = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.MENU_ALL_ITEMS))
        )
        self.All_items.click()
        '''    
        # Wait until inventory page is loaded and first add button is visible
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, Locators.ADD_BIKE_LIGHT)))

        # Add items with explicit waits
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.ADD_BIKE_LIGHT))).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.ADD_TSHIRT))).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.ADD_ONESIE))).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.ADD_RED_TSHIRT))).click()
    
        
        # Going into cart
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.CART_ICON))).click()
        
        Inventory_item = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, Locators.INVENTORY_ITEMS)))
        no_of_inventory = len(Inventory_item)
        assert no_of_inventory > 0
        
        
        
        