from tests.base_test import BaseTest
from time import sleep
from tests.test_data import TestData
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from tests.assertion_tests import AssertionTests

# TC-4
class AddProductsTest(BaseTest):
    """
    Checkt product name added to basket
    """
    def test_add_product_the_basket(self):
        home_page = self.home_page

        # # 1. Kliknięcie "nie" w popupie dotyczącym przesyłania powiadomień - wcześniej popup był, teraz go nie ma
        # home_page.click_no_for_popup()
        # sleep(5)

        # 2. Akceptacja ciasteczek
        home_page.accept_cookies()
        sleep(3)

        # 3. Kliknięcie w pole wyszukiwania i wpisanie nazwy produktu
        home_page.click_to_search_area(TestData.searched_item)
        sleep(3)

        # 4. Kliknięcie wyszukiwania
        search_product_list = home_page.click_search()
        sleep(3)

        # 5. Wybranie pierwszego przedmiotu z wyświetlonej listy wyszukanych przedmiotów
        first_item_click = search_product_list.click_first_item()
        sleep(3)

        # 6. Pobranie nazwy przedmiotu do zmiennej
        product_name = ProductPage.get_name_of_the_product(self)
        sleep(3)

        # 7. Dodanie przedmiotu do koszyka
        add_product = ProductPage.add_product_to_basket(self)
        sleep(3)

        # 8. Wejście do koszyka
        go_to_basket = ProductPage.go_to_basket(self)
        sleep(5)

        # 9. Sprawdzenie jaki przedmiot znajduje się w koszyku
        what_is_in_the_basket = BasketPage.get_name_of_the_product_in_the_basket(self)
        sleep(3)

        # 10. Porównanie czy przedmiot dodany do koszyka oraz ten znajdujący się w nim to te same przedmioty
        items_name_comparison = AssertionTests.item_name_assertion(self)