from base_test import BaseTest
from utils import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# No access to login page after login
class TestAuthorization(BaseTest):
    def test_authorization_required(self):
        driver = self.driver
        wait = self.wait

        # Login first
        login(driver, wait, "armanmarya6@gmail.com", "Arman2005@")

        # Try to access the login page after login
        self.driver.get("https://www.marriagevendors.com/login")
        # Wait for the page to load
        wait.until(EC.title_is("Wedding Services & Vendors | Marriage Vendors"))
        self.assertEqual(driver.title, "Wedding Services & Vendors | Marriage Vendors")
        print("✅ Login page title is correct after login attempt.")
