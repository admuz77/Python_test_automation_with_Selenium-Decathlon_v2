from pages.base_page import BasePage
from pages.locators import SearchedProductsListLocators
from pages.product_page import ProductPage
from pages.basket_page import BasketPage

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

    def discounts_comparison(self):
        discounts = self.driver.find_elements(*SearchedProductsListLocators.DISCOUNTS)
        get_discounts = [discount.get_attribute("innerText") for discount in discounts]
        print(get_discounts)
        x = ' '.join(get_discounts)

        throw_away = ["−", "%"]
        for i in x:
            if i in throw_away:
                x = x.replace(i,"")
        new_discounts_list = x.split()
        print(list(new_discounts_list))
        discounts_int = map(int, new_discounts_list)
        discounts_list = list(discounts_int)
        for value in discounts_list:
            print("wysokość rabatu: ", value)

        reversed_discounts_list = list(discounts_list)
        (reversed_discounts_list.sort())
        (reversed_discounts_list.reverse())
        for reversed_discounts_value in reversed_discounts_list:
            print("Rabat po weryfikacji sortowania to", reversed_discounts_value)

        assert discounts_list == reversed_discounts_list



    def item_name_assertion(self):
        # pobranie nazwy przedmiotu z momentu dodawania do koszyka (pobranie nazwy z pliku item_added_to_basket_at_product_page_data.txt)
        file = open('item_added_to_basket_at_product_page_data.txt')
        first_name = file.read()
        print(f'asercja:', first_name)

        # pobranie nazwy przedmiotu z koszyka
        file2 = open('item_in_basket_data.txt')
        second_name = file2.read()
        # second_name = BasketPage.get_name_of_the_product_in_the_basket(self)
        print(f'asercja2:', second_name)

        # porównanie nazw przedmiowów

        assert first_name == second_name

        file.close()
        file2.close()


        # wyczyszczenie pliku item_added_to_basket_at_product_page_data.txt
