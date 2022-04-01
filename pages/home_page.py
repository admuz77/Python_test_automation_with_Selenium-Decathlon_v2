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
        Click "no" in popup asking for permission to push notifications
        """
        cnfp = self.driver.find_element(*HomePageLocators.NO_FOR_POPUP)
        cnfp.click()
        pass

    # Akceptuj ciasteczka
    def accept_cookies(self):
        """
        Click button "Accept and quit" (about cookies)
        """
        ac = self.driver.find_element(*HomePageLocators.ACCEPT_COOKIES)
        ac.click()

    # Kliknij w pasek wyszukiwania
    def click_to_search_area(self, searched_item):
        """
        Click to the search area and search product
        """
        ctsa = self.driver.find_element(*HomePageLocators.CLICK_SEARCH_AREA)
        # Fill this input with searched keys
        ctsa.send_keys(searched_item)
        print(f'Poszukiwany przedmiot to',searched_item)
        pass

    # Kliknij przycisk wyszukiwania
    def click_search(self):
        """
        Click search button and returns SearchProductsList Page instance
        """
        cs = self.driver.find_element(*HomePageLocators.CLICK_SEARCH_BTN)
        cs.click()
        # Zwróć kolejną stronę (Searched Products List Page)
        return SearchProductsList(self.driver)


    def _verify_page(self):
        """
        Verifies Home Page
        """
        return
