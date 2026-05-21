from selenium.webdriver.common.by import By
from locators import Locators
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class TestCheckout:
    @pytest.mark.order(4)
    def test_checkout(self, login:WebDriver):
        wait = WebDriverWait(login, 10)
        
        # Ensure we are on the cart page
        #login.get("https://www.saucedemo.com/cart.html")
        # Going into cart
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.CART_ICON))).click()
        
        
        # Wait for checkout button to be present
        checkout=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.CHECKOUT_BTN)))
        checkout.click()
        
        # Click checkout button
        #wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.CHECKOUT_BTN))).click()
        
        firstname=wait.until(EC.element_to_be_clickable((By.ID, Locators.CHECKOUT_FIRSTNAME)))
        firstname.send_keys("Test_Firstname")
        
        lastname=wait.until(EC.element_to_be_clickable((By.ID, Locators.CHECKOUT_LASTNAME)))
        lastname.send_keys("Test_lastname")
        zip_code=wait.until(EC.element_to_be_clickable((By.ID, Locators.CHECKOUT_ZIP)))
        zip_code.send_keys("E1A353")
        
        continue_to_checkout=wait.until(EC.element_to_be_clickable((By.ID, Locators.CHECKOUT_CONTINUE)))
        continue_to_checkout.click()
        
        finish_checkout=wait.until(EC.element_to_be_clickable((By.ID, Locators.FINISH_BTN)))
        finish_checkout.click()
        
        # Wait for the confirmation message to appear
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, Locators.ORDER_CONFIRMATION), "Thank you for your order!"))
        
        # Verify the confirmation text is present
        confirmation_element = login.find_element(By.CSS_SELECTOR, Locators.ORDER_CONFIRMATION)
        assert "Thank you for your order!" in confirmation_element.text
        
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.BACK_TO_PRODUCTS))).click()

            