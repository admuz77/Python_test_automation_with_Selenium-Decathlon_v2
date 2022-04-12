from pages.base_page import BasePage
from pages.locators import SearchedProductsListLocators

class AssertionTests(BasePage):
    """
    Assertions Test
    """

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
