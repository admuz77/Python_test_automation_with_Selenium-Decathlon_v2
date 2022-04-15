import unittest
from tests.sort_items_test_by_price import SortItemsTestByPrice
from tests.sort_items_by_price_revers import SortItemsTestByPriceRevers
from tests.sort_items_by_discount import SortItemsTestByDiscount
from tests.add_product_to_basket_test import AddProductsTest
from tests.delete_product_from_basket_test import DeleteProductsFromBasketTest

# Pobieram testy, które chcę uruchomić
sort_items_by_price_test = unittest.TestLoader().loadTestsFromTestCase(SortItemsTestByPrice)
sort_items_by_price_revers_test = unittest.TestLoader().loadTestsFromTestCase(SortItemsTestByPriceRevers)
sort_items_by_discount_test = unittest.TestLoader().loadTestsFromTestCase(SortItemsTestByDiscount)
add_product_to_basket_test = unittest.TestLoader().loadTestsFromTestCase(AddProductsTest)
delete_product_from_basket_test = unittest.TestLoader().loadTestsFromTestCase(DeleteProductsFromBasketTest)


# Lista testów do uruchomienia
tests_for_run = [
    sort_items_by_price_test,
    sort_items_by_price_revers_test,
    sort_items_by_discount_test,
    add_product_to_basket_test,
    delete_product_from_basket_test
]

# Stwórz Test Suitę łącząc testy
test_suite = unittest.TestSuite(tests_for_run)

# Odpal testy
unittest.TextTestRunner().run(test_suite)