import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class BaseTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        # options.add_argument("--headless")  # Uncomment for headless tests
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.marriagevendors.com/")

    def tearDown(self):
        self.driver.quit()
