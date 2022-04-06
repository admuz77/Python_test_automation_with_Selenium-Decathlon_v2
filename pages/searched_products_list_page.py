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

    def prices_comparison(self):
        # Tworzę listę z cenami, która uwzględnia ceny promocyjne, konieczna jest zmiana pobranej ceny na float,
        # bo inaczej jest stringiem
        prices = self.driver.find_elements(*SearchedProductsListLocators.PRICES)
        get_prices = [price.get_attribute("data-price") for price in prices]
        prices_float = map(float, get_prices)
        prices_list = list(prices_float)
        for value in prices_list:
            print("Cena produktu sortowanego na stronie to", value)

        # Tworzę duplikat listy z cenami, aby go uporządkować od najmniejszej wartości do największej, a potem je porównać.

        verifity_prices_list = list(prices_list)
        (verifity_prices_list.sort())
        for verifity_value in verifity_prices_list:
            print("Cena produktu po weryfikacji sortowania to", verifity_value)


        assert prices_list == verifity_prices_list


    def prices_comparison_reverse(self):
        # Tworzę listę z cenami, która uwzględnia ceny promocyjne
        prices = self.driver.find_elements(*SearchedProductsListLocators.PRICES)
        get_prices = [price.get_attribute("data-price") for price in prices]
        prices_float = map(float, get_prices)
        prices_list = list(prices_float)
        for value in prices_list:
            print("Cena produktu sortowanego na stronie to", value)

        # Tworzę duplikat listy z cenami, aby go uporządkować od najmniejszej wartości do największej, następnie odwracam kolejność,
        # a potem je porównuję z cenami pobranmi ze strony.

        reversed_prices_list = list(prices_list)
        (reversed_prices_list.sort())
        (reversed_prices_list.reverse())
        for reversed_value in reversed_prices_list:
            print("Cena produktu po weryfikacji sortowania to", reversed_value)


        assert prices_list == reversed_prices_list


    def sorting_by_discount(self):
        sbd = self.driver.find_element(*SearchedProductsListLocators.SORTING_BY_DISCOUNT)
        sbd.click()

    def discounts_comparison(self):
        discounts = self.driver.find_elements(*SearchedProductsListLocators.DISCOUNTS)
        get_discounts = [discounts.get_attribute('prc__rate') for discount in discounts]
        discounts_float = map(float, get_discounts)
        discounts_list = list(discounts_float)
        for value in discounts_list:
            print("wysokość rabatu: ", value)


    def _verify_page(self):
        """
        Verifity Searched Products Page
        """
        return

