from locators  import Inventory
class InventoryPage:
    def __init__(self,browser):
        self.browser=browser
        

    def get_all_item_names(self):
        items = self.browser.find_elements(Inventory.ITEM_NAME)
        for i in items:
            return i.text
 