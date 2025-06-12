import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        # options.add_argument("--headless")  # Uncomment this to run without opening browser window
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 15)
        cls.driver.get("https://www.marriagevendors.com/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
