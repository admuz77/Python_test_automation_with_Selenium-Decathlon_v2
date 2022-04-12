from pages.base_page import BasePage
from pages.locators import SearchedProductsListLocators

class SearchProductsList(BasePage):
    """
    Page with results of searching from HomePage
    """
    # Naciśnięcie opcji wyboru rodzaju produtu
    def type_of_product_btn(self):
        topb = self.driver.find_element(*SearchedProductsListLocators.TYPE_OF_PRODUCTS_BTN)
        topb.click()
    # Wybór rodzaju produktu
    def choose_type_of_product(self):
        ctop = self.driver.find_element(*SearchedProductsListLocators.CHOOSE_TYPE_OF_PRODUCT)
        ctop.click()
    # Zapisanie wyboru rodzaju produktu
    def save_selection(self):
        ss = self.driver.find_element(*SearchedProductsListLocators.SAVE_SELECTION_ABOUT_TYPE_OF_PRODUCT)
        ss.click()
    # Naciśnięcie opcji sortowania według kryteriów
    def sort_list_btn(self):
        slb = self.driver.find_element(*SearchedProductsListLocators.SORT_LIST_BTN)
        slb.click()
    # Wybór sortowania według ceny od najtańszej do najdroższej
    def sorting_by_price(self):
        sbp = self.driver.find_element(*SearchedProductsListLocators.SORTING_BY_PRICE)
        sbp.click()

    # Wybór sortowania według ceny od najdroższej do najtańszej
    def sorting_by_price_reverse(self):
        sbp = self.driver.find_element(*SearchedProductsListLocators.SORTING_BY_PRICE_REVERSE)
        sbp.click()


    def sorting_by_discount(self):
        sbd = self.driver.find_element(*SearchedProductsListLocators.SORTING_BY_DISCOUNT)
        sbd.click()




    def _verify_page(self):
        """
        Verifity Searched Products Page
        """
        return

