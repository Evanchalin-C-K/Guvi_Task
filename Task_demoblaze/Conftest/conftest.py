from selenium import webdriver
from selenium.common.exceptions import WebDriverException
# Firefox
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
# Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# Edge
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service


class Browser:
    def __init__(self, browser_name):
        self.browser_name = browser_name

    def setup_browser(self):
        # Firefox
        if self.browser_name == "firefox":
            try:
                driver = webdriver.Firefox()
            except WebDriverException:
                driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
            return driver

        # Chrome
        elif self.browser_name == "chrome":
            try:
                driver = webdriver.Chrome()
            except WebDriverException:
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            return driver

        # Edge
        elif self.browser_name == "edge":
            try:
                driver = webdriver.Edge()
            except WebDriverException:
                driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
            return driver

        else:
            print("Invalid Browser Name")