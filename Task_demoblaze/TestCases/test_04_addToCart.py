import time

from Task_demoblaze.Conftest.conftest import Browser
from Task_demoblaze.PageObjects.data import Data
from Task_demoblaze.PageObjects.locators import Locators
from selenium.webdriver.common.by import By
from Task_demoblaze.PageObjects.excel_function import Excel_Function
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import UnexpectedAlertPresentException

# read excel data
excel_file = Data().excel_file
sheet_num = Data().sheet_number
readData = Excel_Function(excel_file, sheet_num)
row = readData.row_count()


class TestAddToCart:
    url = Data.home_page_url
    # Browser set up
    get_driver = Browser("firefox")
    driver = get_driver.setup_browser()

    #  test setup
    def test_setup(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        # Login
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.ID, value=Locators().login_loc).click()
        self.driver.find_element(by=By.ID, value=Locators().login_username)\
            .send_keys(readData.read_file(row, 2))
        self.driver.find_element(by=By.ID, value=Locators().login_password)\
            .send_keys(readData.read_file(row, 3))
        self.driver.find_element(by=By.XPATH, value=Locators().login_btn).click()
        time.sleep(5)

    # validation of add to cart
    def test_04_addToCart(self):
        wait = WebDriverWait(self.driver, 15)
        # click on the Laptop option in categories
        try:
            self.driver.find_element(by=By.LINK_TEXT, value=Locators().laptop_loc).click()
        except StaleElementReferenceException:
            element = self.driver.find_element(by=By.LINK_TEXT, value=Locators().laptop_loc)
            wait.until(ec.element_to_be_clickable(element)).click()

        # select laptop
        element = self.driver.find_element(by=By.XPATH, value=Locators().macbook_pro)
        wait.until(ec.element_to_be_clickable(element)).click()
        try:
            self.driver.find_element(by=By.XPATH, value=Locators().add_to_cart).click()
        except UnexpectedAlertPresentException:
            self.driver.save_screenshot(Data().screenshot_path + "/cart.png")
            self.driver.switch_to.alert().accept()
        print("\nProduct added to the cart successfully")

    def test_teardown(self):
        self.driver.quit()
