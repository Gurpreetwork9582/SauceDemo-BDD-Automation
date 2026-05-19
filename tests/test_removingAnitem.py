from selenium.webdriver.common.by import By
from locators import Locators
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRemovingAnitem:
    def test_removingAnitem(self, login:WebDriver):
        wait = WebDriverWait(login, 10)
        


        cart_link = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,Locators.CART_ICON)
            )
        )
        cart_link.click()

        remove_btn = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, Locators.REMOVE_BACKPACK)
            )
        )
        remove_btn.click()


        wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, Locators.INVENTORY_ITEMS)))




        menu_btn=login.find_element(By.ID,"react-burger-menu-btn")
        menu_btn.click()
        
        inv_link = wait.until(
            EC.element_to_be_clickable((By.ID, "inventory_sidebar_link"))
        )
        inv_link.click()
        
      
        