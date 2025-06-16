import time
from base_test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
from utils import user_login, vendor_login
import random
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import Select


class TestVendorService(BaseTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Perform login before running the tests
        vendor_login(cls.driver, cls.wait)

    def test_1_service_page_access(self):
        # Navigate to the service page
        service_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Services"))
        )
        service_link.click()

        # Find all Elements at this xpath /html/body/div/div[1]/div/div[2]/main/div/div[1]/div[3]/div/div
        service_items = self.wait.until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    "/html/body/div/div[1]/div/div[2]/main/div/div[1]/div[3]/div/div",
                )
            )
        )

        # Verify that the service items are displayed
        self.assertTrue(len(service_items) > 0, "No service items found.")
        print("✅ Service page access test passed.")

    def test_2_add_service(self):
        # Find and click the 'Add Service' button by its title attribute
        add_service_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@title='Click to add a new service']")
            )
        )
        add_service_button.click()

        # Fill in the service form
        # Fill the 'Service Name' input
        service_name_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "service_name"))
        )
        service_name_input.send_keys("Test Service " + str(random.randint(1000, 9999)))

        # Store the service name for later verification
        service_name = service_name_input.get_attribute("value")

        # Select a value from the 'Service Category' dropdown
        service_category_select = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//label[contains(text(), 'Service Category')]/following-sibling::select",
                )
            )
        )
        select = Select(service_category_select)
        select.select_by_visible_text("Wedding Venue")

        # Select a value from the 'Service Type' dropdown (the one after Service Category)
        service_type_select = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//label[contains(text(), 'Service Type')]/following-sibling::select",
                )
            )
        )
        select_type = Select(service_type_select)
        select_type.select_by_visible_text("Wedding Lawns Farmhouse")

        # Select a value from the 'unit type' dropdown (the one after Service Type)
        unit_type_select = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//label[contains(text(), 'unit type')]/following-sibling::select",
                )
            )
        )
        select_unit = Select(unit_type_select)
        select_unit.select_by_visible_text("Per Day")

        # Fill the minimum price input
        min_price_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "min_price"))
        )
        min_price_input.send_keys("10000")

        # Select a value from the 'State' dropdown
        state_select = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//label[contains(text(), 'State')]/following-sibling::select",
                )
            )
        )
        select_state = Select(state_select)
        select_state.select_by_visible_text("Delhi")

        # Select a value from the 'City' dropdown
        city_select = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//label[contains(text(), 'City')]/following-sibling::select",
                )
            )
        )
        select_city = Select(city_select)
        # Wait for city options to be populated if needed
        self.wait.until(lambda d: len(select_city.options) > 1)
        # Select the first available city that is not the placeholder
        for option in select_city.options:
            if option.get_attribute("value"):
                select_city.select_by_visible_text(option.text)
                # print(f"✅ '{option.text}' selected in City dropdown.")
                break

        # Select the textarea for description using XPath and set value using JavaScript
        textarea = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div/div[1]/div/div[2]/main/div/div/form/div[4]/textarea",
                )
            )
        )
        self.driver.execute_script("arguments[0].focus();", textarea)
        self.driver.execute_script(
            "arguments[0].value = 'This is a test service description.';", textarea
        )

        # Submit the form
        submit_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", submit_button
        )
        # wait for button visibility
        time.sleep(0.5)
        submit_button.click()

        # After submission, check the Service Title matches the Service Name
        service_title = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//h1[contains(@class, 'text-4xl') and contains(@class, 'font-bold')]",
                )
            )
        )
        self.assertEqual(
            service_title.text.strip().lower(),
            service_name.strip().lower(),
            "Service Title does not match Service Name",
        )
        print(
            f"✅ Service Title '{service_title.text}' matches Service Name '{service_name}'"
        )

    def test_3_add_faq(self):
        # Find and click the 'Add FAQ' button by its text and class
        add_faq_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[span and contains(., 'Add FAQ') and contains(@class, 'border-blue-500')]",
                )
            )
        )
        add_faq_button.click()

        # Find and click the 'ADD' button by its text and class
        add_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[span and contains(., 'ADD') and contains(@class, 'bg-primary') and contains(@class, 'text-white')]",
                )
            )
        )
        add_button.click()

        # Fill the FAQ question input
        faq_question_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "faqs[0].question"))
        )
        faq_question_input.clear()
        faq_question_input.send_keys("What is your cancellation policy?")

        # Fill the FAQ answer textarea
        faq_answer_textarea = self.wait.until(
            EC.presence_of_element_located((By.NAME, "faqs[0].answer"))
        )
        faq_answer_textarea.clear()
        faq_answer_textarea.send_keys(
            "You can cancel up to 7 days before the event for a full refund."
        )

        # Find and click the 'SAVE' button by its text and class
        save_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[@type='submit' and contains(., 'SAVE') and contains(@class, 'text-green-500')]",
                )
            )
        )
        save_button.click()

        faq_answer = "You can cancel up to 7 days before the event for a full refund."
        faq_answer_elem = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f"//p[contains(text(), '{faq_answer}')]")
            )
        )
        self.assertIsNotNone(faq_answer_elem, "FAQ answer not found on the page.")
        print("✅ FAQ added successfully.")

    def test_4_edit_delete_faq(self):
        # Get all elements at the given FAQ Element XPath
        faq_elements = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "/html/body/div/div[1]/div/div[2]/main/div/div[5]/div")
            )
        )

        print(faq_elements)
        # Select the first FAQ item
        if not faq_elements:
            self.fail("No FAQ elements found to delete.")

        # Select the second SVG (e.g., delete icon) relative to the first FAQ
        first_faq = faq_elements[0]

        edit_icon = first_faq.find_element(By.CLASS_NAME, "text-green-500")
        edit_icon.click()
        # wait for the edit modal to appear
        question_input = self.wait.until(EC.presence_of_element_located((By.NAME, "question")))
        question_input.clear()
        question_input.send_keys("What is your updated cancellation policy?")
        answer_textarea = self.wait.until(EC.presence_of_element_located((By.NAME, "answer")))
        answer_textarea.clear()
        answer_textarea.send_keys("You can cancel up to 5 days before the event for a full refund.")

        # Find and click the 'SAVE' button by its type only
        save_button = self.wait.until(
            EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit']")
            )
        )
        # Scroll to the save button to ensure it's in view
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_button)
        # wait for button visibility
        time.sleep(0.5)
        save_button.click()

        # wait for the updated FAQ to appear
        updated_faq_answer = "You can cancel up to 5 days before the event for a full refund."
        updated_faq_answer_elem = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f"//p[contains(text(), '{updated_faq_answer}')]")
            )
        )
        self.assertIsNotNone(updated_faq_answer_elem, "Updated FAQ answer not found on the page.")
        print("✅ FAQ updated successfully.")

        # find the delete icon (SVG) within the first FAQ item using class cursor-pointer text-red-500
        # Select the SVG delete icon within the first FAQ item by its class
        delete_icon = first_faq.find_element(By.CLASS_NAME, "text-red-500")
        delete_icon.click()
        
        # check for FAQ deleted successfully. message
        success_message = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'FAQ deleted successfully.')]")
            )
        )
        # wait for item to be deleted
        print("✅ FAQ deleted successfully.")

    def test_5_delete_service(self):
        try:
            self.wait.until_not(EC.presence_of_element_located((By.CLASS_NAME, "Toastify__toast-body")))
        except Exception:
            pass  # If no toast, continue
        # Find the 'Delete' button by its text and class
        delete_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[span and contains(., 'Delete') and contains(@class, 'border-red-500') and contains(@class, 'text-red-500')]")))
        delete_button.click()

        # Wait for the Service deleted successfully. message to appear
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Service deleted successfully.')]")
            )
        )
        print("✅ Service deleted successfully.")

if __name__ == "__main__":
    unittest.main()
