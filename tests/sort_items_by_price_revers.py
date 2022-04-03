from tests.base_test import BaseTest
from time import sleep
from tests.test_data import TestData
from pages.home_page import HomePage
from pages.searched_products_list_page import SearchProductsList
# from pages.searched_products_list_page import PricesComparison

class SortItemsTestByPriceRevers(BaseTest):
    """
    Sort Items Test. Sorting by price from the most expensive to the cheapest.
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

        # 4. Kliknięcie przycisku wyszuiwania
        search_product_list = home_page.click_search()

        # 5. Naciśnięcie opcji wyboru rodzaju produtu
        type_of_product_option = search_product_list.type_of_product_btn()

        # 6. Wybór rodzaju produktu
        product_type = search_product_list.choose_type_of_product()

        # 7. Zapisanie wyboru rodzaju produktu
        save_selection = search_product_list.save_selection()

        # 8. Naciśnięcie opcji sortowania według kryteriów
        sort_list_btn = search_product_list.sort_list_btn()

        # 9. Wybór sortowania według ceny
        sorting_by_price = search_product_list.sorting_by_price_reverse()

        sleep(5)

        # 10. Pobranie cen produktów oraz sprawdzenie, czy są właściwie posortowane
        prices_comparison = search_product_list.prices_comparison_reverse()



