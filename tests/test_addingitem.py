from selenium.webdriver.common.by import By


class TestAddingitem:
    def test_addingitem(self, browser):
        browser.find_element(By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]').click()
        browser.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()
        item_name = browser.find_element(By.CLASS_NAME, "inventory_item_name").text
        assert item_name == "Sauce Labs Backpack"
        browser.find_element(By.ID, "react-burger-menu-btn").click()
        browser.find_element(By.ID, "inventory_sidebar_link").click()
  
