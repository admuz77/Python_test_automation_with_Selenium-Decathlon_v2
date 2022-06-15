from tests.base_test import BaseTest
from time import sleep
from tests.test_data import TestData
from tests.assertion_tests import AssertionTests

# TC-1
class SortItemsTestByPrice(BaseTest):
    """
    Sort items by price Test
    """
    def test_sort_by_price(self):
        home_page = self.home_page

        # # 1. Kliknięcie "nie" w popupie dotyczącym przesyłania powiadomień - wcześniej popup był, teraz go nie ma
        # home_page.click_no_for_popup()
        # sleep(5)

        # 2. Akceptacja ciasteczek
        home_page.accept_cookies()
        sleep(5)

        # 3. Kliknięcie w pole wyszukiwania i wpisanie nazwy produktu
        home_page.click_to_search_area(TestData.searched_item)
        sleep(3)

        # 4. Kliknięcie przycisku wyszuiwania
        search_product_list = home_page.click_search()
        sleep(3)

        # 5. Naciśnięcie opcji wyboru rodzaju produtu
        type_of_product_option = search_product_list.type_of_product_btn()
        sleep(3)

        # 6. Wybór rodzaju produktu
        product_type = search_product_list.choose_type_of_product()
        sleep(3)

        # 7. Zapisanie wyboru rodzaju produktu
        save_selection = search_product_list.save_selection()

        # 8. Naciśnięcie opcji sortowania według kryteriów
        sort_list_btn = search_product_list.sort_list_btn()
        sleep(3)

        # 9. Wybór sortowania według ceny
        sorting_by_price = search_product_list.sorting_by_price()
        sleep(3)

        # 10. Pobranie cen produktów oraz sprawdzenie, czy ceny są właściwie posortowane
        prices_comparison = AssertionTests.prices_comparison(self)








