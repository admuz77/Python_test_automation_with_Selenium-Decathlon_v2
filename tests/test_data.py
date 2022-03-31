import random

class TestData():
    products = open("products.csv").readlines()
    searched_item = (products[random.randrange(len(products))])