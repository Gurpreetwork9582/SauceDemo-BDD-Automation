from selenium.webdriver.common.by import By


class TestRemovingAnitem:
    def test_removingAnitem(self, browser):
        browser.find_element(By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]').click()
        browser.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()
        browser.find_element(By.CSS_SELECTOR, '[data-test="remove-sauce-labs-backpack"]').click()
        assert not browser.find_elements(By.CSS_SELECTOR, ".cart_item")
        browser.find_element(By.ID, "react-burger-menu-btn").click()
        browser.find_element(By.ID, "inventory_sidebar_link").click()
  
