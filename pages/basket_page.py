from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    """
    Basket Page
    """
    def get_name_of_the_product_in_the_basket(self):
        gnotpitb = self.driver.find_element(*BasketPageLocators.NAME_OF_THE_PRODUCT)
        product_name = gnotpitb.get_attribute("innerText")
        print(f'Produkt w koszyku to:', product_name)
        file = open("item_in_basket_data.txt", "w")
        file.write(product_name)
        file.close()

    def remove_product_from_the_basket(self):
        rpftb = self.driver.find_element(*BasketPageLocators.REMOVE_PRODUCT_FROM_BASKET)
        rpftb.click()


