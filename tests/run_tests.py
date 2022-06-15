import unittest
from tests.sort_items_test_by_price import SortItemsTestByPrice
from tests.sort_items_by_price_revers import SortItemsTestByPriceRevers
from tests.sort_items_by_discount import SortItemsTestByDiscount
from tests.add_product_to_basket_test import AddProductsTest
from tests.delete_product_from_basket_test import DeleteProductsFromBasketTest

# Pobieram testy, które chcę uruchomić
test_sort_by_price = unittest.TestLoader().loadTestsFromTestCase(SortItemsTestByPrice)
test_sort_by_price_reverse = unittest.TestLoader().loadTestsFromTestCase(SortItemsTestByPriceRevers)
test_sort_by_discount = unittest.TestLoader().loadTestsFromTestCase(SortItemsTestByDiscount)
test_add_product_the_basket = unittest.TestLoader().loadTestsFromTestCase(AddProductsTest)
test_delete_product_from_basket = unittest.TestLoader().loadTestsFromTestCase(DeleteProductsFromBasketTest)


# Lista testów do uruchomienia
tests_for_run = [
    test_sort_by_price,
    test_sort_by_price_reverse,
    test_sort_by_discount,
    test_add_product_the_basket,
    test_delete_product_from_basket
]

# Stwórz Test Suitę łącząc testy
test_suite = unittest.TestSuite(tests_for_run)

# Odpal testy
unittest.TextTestRunner().run(test_suite)