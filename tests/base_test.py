from pages.home_page import HomePage
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """

    def setUp(self):
        self.options = Options()
        self.options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.maximize_window()
        self.driver.get("https://www.decathlon.pl/")
        self.home_page = HomePage(self.driver)
        self.driver.implicitly_wait(5)


    def tearDown(self):
        self.driver.quit()

