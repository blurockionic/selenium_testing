from base_test import BaseTest
from utils import login
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
class TestUserAuthentication(BaseTest):

    def test_invalid_login(self):
        # Click login button in the home page
        login_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_link.click()

        # Fill invalid credentials
        email_input = self.wait.until(EC.presence_of_element_located((By.NAME, "email")))
        password_input = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
        email_input.send_keys("invalid@example.com")
        password_input.send_keys("wrongpassword")

        # Click on the login button
        login_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Login')]")))
        login_btn.click()

        # Wait for error alert and assert the message
        try:
            error_alert = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Invalid email or password')]")))
            self.assertIn("Invalid email or password", error_alert.text)
        except Exception as e:
            print("\nDEBUG: Page source after failed login:\n")
            self.fail("Expected error alert not found or message mismatch. Check debug output above.")

    def test_valid_login(self):
        # Test login functionality
        """
        Perform login using the provided driver, wait, email, and password.
        """

        # Fill credentials
        email_input = self.wait.until(EC.presence_of_element_located((By.NAME, "email")))
        password_input = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
        email_input.clear()
        password_input.clear()
        email_input.send_keys("armanmarya6@gmail.com")
        password_input.send_keys("Arman2005@")

        # Submit
        submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        submit_button.click()

        # Wait for "Login successful" message to appear and disappear
        success_msg = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Login successful')]")))
        self.wait.until(EC.invisibility_of_element(success_msg))
        print("✅ Valid login test passed.")

    def test_logout(self):
        # Test logout functionality
        profile_icon = self.wait.until(EC.presence_of_element_located((By.XPATH, "//img[@alt='Profile']")))
        self.assertIsNotNone(profile_icon)

        # Wait for the profile icon to be clickable before clicking
        profile_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Profile']")))
        profile_icon.click()
        # time.sleep(5)  # Wait for profile page to load

        # Wait for logout button to appear
        logout_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Logout')]")))

        # Scroll logout button into view and click with JS
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", logout_button)
        self.driver.execute_script("arguments[0].click();", logout_button)

        # Confirm logout by waiting for login link to reappear
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
        print("✅ Logout successful.")

    def test_registration(self):
        # Test registration functionality
        pass


if __name__ == "__main__":
    unittest.main()