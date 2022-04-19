from tests.base_test import BaseTest
from time import sleep
from tests.test_data import TestData
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from tests.assertion_tests import AssertionTests



class DeleteProductsFromBasketTest(BaseTest):
    """
    Delete one product from the basket. From that moment basket should be empty.
    """
    def test_delete_product_from_basket(self):
        home_page = self.home_page

        # # 1. Kliknięcie "nie" w popupie dotyczącym przesyłania powiadomień - wcześniej popup był, teraz go nie ma
        # home_page.click_no_for_popup()
        # sleep(5)

        # 2. Akceptacja ciasteczek
        home_page.accept_cookies()
        sleep(5)

        # 3. Kliknięcie w pole wyszukiwania i wpisanie nazwy produktu
        home_page.click_to_search_area(TestData.searched_item)

        # 4. Kliknięcie wyszukiwania
        search_product_list = home_page.click_search()

        # 5. Wybranie pierwszego przedmiotu z wyświetlonej listy wyszukanych przedmiotów
        first_item_click = search_product_list.click_first_item()

        # 6. Dodanie przedmiotu do koszyka
        add_product = ProductPage.add_product_to_basket(self)

        # 7. Wejście do koszyka
        go_to_basket = ProductPage.go_to_basket(self)

        # 8. Sprawdzenie jaki przedmiot znajduje się w koszyku
        what_is_in_the_basket = BasketPage.get_name_of_the_product_in_the_basket(self)

        # 9. Usunięcie przedmiotu z koszyka
        remove_product_from_the_basket = BasketPage.remove_product_from_the_basket(self)

        # 10. Sprawdzenie czy koszyk jest pusty
        empty_basket_assertion = AssertionTests.empty_basket_assertion(self)