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


class TestLogout:
    url = Data.home_page_url
    # Browser setup
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

    # Logout validation
    def test_06_logout(self):
        self.driver.find_element(by=By.LINK_TEXT, value=Locators().logout_btn).click()
        if self.url in self.driver.current_url:
            assert True
            print("\nLogout : Redirected to Home Page Successfully")

    def test_teardown(self):
        self.driver.quit()
