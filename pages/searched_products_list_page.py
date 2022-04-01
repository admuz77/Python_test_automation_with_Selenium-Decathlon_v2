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
    # Wybór sortowania według ceny
    def sorting_by_price(self):
        sbp = self.driver.find_element(*SearchedProductsListLocators.SORTING_BY_PRICE)
        sbp.click()

    def prices_comparison(self):
        # Tworzę listę z cenami, która uwzględnia ceny promocyjne, konieczna jest zmiana pobranej ceny na float,
        # bo inaczej jest stringiem
        prices = self.driver.find_elements(*SearchedProductsListLocators.PRICES)
        get_prices = [price.get_attribute("data-price") for price in prices]
        prices_float = map(float, get_prices)
        prices_list = list(prices_float)
        for value in prices_list:
            print("Cena produktu: ", value)

        # Tworzę duplikat listy z cenami, aby go uporządkować od najmniejszej wartości do największej, a potem je porównać.

        verifity_prices_list = list(prices_list)
        for verifity_value in verifity_prices_list:
            print("Cena porównawcza produktu to ", verifity_value)

        (verifity_prices_list.sort())
        assert prices_list == verifity_prices_list

    def _verify_page(self):
        """
        Verifity Searched Products Page
        """
        return

