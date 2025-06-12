from base_test import BaseTest
from utils import login
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest


class TestLogin(BaseTest):
    def test_valid_login(self):
        driver = self.driver
        wait = self.wait

        # Use the login utility function
        login(driver, wait, "armanmarya6@gmail.com", "Arman2005@")
        print("✅ Valid login test passed.")
        # Check for profile image
        profile_icon = wait.until(EC.presence_of_element_located((By.XPATH, "//img[@alt='Profile']")))
        self.assertIsNotNone(profile_icon)

        # Wait for the profile icon to be clickable before clicking
        profile_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Profile']")))
        profile_icon.click()
        # time.sleep(5)  # Wait for profile page to load

        # Wait for logout button to appear
        logout_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Logout')]")))

        # Scroll logout button into view and click with JS
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", logout_button)
        driver.execute_script("arguments[0].click();", logout_button)

        # Confirm logout by waiting for login link to reappear
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
        print("✅ Logout successful.")


if __name__ == "__main__":
    unittest.main()
