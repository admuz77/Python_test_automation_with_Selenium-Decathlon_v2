from selenium.webdriver.common.by import By

class HomePageLocators():
    """
    Locators used on Home Page
    """

    NO_FOR_POPUP = (By.XPATH, "//button[@class='wp-no']")
    ACCEPT_COOKIES = (By.XPATH, "//button[@id='didomi-notice-agree-button']")
    CLICK_SEARCH_AREA = (By.XPATH, "//input[@type='search']")
    CLICK_SEARCH_BTN = (By.XPATH, "//button[@tabindex='1']")



class SearchedProductsListLocators():
    """
    Locators used on Searched Products List Page
    """

    TYPE_OF_PRODUCTS_BTN = (By.XPATH, "//*[@id='start-of-listing']/div[2]/button/span[1]")
    CHOOSE_TYPE_OF_PRODUCT = (By.XPATH, "//*[@id='option-0']")
    SAVE_SELECTION_ABOUT_TYPE_OF_PRODUCT = (By.XPATH, "//*[@id='start-of-listing']/div[2]/div/div")
    SORT_LIST_BTN = (By.XPATH, "//*[@id='start-of-listing']/div[1]")
    SORTING_BY_PRICE = (By.XPATH, "//*[@id='option-sort-1']/span")
    SORTING_BY_PRICE_REVERSE = (By.XPATH, "//*[@id='option-sort-2']/span")
    PRICES = (By.XPATH, "//*[@data-price]")
    SORTING_BY_DISCOUNT = (By.XPATH, "//*[@id='option-sort-3']/span")
    DISCOUNTS = (By.XPATH, "//span[@class='prc__rate']")
    # FIRST_ITEM = (By.XPATH, "//div[@class='prc__cartridge']")
    FIRST_ITEM =(By.XPATH, "//div[2]/div//strong")



class ProductPageLocators():
    """
    Locators used at Product Cart
    """
    GET_NAME_OF_THE_ITEM = (By.XPATH, "//h1")
    ADD_TO_BASKET = (By.XPATH, "//*[@id='fitAnalytics-pdp-add-to-cart']")
    GO_TO_BASKET = (By.XPATH, "//span[. = 'Koszyk']")

class BasketPageLocators():
    """
    Locators used at Bascet Page
    """

    NAME_OF_THE_PRODUCT = (By.CSS_SELECTOR, "a[class^='product-name']")
    REMOVE_PRODUCT_FROM_BASKET = (By.CSS_SELECTOR, "button[aria-label='Remove product in cart page']")
    EMPTY_BASKET_STATEMENT = (By.XPATH, "//h2[contains(text(),'Twój koszyk jest pusty.')]")

