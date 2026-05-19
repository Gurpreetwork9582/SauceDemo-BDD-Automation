from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRemovingAnitem:
    def test_removingAnitem(self, login:WebDriver):
        wait = WebDriverWait(login, 10)
        
        '''
        add_btn = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')
            )
        )
        add_btn.click()
        '''

        cart_link = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
            )
        )
        cart_link.click()

        remove_btn = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[data-test="remove-sauce-labs-backpack"]')
            )
        )
        remove_btn.click()


        wait.until(
            lambda driver:
            len(driver.find_elements(By.CSS_SELECTOR, ".cart_item")) == 0
            )

        cart_items = login.find_elements(
            By.CSS_SELECTOR, ".cart_item"
            )

        assert len(cart_items) == 0


        menu_btn=login.find_element(By.ID,"react-burger-menu-btn")
        menu_btn.click()
        
        inv_link = wait.until(
            EC.element_to_be_clickable((By.ID, "inventory_sidebar_link"))
        )
        inv_link.click()
        
        
        add_btn = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')
            )
        )
        assert "Add to cart" in add_btn
        