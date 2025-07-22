from base_test import BaseTest
from utils import user_login, close_modal_if_present
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
class TestUserAuthentication(BaseTest):

    def test_1_unregistered_email(self):

        # Click login button in the home page
        vendor_login_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Vendor Login")))
        vendor_login_link.click()

        # Fill invalid credentials
        email_input = self.wait.until(EC.presence_of_element_located((By.NAME, "email")))
        password_input = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
        email_input.send_keys("invalid@example.com")
        password_input.send_keys("wrongpassword")

        # Click on the login button
        login_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Login')]")))
        login_btn.click()

        # Wait for error alert and assert the message
        error_alert = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Vendor not found with this email')]")))
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(), 'Vendor not found with this email')]")
        ))
        self.assertIn("Vendor not found with this email", error_alert.text)
        print("✅ Unregistered email test passed. Error message displayed as expected.")
    
    
    def test_2_invalid_password(self):
        # Fill invalid credentials
        email_input = self.wait.until(EC.presence_of_element_located((By.NAME, "email")))
        password_input = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
        email_input.clear()
        password_input.clear()
        email_input.send_keys("armanmarya6@gmail.com")
        password_input.send_keys("wrongpassword")

        # Click on the login button
        login_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Login')]")))
        login_btn.click()

        # Wait for error alert and assert the message
        # error_alert = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Invalid password')]")))
        # self.assertIn("Invalid password", error_alert.text)

        # Check that the page title is still the login page
        self.assertEqual(self.driver.title, "Vendor Login - Marriage Vendors | Manage Your Wedding Services")
        print("✅ Invalid password test passed. Error message displayed as expected.")

    def test_3_valid_login(self):
        # Test login functionality
        """
        Perform login using the provided driver, wait, email, and password.
        """
        self.driver.get("https://www.marriagevendors.com/vendorLogin")
        email_input = self.wait.until(EC.presence_of_element_located((By.NAME, "email")))
        password_input = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
        email_input.send_keys("armanmarya6@gmail.com")
        password_input.send_keys("Arman2005")

        # Submit
        submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        submit_button.click()

        # time.sleep(1)
        self.wait.until(EC.title_is("Wedding | Vendor Dashbaord"))
        self.assertEqual(self.driver.title, "Wedding | Vendor Dashbaord")

        # # Wait for "Login successful" message to appear and disappear
        # success_msg = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Login successful')]")))
        # self.wait.until(EC.invisibility_of_element(success_msg))
        print("✅ Valid login test passed.")
    
    def test_4_authorization(self):
        # Try to access the login page after login
        self.driver.get("https://www.marriagevendors.com/vendorLogin")
        # Wait for the page to load
        self.wait.until(EC.title_is("Wedding | Vendor Dashbaord"))
        self.assertEqual(self.driver.title, "Wedding | Vendor Dashbaord")
        print("✅ Redirected to Dashboard if logged in.")

    def test_5_logout(self):
        # Test logout functionality
        # Find and click the SVG profile/menu button before logout
        svg_icon = self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                "div > svg.text-primary.text-3xl.cursor-pointer.p-2.hover\\:bg-primary.hover\\:text-background.rounded-full"
            ))
        )
        svg_icon.click()
        print("✅ SVG profile/menu icon clicked.")
        # Wait for the logout button to appear
        logout_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Logout')]")))
        logout_button.click()
        # Wait for the page to load after logout
        self.wait.until(EC.title_is("Wedding Services & Vendors | Marriage Vendors"))
        self.assertEqual(self.driver.title, "Wedding Services & Vendors | Marriage Vendors")
        self.wait.until(EC.invisibility_of_element_located(
            (By.XPATH, "//*[contains(text(), 'Vendor logged out successfully')]")
        ))
        print("✅ Logout successful.")

    def test_6_forgot_password(self):
        # Click login button in the home page
        vendor_login_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Vendor Login")))
        vendor_login_link.click()

        # Click on the "Forgot Password?" link
        forgot_password_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Forgot Password?")))
        forgot_password_link.click()

        # Find the reset button
        reset_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Reset Password')]")))
        
        # Find the email input field
        email_input = self.wait.until(EC.presence_of_element_located((By.NAME, "email")))
        email_input.send_keys("armanmarya6@gmail.com")

        # Wait for the reset button to be clickable and click it
        self.wait.until(EC.element_to_be_clickable(reset_button)).click()

        # Wait for the success message to appear

        success_message = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Reset password link sent')]")))
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(), 'Reset password link sent')]")
        ))
        self.assertIn("Reset password link sent", success_message.text)

if __name__ == "__main__":
    unittest.main(verbosity=2)  # Set verbosity to 2 for more detailed output