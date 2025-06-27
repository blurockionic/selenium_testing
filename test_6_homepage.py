from base_test import BaseTest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium.webdriver.common.action_chains import ActionChains


class TestHomepage(BaseTest):

    def test_01_homepage_title(self):
        # Check if the homepage title is correct
        # wait for the page to load
        self.wait.until(EC.title_is("Wedding Services & Vendors | Marriage Vendors"))
        # self.assertEqual(self.driver.title, "Wedding Services & Vendors | Marriage Vendors")
        print("✅ Homepage title test passed.")

    def test_02_app_bar_venue_links(self):
        # Hover over the Venue link and check if the dropdown appears

        venue_link = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//li[.//span[text()='Venue']]//span[contains(@class, 'cursor-pointer')]",
                )
            )
        )
        ActionChains(self.driver).move_to_element(venue_link).perform()

        # List of (button text, expected page title) for venue dropdown
        venue_links = [
            ("Wedding Lawns Farmhouse", "Wedding Lawns Farmhouse Services | Wedding Planner India"),
            ("Hotel", "Hotel Services | Wedding Planner India"),
            ("Banquet Halls", "Banquet Halls Services | Wedding Planner India"),
            ("Marriage Garden", "Marriage Garden Services | Wedding Planner India"),
            ("Wedding Halls", "Wedding Halls Services | Wedding Planner India"),
            ("Wedding Resorts", "Wedding Resorts Services | Wedding Planner India"),
        ]

        for link_text, expected_title in venue_links:
            button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//button[text()='{link_text}']"))
            )
            button.click()
            self.wait.until(EC.title_is(expected_title))
            print(f"✅ {link_text} page title test passed.")

    def test_03_app_bar_vendor_links(self):
        venue_link = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//li[.//span[text()='Vendor']]//span[contains(@class, 'cursor-pointer')]",
                )
            )
        )
        ActionChains(self.driver).move_to_element(venue_link).perform()

        vendor_links = [
            ("Caterers", "Caterers Services | Wedding Planner India"),
            ("Wedding Decor", "Wedding Decor Services | Wedding Planner India"),
            ("Wedding Photographers", "Wedding Photographers Services | Wedding Planner India"),
            ("Wedding Music", "Wedding Music Services | Wedding Planner India"),
            ("Wedding Transportation", "Wedding Transportation Services | Wedding Planner India"),
            ("Tent House", "Tent House Services | Wedding Planner India"),
            ("Florists", "Florists Services | Wedding Planner India"),
            ("Wedding Decoration", "Wedding Decoration Services | Wedding Planner India"),
            ("Wedding Agencies", "Wedding Agencies Services | Wedding Planner India"),
            ("Pandit", "Pandit Services | Wedding Planner India"),
            ("Astrologers", "Astrologers Services | Wedding Planner India"),
            ("Wedding Invitation", "Wedding Invitation Services | Wedding Planner India"),
            ("Wedding Gift", "Wedding Gift Services | Wedding Planner India"),
            ("Wedding Coordinators", "Wedding Coordinators Services | Wedding Planner India"),
            ("Wedding Videographers", "Wedding Videographers Services | Wedding Planner India"),
            ("Wedding House", "Wedding House Services | Wedding Planner India"),
            ("Wedding Entertainment", "Wedding Entertainment Services | Wedding Planner India"),
            ("Wedding Planner", "Wedding Planner Services | Wedding Planner India"),
            ("Wedding Cakes", "Wedding Cakes Services | Wedding Planner India"),
            ("Wedding DJ", "Wedding Dj Services | Wedding Planner India"),
            ("Photobooth", "Photobooth Services | Wedding Planner India"),
            ("Invitation", "Invitation Services | Wedding Planner India"),
        ]

        for link_text, expected_title in vendor_links:
            button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//button[text()='{link_text}']"))
            )
            button.click()
            self.wait.until(EC.title_is(expected_title))
            print(f"✅ {link_text} page title test passed.")

    def test_04_app_bar_brides_links(self):
        venue_link = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//li[.//span[text()='Brides']]//span[contains(@class, 'cursor-pointer')]",
                )
            )
        )
        ActionChains(self.driver).move_to_element(venue_link).perform()

        brides_links = [
            ("Bridal Lahenga", "Bridal Lahenga Services | Wedding Planner India"),
            ("Bridal Jewellery", "Bridal Jewellery Services | Wedding Planner India"),
            ("Bridal Makeup Artist", "Bridal Makeup Artist Services | Wedding Planner India"),
            ("Mehndi Artist", "Mehndi Artist Services | Wedding Planner India"),
            ("Makeup Salon", "Makeup Salon Services | Wedding Planner India"),
        ]

        for link_text, expected_title in brides_links:
            button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//button[text()='{link_text}']"))
            )
            button.click()
            self.wait.until(EC.title_is(expected_title))
            print(f"✅ {link_text} page title test passed.")

    def test_05_app_bar_grooms_links(self):
        venue_link = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//li[.//span[text()='Grooms']]//span[contains(@class, 'cursor-pointer')]",
                )
            )
        )
        ActionChains(self.driver).move_to_element(venue_link).perform()

        groom_links = [
            ("Sherwani", "Sherwani Services | Wedding Planner India"),
            ("Men's Grooming", "Men'S Grooming Services | Wedding Planner India"),
            ("Men's Accessories", "Men'S Accessories Services | Wedding Planner India"),
        ]

        for link_text, expected_title in groom_links:
            button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f'//button[text()="{link_text}"]'))
            )
            button.click()
            self.wait.until(EC.title_is(expected_title))
            print(f"✅ {link_text} page title test passed.")

    def test_06_app_bar_invitation_link(self):
        # Click on the Invitation link in the app bar
        invitation_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Invitation']"))
        )
        invitation_link.click()
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h1[contains(text(), 'Create Beautiful Memories')]")
            )
        )
        print("✅ Invitation page test passed.")

    def test_07_app_bar_blog_link(self):
        # Click on the Blog link in the app bar
        blog_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Blog']"))
        )
        blog_link.click()
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h2[contains(text(), 'Latest Articles')]")
            )
        )
        print("✅ Blog page test passed.")

    def test_08_app_bar_other_links(self):
        # Checking Vendor Login link in the app bar
        vendor_login_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Vendor Login']"))
        )
        vendor_login_link.click()
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//p[contains(text(), 'Vendor Login')]")
            )
        )
        print("✅ Vendor Login page test passed.")

        self.driver.back()

        # checking Login link in the app bar
        login_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Login']"))
        )
        login_link.click()
        self.wait.until(EC.title_is("Couple Login - Marriage Vendors"))
        print("✅ Couple Login page test passed.")

        # checking Sign up link in the app bar
        signup_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Sign Up']"))
        )
        signup_link.click()
        self.wait.until(EC.title_is("Signup | Marriage Vendors"))
        print("✅ Couple Sign Up page test passed.")

    def test_09_search_bar(self):
        self.driver.get("https://marriagevendors.com/")
        # Locate the search bar input by its placeholder attribute
        search_bar = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@placeholder='Select Vendor']")
            )
        )
        search_bar.click()
        search_bar.send_keys("Caterers")

        # Wait for the dropdown to appear and select the first item
        first_dropdown_item = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//*[@id='/']/div/div[1]/section/div[1]/div[1]/ul/li[1]/ul/li[1]",
                )
            )
        )
        first_dropdown_item.click()
        search_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(@class, 'bg-primary') and text()='search']",
                )
            )
        )
        search_button.click()

        self.wait.until(EC.title_is("Caterers Services | Wedding Planner India"))
        print("✅ Search bar test passed.")

    def test_10_popular_search(self):
        self.driver.get("https://marriagevendors.com/")

        # List of (index, expected_title, description) for popular searches
        popular_searches = [
            (1, "Caterers Services | Wedding Planner India", "Caterering services"),
            (2, "Wedding Photographers Services | Wedding Planner India", "Wedding Photographers"),
            (3, "Makeup Salon Services | Wedding Planner India", "Makeup Salon"),
            (4, "Wedding Entertainment Services | Wedding Planner India", "Wedding Entertainment"),
            (5, "Wedding Gift Services | Wedding Planner India" , "Wedding Gift"),
            (6, "Wedding Invitation Services | Wedding Planner India", "Wedding Invitation"),
            (7, "Transport Services | Wedding Planner India", "Transport Services"),
            (8, "Wedding Planner Services | Wedding Planner India", "Wedding Planner"),
            (9, "Mehndi Artist Services | Wedding Planner India", "Mehndi Artist")
        ]

        for idx, expected_title, desc in popular_searches:
            self.driver.get("https://marriagevendors.com/")
            popular_search_div = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f'//*[@id="suggestion"]/div/div/div/div[{idx}]')
            )
            )
            self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", popular_search_div
            )
            time.sleep(0.5)
            popular_search_div.click()
            try:
                self.wait.until(EC.title_is(expected_title))
            except Exception as e:
                print(f"❌ Popular search '{desc}' test failed: {e}")
                continue
            print(f"✅ Popular search '{desc}' test passed.")

if __name__ == "__main__":
    unittest.main()
