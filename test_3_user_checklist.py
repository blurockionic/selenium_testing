import time
from base_test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
from utils import login
import random
from selenium.webdriver.common.action_chains import ActionChains

class TestUserChecklist(BaseTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Perform login before running the tests
        login(cls.driver, cls.wait, "armanmarya6@gmail.com", "Arman2005@")

    def test_1_checklist_page_access(self):
        # Wait for any toast notifications to disappear
        try:
            self.wait.until_not(EC.presence_of_element_located((By.CLASS_NAME, "Toastify__toast-body")))
        except Exception:
            pass  # If no toast, continue

        # Navigate to the checklist page
        profile_icon = self.wait.until(EC.presence_of_element_located((By.XPATH, "//img[@alt='Profile']")))
        profile_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Profile']")))
        profile_icon.click()

        checklist_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Checklist")))
        checklist_link.click()

        # Verify that the checklist page is loaded
        self.wait.until(EC.title_is("Checklist - Book an Appointment"))
        self.assertEqual(self.driver.title, "Checklist - Book an Appointment")
        print("✅ Checklist page access test passed.")

    def test_2_checklist_items_displayed(self):
        # Check if checklist items are displayed
        checklist_items = self.wait.until(
            EC.presence_of_all_elements_located(
            (By.XPATH, '//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/div[2]/div')
            )
        )
        self.assertGreater(len(checklist_items), 0, "No checklist items found.")
        print("✅ Checklist items are displayed as expected.")

    def test_3_checklist_item_interaction(self):
        # Interact with the first checklist item
        checklist_items = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/div[2]/div')
            )
        )
        # Find the first <li> element inside the first checklist item
        first_item = checklist_items[0]
        all_li = first_item.find_elements(By.XPATH, ".//ul/li")

        if not all_li:
            self.fail("No <li> elements found inside the first checklist item.")

        current_li_span = all_li[0].find_element(By.XPATH, ".//div/span")
        classes = current_li_span.get_attribute("class").split()

        if "line-through" in classes:
            print("Item is already marked as completed. Unchecking...")
            all_li[0].click()
            # After unchecking, verify it is not completed
            current_li_span = all_li[0].find_element(By.XPATH, ".//div/span")
            classes = current_li_span.get_attribute("class").split()
            self.assertNotIn("line-through", classes, "Checklist item should not be marked as completed after unchecking.")
            print("Checklist item was completed, now unchecked.")
            # Now check it again
            all_li[0].click()
            current_li_span = all_li[0].find_element(By.XPATH, ".//div/span")
            classes = current_li_span.get_attribute("class").split()
            self.assertIn("line-through", classes, "Checklist item not marked as completed after re-checking.")
            print("✅ Checklist item re-checked and marked as completed.")
        else:
            print("Item is not completed. Checking...")
            all_li[0].click()
            # After clicking, check again
            current_li_span = all_li[0].find_element(By.XPATH, ".//div/span")
            classes = current_li_span.get_attribute("class").split()
            self.assertIn("line-through", classes, "Checklist item not marked as completed after click.")
            print("✅ Checklist item was not completed, now marked as completed after click.")

    def test_4_add_item_to_checklist(self):
        # Click on the "Add Item" button
        # Interact with the first checklist item
        checklist_items = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/div[2]/div')
            )
        )
        # Find the first <li> element inside the first checklist item
        first_item = checklist_items[0]
        all_li = first_item.find_elements(By.XPATH, ".//ul/li")

        if not all_li:
            self.fail("No <li> elements found inside the first checklist item.")

        # Click the input to focus (if needed)
        item_name_input = first_item.find_element(By.XPATH, ".//input[@name='item']")
        unique_item_name = f"Test Checklist Item {random.randint(1000, 9999)}"
        item_name_input.clear()
        item_name_input.send_keys(unique_item_name)
        # Optionally, press Enter to submit if that's how the UI works
        item_name_input.send_keys(u'\ue007')  # u'\ue007' is the Enter key in Selenium
        
        # Wait for the new item to appear in the checklist
        new_item = self.wait.until(
            EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{unique_item_name}')]"))
        )

        self.assertIsNotNone(new_item, "New checklist item was not added successfully.")
        print("✅ New checklist item added successfully.")

    def test_5_remove_item_from_checklist(self):
        # Interact with the first checklist item
        checklist_items = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/div[2]/div')
            )
        )
        # Find the first <li> element inside the first checklist item
        first_item = checklist_items[0]
        all_li = first_item.find_elements(By.XPATH, ".//ul/li")

        if not all_li:
            self.fail("No <li> elements found inside the first checklist item.")

        # Use the last li for removal
        last_li = all_li[-1]
        item_text = last_li.text

        # Move to the last checklist item to trigger hover (make remove button visible)
        ActionChains(self.driver).move_to_element(last_li).perform()
        time.sleep(0.5)  # Give time for the button to become visible

        # Find the remove button (SVG) after hover
        actions_div = last_li.find_element(By.XPATH, ".//div[contains(@class, 'flex') and contains(@class, 'justify-end')]")
        svgs = actions_div.find_elements(By.TAG_NAME, "svg")
        if len(svgs) < 2:
            self.fail("Remove button SVG not found in checklist item.")
        remove_button = svgs[1]
        remove_button.click()

        # Wait for the item to be removed
        self.wait.until(EC.staleness_of(last_li))
        print("✅ Checklist item removed successfully.")

    def test_6_add_new_category(self):
        # Fill in the category name
        category_name_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='category']"))
        )
        unique_category_name = f"Test Category {random.randint(1000, 9999)}"
        category_name_input.clear()
        category_name_input.send_keys(unique_category_name)

        category_name_input.send_keys(u'\ue007')  # u'\ue007' is the Enter key in Selenium

        # Verify that the new category is added
        new_category = self.wait.until(
            EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{unique_category_name}')]"))
        )
        self.assertIsNotNone(new_category, "New category was not added successfully.")
        print("✅ New category added successfully.")

    def test_7_remove_category(self):
        checklist_items = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/div[2]/div')
            )
        )
        last_category_item = checklist_items[-1]  # Use the last item for removal
        # Hover to make the remove button visible
        ActionChains(self.driver).move_to_element(last_category_item).perform()
        time.sleep(0.5)  # Give time for the button to become visible
        remove_button = last_category_item.find_element(By.TAG_NAME, "svg")
        if not remove_button:
            self.fail("Remove button SVG not found in checklist item.")
        remove_button.click()
        # Wait for the category to be removed
        self.wait.until(EC.staleness_of(last_category_item))
        print("✅ Checklist category removed successfully.")



if __name__ == "__main__":
    unittest.main(verbosity=2)