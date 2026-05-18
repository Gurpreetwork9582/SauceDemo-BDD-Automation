from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAddingitem:
    def test_addingitem(self, login):
        wait = WebDriverWait(login, 10)

        add_btn = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')
            )
        )
        add_btn.click()

        cart_link = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
            )
        )
        cart_link.click()

        item_name = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
        ).text
        assert item_name == "Sauce Labs Backpack"

        menu_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
        )
        menu_btn.click()

        inv_link = wait.until(
            EC.element_to_be_clickable((By.ID, "inventory_sidebar_link"))
        )
        inv_link.click()