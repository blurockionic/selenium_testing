from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def user_login(driver, wait, email, password):
    """
    Perform login using the provided driver, wait, email, and password.
    """
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

def vendor_login(driver, wait):
    # Click login button in the home page
    vendor_login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Vendor Login")))
    vendor_login_link.click()
    email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    email_input.send_keys("armanmarya6@gmail.com")
    password_input.send_keys("Arman2005")


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
