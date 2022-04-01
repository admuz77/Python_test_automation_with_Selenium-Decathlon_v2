import random

class TestData():
    """
    List of searched products
    """
    products = open("products.csv").readlines()
    searched_item = (products[random.randrange(len(products))])