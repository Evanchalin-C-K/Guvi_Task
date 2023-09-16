# Home Page Validation
from Task_demoblaze.Conftest.conftest import Browser
from Task_demoblaze.PageObjects.data import Data
from Task_demoblaze.PageObjects.locators import Locators
from selenium.webdriver.common.by import By


class TestHomePage:
    url = Data.home_page_url
    get_driver = Browser("firefox")
    driver = get_driver.setup_browser()

    def test_setup(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def test_home_page(self):
        # Home page url validation
        if self.url in self.driver.current_url:
            print("\nHome page loading")
            assert True
        # website logo
        print(self.driver.find_element(by=By.XPATH, value=Locators().logo_loc).is_displayed())
        # navigation menu
        navigation_menu = []
        nav_menu = self.driver.find_elements(by=By.XPATH, value=Locators().navigation_menu_loc)
        for menu in nav_menu:
            navigation_menu.append(menu.text)
        print("Navigation Menu : \n", navigation_menu)
        # featured products
        featured_products = []
        feature_prod = self.driver.find_elements(by=By.XPATH, value=Locators().featured_products_loc)
        for prod in feature_prod:
            featured_products.append(prod)
        print("Featured products : \n", featured_products)

    def test_teardown(self):
        self.driver.quit()

