import time

from Task_demoblaze.Conftest.conftest import Browser
from Task_demoblaze.PageObjects.data import Data
from Task_demoblaze.PageObjects.locators import Locators
from selenium.webdriver.common.by import By
from Task_demoblaze.PageObjects.excel_function import Excel_Function


# read excel data
excel_file = Data().excel_file
sheet_num = Data().sheet_number
readData = Excel_Function(excel_file, sheet_num)
row = readData.row_count()


class TestLogin:
    url = Data.home_page_url
    # Browser set up
    get_driver = Browser("firefox")
    driver = get_driver.setup_browser()

    #  test setup
    def test_setup(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    # Login
    def test_03_login(self):
        self.driver.implicitly_wait(10)
        # Login
        self.driver.find_element(by=By.ID, value=Locators().login_loc).click()
        # Login username
        self.driver.find_element(by=By.ID, value=Locators().login_username)\
            .send_keys(readData.read_file(row, 2))
        # Login password
        self.driver.find_element(by=By.ID, value=Locators().login_password)\
            .send_keys(readData.read_file(row, 3))
        # Login Button
        self.driver.find_element(by=By.XPATH, value=Locators().login_btn).click()
        time.sleep(5)
        self.driver.save_screenshot(Data().screenshot_path + "/login_success.png")
        print("\nLogin with valid credential : Success ")

    def test_teardown(self):
        self.driver.quit()
