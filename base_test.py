import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load environment variables
        load_dotenv()
        
        # Get configuration from environment variables
        headless = os.getenv('HEADLESS', 'false').lower() == 'true'
        wait_time = int(os.getenv('EXPLICIT_WAIT', '15'))
        base_url = os.getenv('BASE_URL', 'https://www.marriagevendors.com/')
        
        options = Options()
        if headless:
            options.add_argument("--headless")
            
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, wait_time)
        cls.driver.get(base_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
