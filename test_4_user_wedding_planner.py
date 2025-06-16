import time
from base_test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
from utils import user_login
import random
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime, timedelta


class TestUserWeddingPlanner(BaseTest):
    created_event = None  # Class variable to store the created event

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Perform login before running the tests
        user_login(cls.driver, cls.wait, "armanmarya6@gmail.com", "Arman2005@")

    def test_1_wedding_planner_page_access(self):
        try:
            self.wait.until_not(
                EC.presence_of_element_located((By.CLASS_NAME, "Toastify__toast-body"))
            )
        except Exception:
            pass  # If no toast, continue

        # Navigate to the checklist page
        profile_icon = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//img[@alt='Profile']"))
        )
        profile_icon = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//img[@alt='Profile']"))
        )
        profile_icon.click()

        wedding_planner_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Wedding Planner"))
        )
        wedding_planner_link.click()

        # Verify that the wedding planner page is loaded
        # Check for "From Wishes to Reality!" this text to ensure the page is loaded
        page_element = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'From Wishes to Reality!')]")
            )
        )
        self.assertEqual(
            page_element.text,
            "From Wishes to Reality!",
            "Wedding Planner page did not load correctly.",
        )
        print("✅ Wedding Planner page access test passed.")

    def test_2_event_items_displayed(self):
        # Check if the wedding planner items are displayed
        event_container = self.wait.until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    '//*[@id="root"]/div[2]/div/div/div[2]/div/section/div[1]/section',
                )
            )
        )

        self.assertGreater(len(event_container), 0, "No event items found.")
        print("✅ Event items display test passed.")

    def test_3_create_event(self):
        # Find the Event button and click it
        event_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[p[text()='Event']]"))
        )
        event_button.click()

        # Wait for the modal to appear and be visible
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="root"]/div[2]/div/div/div[2]/div/div[3]')
            )
        )
        # Fill in the event details
        event_name_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "eventName"))
        )
        random_event_name = f"Test Event {random.randint(1000, 9999)}"
        event_name_input.send_keys(random_event_name)

        # Fill in the event budget
        event_budget_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "eventBudget"))
        )
        event_budget_input.send_keys(str(random.randint(1000, 10000)))

        # Fill in the event date
        event_date_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "eventDate"))
        )
        # Set a valid date (e.g., tomorrow) in mm/dd/yyyy format
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%m/%d/%Y")
        event_date_input.send_keys(tomorrow)

        # Fill in the event start time
        event_start_time_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "startTime"))
        )
        # Set a valid start time (e.g., 12:00)
        event_start_time_input.send_keys("14:00")

        # Fill in the event end time
        event_end_time_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "endTime"))
        )
        # Set a valid end time (e.g., 14:00)
        event_end_time_input.send_keys("16:00")

        # Fill in the event description
        event_description_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "eventDescription"))
        )
        event_description_input.send_keys("This is a test event description.")

        # Submit the event form (click the "Create Event" button)
        create_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Create Event')]")
            )
        )
        create_button.click()

        # Wait for the modal to close
        self.wait.until(
            EC.invisibility_of_element_located(
                (By.XPATH, '//*[@id="root"]/div[2]/div/div/div[2]/div/div[3]')
            )
        )

        # Check for the event name in the event list
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f"//*[contains(text(), '{random_event_name}')]")
            )
        )
        print("✅ Event creation test passed.")

    

    def test_4_remove_event(self):
        # Find the Event Container
        events = self.wait.until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    '//*[@id="root"]/div[2]/div/div/div[2]/div/section/div[1]/section/div',
                    # //*[@id="root"]/div[2]/div/div/div[2]/div/section/div[1]/section/div[2]
                )
            )
        )

        if not events:
            self.fail("No events found to remove.")

        # Use the last event for removal
        last_event = events[-1]
        print("XPath of last event:", last_event.get_attribute("xpath") if last_event.get_attribute("xpath") else "XPath not available")

        # Get the XPath of the last event and concatenate with the relative path to the toggle button
        last_event_index = len(events)
        last_event_xpath = f'//*[@id="root"]/div[2]/div/div/div[2]/div/section/div[1]/section/div[{last_event_index}]'
        toggle_button_xpath = last_event_xpath + "/div/div[2]/div[3]/button"
        toggle_button = self.wait.until(
            EC.element_to_be_clickable(
            (By.XPATH, toggle_button_xpath)
            )
        )
        # print("HTML of toggle button:", toggle_button.get_attribute("outerHTML"))
        # Scroll into view and try JS click if normal click fails
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", toggle_button)
        time.sleep(0.2)
        # wait for the toggle button to be visible
        self.wait.until(EC.visibility_of(toggle_button))
        
        toggle_button.click()
        
        # Wait for the delete button to appear of xpath //*[@id="root"]/div[2]/div/div/div[2]/div/section/div[1]/section/div[14]/div[1]/div[2]/div[3]/div/button[1]
        delete_button_xpath = last_event_xpath + "/div/div[2]/div[3]/div/button[1]"
        delete_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, delete_button_xpath))
        )
        delete_button.click()

        # Wait for the event to be removed from the list
        self.wait.until(
            EC.staleness_of(last_event)
        )
        print("✅ Event removal test passed.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
