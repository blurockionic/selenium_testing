import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_test_credentials():
    """
    Get test credentials from environment variables
    """
    return {
        'user_email': os.getenv('TEST_USER_EMAIL'),
        'user_password': os.getenv('TEST_USER_PASSWORD'),
        'vendor_email': os.getenv('TEST_VENDOR_EMAIL'),
        'vendor_password': os.getenv('TEST_VENDOR_PASSWORD')
    }

def user_login(driver, wait, email=None, password=None):
    """
    Perform login using the provided driver, wait, email, and password.
    If email/password not provided, uses environment variables.
    """
    if not email or not password:
        credentials = get_test_credentials()
        email = credentials['user_email']
        password = credentials['user_password']
    
    # Click login link
    login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
    login_link.click()

    # Fill credentials
    email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    email_input.send_keys(email)
    password_input.send_keys(password)

    # Submit
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    submit_button.click()

    # Wait for "Login successful" message to appear and disappear
    success_msg = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Login successful')]")))
    wait.until(EC.invisibility_of_element(success_msg))

def vendor_login(driver, wait, email=None, password=None):
    """
    Perform vendor login using environment variables or provided credentials.
    Raises ValueError if vendor credentials are not provided and not set in environment.
    """
    if not email or not password:
        credentials = get_test_credentials()
        email = credentials['vendor_email']
        password = credentials['vendor_password']
        
        # Check if vendor credentials are actually set
        if not email or not password:
            raise ValueError(
                "Vendor credentials not found. Please set TEST_VENDOR_EMAIL and TEST_VENDOR_PASSWORD "
                "in your .env file or pass email and password parameters directly."
            )
    
    # Click login button in the home page
    vendor_login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Vendor Login")))
    vendor_login_link.click()
    email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    email_input.send_keys(email)
    password_input.send_keys(password)

    # Submit
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    submit_button.click()
    wait.until(EC.title_is("Wedding | Vendor Dashbaord"))




def close_modal_if_present(driver, wait):
    """
    Closes a modal if it appears by clicking the close button (X) with aria-label 'Close'.
    """
    try:
        close_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Close']"))
        )
        close_btn.click()
        print("Modal closed.")
    except Exception:
        # Modal did not appear, or already closed
        pass
