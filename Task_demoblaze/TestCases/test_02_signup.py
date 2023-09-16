# Sign up Validation
import time

from selenium.common.exceptions import UnexpectedAlertPresentException
from Task_demoblaze.Conftest.conftest import Browser
from Task_demoblaze.PageObjects.data import Data
from Task_demoblaze.PageObjects.locators import Locators
from Task_demoblaze.PageObjects.excel_function import Excel_Function
from selenium.webdriver.common.by import By

# Read excel data
excel_file = Data().excel_file
sheet_num = Data().sheet_number
readData = Excel_Function(excel_file, sheet_num)
row = readData.row_count()


class TestSignUp:
    url = Data().home_page_url
    get_driver = Browser("firefox")
    driver = get_driver.setup_browser()

    # Setup
    def test_setup(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    # Sign up
    def test_sign_up(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.XPATH, value=Locators().sign_up).click()
        # Username
        user_name = self.driver.find_element(by=By.XPATH, value=Locators().username_loc)
        user_name.send_keys(readData.read_file(row, 2))
        # Password
        password = self.driver.find_element(by=By.XPATH, value=Locators().password_loc)
        password.send_keys(readData.read_file(row, 3))
        # SignUp Button
        sign_up_btn = self.driver.find_element(by=By.XPATH, value=Locators().sign_up_btn_loc)
        try:
            sign_up_btn.click()
        except UnexpectedAlertPresentException:
            self.driver.save_screenshot(Data().screenshot_path + "/sign_up_success.png")
            self.driver.switch_to.alert().accept()
        print("Sign up : Success")

    def test_teardown(self):
        self.driver.quit()
