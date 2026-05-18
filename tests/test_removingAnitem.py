from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRemovingAnitem:
    def test_removingAnitem(self, login):
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

        remove_btn = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[data-test="remove-sauce-labs-backpack"]')
            )
        )
        remove_btn.click()

        wait.until(
            EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, '[data-test="remove-sauce-labs-backpack"]')
            )
        )

        cart_items = login.find_elements(By.CSS_SELECTOR, ".cart_item")
        assert len(cart_items) == 0
