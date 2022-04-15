from pages.base_page import BasePage
from pages.locators import ProductPageLocators



class ProductPage(BasePage):
    """
    Product Page
    """
    def get_name_of_the_product(self):
        gnotp = self.driver.find_element(*ProductPageLocators.GET_NAME_OF_THE_ITEM)
        product_name =gnotp.get_attribute("innerText")
        print(f'Produkt dodany do koszyka to:', product_name)
        # Zapisanie nazwy produktu do pliku
        file = open("item_added_to_basket_at_product_page_data.txt", "w")
        file.write(product_name)
        file.close()

    def add_product_to_basket(self):
        aptb = self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET)
        aptb.click()

    def go_to_basket(self):
        gtb = self.driver.find_element(*ProductPageLocators.GO_TO_BASKET)
        gtb.click()