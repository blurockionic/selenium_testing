from base_test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestInvalidLogin(BaseTest):
    def test_invalid_login(self):
        driver = self.driver
        wait = self.wait

        # Click login buttom in the home page
        login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_link.click()

        # Fill invalid credentials
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        email_input.send_keys("invalid@example.com")
        password_input.send_keys("wrongpassword")

        # Click on the login button
        login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Login')]")))
        login_btn.click()

        # Wait for error alert and assert the message
        try:
            error_alert = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Invalid email or password')]")))
            self.assertIn("Invalid email or password", error_alert.text)
        except Exception as e:
            print("\nDEBUG: Page source after failed login:\n")
            self.fail("Expected error alert not found or message mismatch. Check debug output above.")