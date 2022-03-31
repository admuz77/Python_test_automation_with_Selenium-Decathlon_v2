from pages.base_page import BasePage
from pages.locators import HomePageLocators
from pages.searched_products_list_page import SearchProductsList


class HomePage(BasePage):
    """
    Landing Page Object
    """
    # Kliknij nie dla na popupie
    def click_no_for_popup(self):
        """
        Click "no" in popup asking for permision to push notifications
        """
        el = self.driver.find_element(*HomePageLocators.NO_FOR_POPUP)
        el.click()
        pass

    # Akceptuj ciasteczka
    def accept_cookies(self):
        """
        Click button "Accept and quit" (about cookies)
        """
        el = self.driver.find_element(*HomePageLocators.ACCEPT_COOKIES)
        el.click()

    # Kliknij w pasek wyszukiwania
    def click_to_search_area(self, searched_item):
        """
        Click to the search area and search product
        """
        el = self.driver.find_element(*HomePageLocators.CLICK_SEARCH_AREA)
        # Fill this input with searched keys
        el.send_keys(searched_item)
        # input_product_name.send_keys(searched_item)
        # Nie jestem pewna czy tam powyżej po selfie robić to product name czy inaczej odnieść,
        # chodzi o to by pobrał z pliku csv dane
        pass

    # Kliknij przycisk wyszukiwania
    def click_search(self):
        """
        Click search button and returns SearchProductsList Page instance
        """
        el = self.driver.find_element(*HomePageLocators.CLICK_SEARCH_BTN)
        el.click()
        # Zwróć kolejną stronę (Searched Products List Page)
        return SearchProductsList(self.driver)


    def _verify_page(self):
        """
        Verifies Home Page
        """
        return
