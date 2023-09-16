import time

from Task_demoblaze.Conftest.conftest import Browser
from Task_demoblaze.PageObjects.data import Data
from Task_demoblaze.PageObjects.locators import Locators
from selenium.webdriver.common.by import By
from Task_demoblaze.PageObjects.excel_function import Excel_Function


excel_file = Data().excel_file
sheet_num = Data().sheet_number
readData = Excel_Function(excel_file, sheet_num)
row = readData.row_count()


class TestCartPurchase:
    url = Data.home_page_url
    # Browser set up
    get_driver = Browser("firefox")
    driver = get_driver.setup_browser()

    #  test setup
    def test_setup(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

        # Login
        self.driver.implicitly_wait(15)
        self.driver.find_element(by=By.ID, value=Locators().login_loc).click()
        self.driver.find_element(by=By.ID, value=Locators().login_username)\
            .send_keys(readData.read_file(row, 2))
        self.driver.find_element(by=By.ID, value=Locators().login_password)\
            .send_keys(readData.read_file(row, 3))
        self.driver.find_element(by=By.XPATH, value=Locators().login_btn).click()
        time.sleep(5)

    # Placing order in the cart page
    def test_05_cartPurchase(self):
        self.driver.implicitly_wait(10)
        # click on the cart menu

        self.driver.find_element(by=By.CSS_SELECTOR, value=Locators().cart_loc).click()
        # click on the place order button
        self.driver.find_element(by=By.XPATH, value=Locators().place_order).click()
        # Fill the required shipping details
        # Name
        self.driver.find_element(by=By.XPATH, value=Locators().name_loc)\
            .send_keys(readData.read_file(row, 4))
        # Country
        self.driver.find_element(by=By.XPATH, value=Locators().country_loc)\
            .send_keys(readData.read_file(row, 5))
        # City
        self.driver.find_element(by=By.XPATH, value=Locators().city_loc)\
            .send_keys(readData.read_file(row, 6))
        # Credit card number
        self.driver.find_element(by=By.XPATH, value=Locators().credit_card_loc) \
            .send_keys(readData.read_file(row, 7))
        # month
        self.driver.find_element(by=By.XPATH, value=Locators().month_loc)\
            .send_keys(readData.read_file(row, 8))
        # Year
        self.driver.find_element(by=By.XPATH, value=Locators().year_loc)\
            .send_keys(readData.read_file(row, 9))
        # click on purchase button
        self.driver.find_element(by=By.XPATH, value=Locators().purchase_loc).click()
        time.sleep(5)
        # Screenshot for successful purchase of item
        self.driver.save_screenshot(Data().screenshot_path + "/purchase_success.png")
        self.driver.find_element(by=By.XPATH, value=Locators().ok_btn).click()
        print("\nOrder placed successfully")

    def test_teardown(self):
        self.driver.quit()