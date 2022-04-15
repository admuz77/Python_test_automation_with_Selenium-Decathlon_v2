import random

class TestData():
    """
    List of searched products
    """
    products = open("searched_products_data.csv").readlines()
    searched_item = (products[random.randrange(len(products))])