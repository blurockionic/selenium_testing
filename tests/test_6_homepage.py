from base_test import BaseTest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium.webdriver.common.action_chains import ActionChains


class TestHomepage(BaseTest):

    def test_01_app_bar_venue_links(self):
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
            (
                "Wedding Lawns Farmhouse",
                "Wedding Lawns Farmhouse Services | Wedding Planner India",
            ),
            ("Hotel", "Hotel Services | Wedding Planner India"),
            ("Banquet Halls", "Banquet Halls Services | Wedding Planner India"),
            ("Marriage Garden", "Marriage Garden Services | Wedding Planner India"),
            ("Wedding Halls", "Wedding Halls Services | Wedding Planner India"),
            ("Wedding Resorts", "Wedding Resorts Services | Wedding Planner India"),
        ]

        for link_text, expected_title in venue_links:
            button = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//button[text()='{link_text}']")
                )
            )
            button.click()
            self.wait.until(EC.title_is(expected_title))
            print(f"✅ {link_text} page title test passed.")

    def test_02_app_bar_vendor_links(self):
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
            (
                "Wedding Photographers",
                "Wedding Photographers Services | Wedding Planner India",
            ),
            ("Wedding Music", "Wedding Music Services | Wedding Planner India"),
            (
                "Wedding Transportation",
                "Wedding Transportation Services | Wedding Planner India",
            ),
            ("Tent House", "Tent House Services | Wedding Planner India"),
            ("Florists", "Florists Services | Wedding Planner India"),
            (
                "Wedding Decoration",
                "Wedding Decoration Services | Wedding Planner India",
            ),
            ("Wedding Agencies", "Wedding Agencies Services | Wedding Planner India"),
            ("Pandit", "Pandit Services | Wedding Planner India"),
            ("Astrologers", "Astrologers Services | Wedding Planner India"),
            (
                "Wedding Invitation",
                "Wedding Invitation Services | Wedding Planner India",
            ),
            ("Wedding Gift", "Wedding Gift Services | Wedding Planner India"),
            (
                "Wedding Coordinators",
                "Wedding Coordinators Services | Wedding Planner India",
            ),
            (
                "Wedding Videographers",
                "Wedding Videographers Services | Wedding Planner India",
            ),
            ("Wedding House", "Wedding House Services | Wedding Planner India"),
            (
                "Wedding Entertainment",
                "Wedding Entertainment Services | Wedding Planner India",
            ),
            ("Wedding Planner", "Wedding Planner Services | Wedding Planner India"),
            ("Wedding Cakes", "Wedding Cakes Services | Wedding Planner India"),
            ("Wedding DJ", "Wedding Dj Services | Wedding Planner India"),
            ("Photobooth", "Photobooth Services | Wedding Planner India"),
            ("Invitation", "Invitation Services | Wedding Planner India"),
        ]

        for link_text, expected_title in vendor_links:
            button = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//button[text()='{link_text}']")
                )
            )
            button.click()
            self.wait.until(EC.title_is(expected_title))
            print(f"✅ {link_text} page title test passed.")

    def test_03_app_bar_brides_links(self):
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
            (
                "Bridal Makeup Artist",
                "Bridal Makeup Artist Services | Wedding Planner India",
            ),
            ("Mehndi Artist", "Mehndi Artist Services | Wedding Planner India"),
            ("Makeup Salon", "Makeup Salon Services | Wedding Planner India"),
        ]

        for link_text, expected_title in brides_links:
            button = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//button[text()='{link_text}']")
                )
            )
            button.click()
            self.wait.until(EC.title_is(expected_title))
            print(f"✅ {link_text} page title test passed.")

    def test_04_app_bar_grooms_links(self):
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
                EC.element_to_be_clickable(
                    (By.XPATH, f'//button[text()="{link_text}"]')
                )
            )
            button.click()
            self.wait.until(EC.title_is(expected_title))
            print(f"✅ {link_text} page title test passed.")

    def test_05_app_bar_invitation_link(self):
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

    def test_06_app_bar_blog_link(self):
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

    def test_07_app_bar_other_links(self):
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
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Sign up']"))
        )
        signup_link.click()
        self.wait.until(EC.title_is("Signup | Marriage Vendors"))
        print("✅ Couple Sign Up page test passed.")

    def test_08_search_bar(self):
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

    def test_09_popular_search(self):
        self.driver.get("https://marriagevendors.com/")

        # List of (index, expected_title, description) for popular searches
        popular_searches = [
            (1, "Caterers Services | Wedding Planner India", "Caterering services"),
            (
                2,
                "Wedding Photographers Services | Wedding Planner India",
                "Wedding Photographers",
            ),
            (3, "Makeup Salon Services | Wedding Planner India", "Makeup Salon"),
            (
                4,
                "Wedding Entertainment Services | Wedding Planner India",
                "Wedding Entertainment",
            ),
            (5, "Wedding Gift Services | Wedding Planner India", "Wedding Gift"),
            (
                6,
                "Wedding Invitation Services | Wedding Planner India",
                "Wedding Invitation",
            ),
            (7, "Transport Services | Wedding Planner India", "Transport Services"),
            (8, "Wedding Planner Services | Wedding Planner India", "Wedding Planner"),
            (9, "Mehndi Artist Services | Wedding Planner India", "Mehndi Artist"),
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

    def test_10_service_card_section(self):
        service_cards = [
            (
                1,
                1,
                "Wedding Lawns Farmhouse Services | Wedding Planner India",
                "Wedding Venues",
            ),
            (1, 2, "Hotel Services | Wedding Planner India", "Wedding Venues"),
            (1, 3, "Banquet Halls Services | Wedding Planner India", "Wedding Venues"),
            (
                1,
                4,
                "Marriage Garden Services | Wedding Planner India",
                "Wedding Venues",
            ),
            (1, 5, "Wedding Halls Services | Wedding Planner India", "Wedding Venues"),
            (
                1,
                6,
                "Wedding Resorts Services | Wedding Planner India",
                "Wedding Venues",
            ),
            (2, 1, "Caterers Services | Wedding Planner India", "Wedding Vendors"),
            (
                2,
                2,
                "Wedding Invitation Services | Wedding Planner India",
                "Wedding Vendors",
            ),
            (2, 3, "Wedding Decor Services | Wedding Planner India", "Wedding Vendors"),
            (2, 4, "Wedding Gift Services | Wedding Planner India", "Wedding Vendors"),
            (
                2,
                5,
                "Wedding Photographers Services | Wedding Planner India",
                "Wedding Vendors",
            ),
            (
                2,
                6,
                "Wedding Coordinators Services | Wedding Planner India",
                "Wedding Vendors",
            ),
            (2, 7, "Wedding Music Services | Wedding Planner India", "Wedding Vendors"),
            (
                2,
                8,
                "Wedding Videographers Services | Wedding Planner India",
                "Wedding Vendors",
            ),
            (
                2,
                9,
                "Wedding Transportation Services | Wedding Planner India",
                "Wedding Vendors",
            ),
            (
                2,
                10,
                "Wedding House Services | Wedding Planner India",
                "Wedding Vendors",
            ),
            (2, 11, "Tent House Services | Wedding Planner India", "Wedding Vendors"),
            (
                2,
                12,
                "Wedding Entertainment Services | Wedding Planner India",
                "Wedding Vendors",
            ),
            (2, 13, "Florists Services | Wedding Planner India", "Wedding Vendors"),
            (
                2,
                14,
                "Wedding Planner Services | Wedding Planner India",
                "Wedding Vendors",
            ),
            (
                2,
                15,
                "Wedding Decoration Services | Wedding Planner India",
                "Wedding Vendors",
            ),
            (
                2,
                16,
                "Wedding Cakes Services | Wedding Planner India",
                "Wedding Vendors",
            ),
            (
                2,
                17,
                "Wedding Agencies Services | Wedding Planner India",
                "Wedding Vendors",
            ),
            (2, 18, "Wedding Dj Services | Wedding Planner India", "Wedding Vendors"),
            (2, 19, "Pandit Services | Wedding Planner India", "Wedding Vendors"),
            (2, 20, "Photobooth Services | Wedding Planner India", "Wedding Vendors"),
            (2, 21, "Astrologers Services | Wedding Planner India", "Wedding Vendors"),
            (3, 1, "Bridal Lahenga Services | Wedding Planner India", "Brides"),
            (3, 2, "Bridal Jewellery Services | Wedding Planner India", "Brides"),
            (3, 3, "Bridal Makeup Artist Services | Wedding Planner India", "Brides"),
            (3, 4, "Mehndi Artist Services | Wedding Planner India", "Brides"),
            (3, 5, "Makeup Salon Services | Wedding Planner India", "Brides"),
            (4, 1, "Sherwani Services | Wedding Planner India", "Grooms"),
            (4, 2, "Men'S Grooming Services | Wedding Planner India", "Grooms"),
            (4, 3, "Men'S Accessories Services | Wedding Planner India", "Grooms"),
            (
                5,
                1,
                "Wedding Planners Services | Wedding Planner India",
                "Wedding Services",
            ),
            (5, 2, "Decorators Services | Wedding Planner India", "Wedding Services"),
            (6, 1, "Live Bands Services | Wedding Planner India", "Other Services"),
            (
                6,
                2,
                "Luxury Transport Services | Wedding Planner India",
                "Other Services",
            ),
            (
                6,
                3,
                "Fireworks & Effects Services | Wedding Planner India",
                "Other Services",
            ),
        ]
        for idx, sub_idx, title, category in service_cards:
            self.driver.get("https://marriagevendors.com/")
            # Wait for the service card section to be visible
            wedding_venue_card = self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, f'//*[@id="serviceCategories"]/div/div/div[{idx}]')
                )
            )
            # Scroll until the element is visible on the screen
            while True:
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});",
                    wedding_venue_card,
                )
                # Check if the element is in the viewport
                in_viewport = self.driver.execute_script(
                    "var rect = arguments[0].getBoundingClientRect(); return (rect.top >= 0 && rect.bottom <= (window.innerHeight || document.documentElement.clientHeight));",
                    wedding_venue_card,
                )
                if in_viewport:
                    break
                time.sleep(0.2)
            # Wait for the service card to be clickable
            self.wait.until(EC.element_to_be_clickable(wedding_venue_card))
            # time.sleep(1)
            wedding_venue_card.click()
            # Find a child element relative to the current service_card
            child_element = wedding_venue_card.find_element(
                By.XPATH, f"./div[2]/div/div[{sub_idx}]"
            )
            # Scroll to the child element and click
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});", child_element
            )
            time.sleep(0.5)
            self.wait.until(EC.element_to_be_clickable(child_element))
            child_element.click()
            # Wait for title to be Wedding Lawns Farmhouse Services | Wedding Planner India
            try:
                self.wait.until(EC.title_is(title))
                print(f"✅ {category} - {title} test passed.")
            except Exception as e:
                print(f"❌ {category} - {title} test failed: {e}")

    def test_11_most_rated_wedding_vendors(self):
        discover_section = [
            (1, 1, "takatak", "Most Rated Wedding Vendors"),
            (1, 2, "product shot", "Most Rated Wedding Vendors"),
            (1, 3, "wedding videography", "Most Rated Wedding Vendors"),
            (1, 4, "birthday", "Most Rated Wedding Vendors"),
            (1, 5, "luxury decoration", "Most Rated Wedding Vendors"),
            (1, 6, "event photoshoot", "Most Rated Wedding Vendors"),
            (1, 7, "pre wedding (photo shoot)", "Most Rated Wedding Vendors"),
            (1, 8, "ankit caterers", "Most Rated Wedding Vendors"),
            (1, 9, "laxmi dj & tent house", "Most Rated Wedding Vendors"),
            (1, 10, "sai caterers", "Most Rated Wedding Vendors"),
            (1, 11, "the mat films", "Most Rated Wedding Vendors"),
            (1, 12, "pre wedding (video shoot) ", "Most Rated Wedding Vendors"),
            (1, 13, "birthday photoshoot", "Most Rated Wedding Vendors"),
            (1, 14, "nail arts", "Most Rated Wedding Vendors"),
            (1, 15, "wedding photography", "Most Rated Wedding Vendors"),
            (1, 16, "wedding", "Most Rated Wedding Vendors"),
            (1, 17, "sai tent and light house", "Most Rated Wedding Vendors"),
            (
                1,
                18,
                "pre wedding (photo & video) - 20,000",
                "Most Rated Wedding Vendors",
            ),
            (1, 19, "pre-wedding", "Most Rated Wedding Vendors"),
            (1, 20, "caterer", "Most Rated Wedding Vendors"),
            (2, 1, "takatak", "Most Viewed Services"),
            (2, 2, "laxmi dj & tent house", "Most Viewed Services"),
            (2, 3, "wedding", "Most Viewed Services"),
            (2, 4, "birthday", "Most Viewed Services"),
            (2, 5, "pre wedding (photo shoot)", "Most Viewed Services"),
            (3, 1, "takatak", "Top Wedding Caterers"),
            (3, 2, "caterer", "Top Wedding Caterers"),
            (3, 3, "sai tent and light house", "Top Wedding Caterers"),
            (3, 4, "sai caterers", "Top Wedding Caterers"),
            (3, 5, "ankit caterers", "Top Wedding Caterers"),
            (3, 6, "shree ram caterers", "Top Wedding Caterers"),
            (
                3,
                7,
                "goswami tent services - dee gee caterers & decorators",
                "Top Wedding Caterers",
            ),
            (4, 1, "product shot", "Top Wedding Photographers"),
            (4, 2, "wedding photography", "Top Wedding Photographers"),
            (4, 3, "p3 stories", "Top Wedding Photographers"),
            (4, 4, " studio dzone", "Top Wedding Photographers"),
            (4, 5, "sood photography", "Top Wedding Photographers"),
            (4, 6, "wedding photography", "Top Wedding Photographers"),
            (4, 7, "pre wedding (photo shoot)", "Top Wedding Photographers"),
            (4, 8, "parbhakar studio", "Top Wedding Photographers"),
            (4, 9, " kamal studios", "Top Wedding Photographers"),
            (4, 10, "wedding", "Top Wedding Photographers"),
            (5, 1, "pre wedding (video shoot) ", "Top Wedding Videographers"),
            (5, 2, "pre wedding (photo & video) - 20,000", "Top Wedding Videographers"),
            (5, 3, "wedding videography", "Top Wedding Videographers"),
            (5, 4, "events shot and vidoegraphy", "Top Wedding Videographers"),
            (6, 1, "nail arts", "Top Bridal Services"),
            (7, 1, "ankit dj", "Top Wedding DJs"),
            (7, 2, "sd happy dj", "Top Wedding DJs"),
            (7, 3, "jai jawala dj studio 7", "Top Wedding DJs"),
        ]
        for idx, sub_idx, title, category in discover_section:
            self.driver.get("https://marriagevendors.com/")
            # Wait for the "Most Rated Wedding Vendors" section to be visible
            most_rated_section = self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, f'//*[@id="discover"]/div/div[{idx}]')
                )
            )
            while True:
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});",
                    most_rated_section,
                )
                # Check if the element is in the viewport
                in_viewport = self.driver.execute_script(
                    "var rect = arguments[0].getBoundingClientRect(); return (rect.top >= 0 && rect.bottom <= (window.innerHeight || document.documentElement.clientHeight));",
                    most_rated_section,
                )
                if in_viewport:
                    break
                time.sleep(0.2)
            # Find a child element relative to the current service_card
            child_element = most_rated_section.find_element(
                By.XPATH, f"./div[2]/div/div[{sub_idx}]"
            )
            # Scroll horizontally to the child element and click
            while True:
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'nearest', inline: 'center'});",
                    child_element,
                )
                # Check if the element is in the viewport horizontally
                in_viewport = self.driver.execute_script(
                    "var rect = arguments[0].getBoundingClientRect(); return (rect.left >= 0 && rect.right <= (window.innerWidth || document.documentElement.clientWidth));",
                    child_element,
                )
                if in_viewport:
                    break
                time.sleep(0.2)
            self.wait.until(EC.visibility_of(child_element))
            self.wait.until(EC.element_to_be_clickable(child_element))
            child_element.click()

            try:
                self.wait.until(
                    EC.visibility_of_element_located(
                        (
                            By.XPATH,
                            f"//h1[contains(@class, 'font-bold') and contains(text(), '{title}')]",
                        )
                    )
                )
                print(f"✅ {category} - {title} test passed.")
            except Exception as e:
                print(f"❌ {category} - {title} test failed: {e}")

    def test_00_footer_links(self):
        links = [
            ("Wedding Lawns Farmhouse", "Wedding Venues", "Wedding Lawns Farmhouse Services | Wedding Planner India"),
            ("Hotel", "Wedding Venues", "Hotel Services | Wedding Planner India"),
            ("Banquet Halls", "Wedding Venues", "Banquet Halls Services | Wedding Planner India"),
            ("Marriage Garden", "Wedding Venues", "Marriage Garden Services | Wedding Planner India"),
            ("Wedding Resorts", "Wedding Venues", "Wedding Resorts Services | Wedding Planner India"),
            ("Caterers", "Wedding Vendors", "Caterers Services | Wedding Planner India"),
            ("Wedding Decor", "Wedding Vendors", "Wedding Decor Services | Wedding Planner India"),
            ("Wedding Photographers", "Wedding Vendors", "Wedding Photographers Services | Wedding Planner India"),
            ("Wedding Music", "Wedding Vendors", "Wedding Music Services | Wedding Planner India"),
            ("Wedding Transportation", "Wedding Vendors", "Wedding Transportation Services | Wedding Planner India"),
            ("Tent House", "Wedding Vendors", "Tent House Services | Wedding Planner India"),
            ("Florists", "Wedding Vendors", "Florists Services | Wedding Planner India"),
            ("Wedding Decoration", "Wedding Vendors", "Wedding Decoration Services | Wedding Planner India"),
            ("Wedding Agencies", "Wedding Vendors", "Wedding Agencies Services | Wedding Planner India"),
            ("Pandit", "Wedding Vendors", "Pandit Services | Wedding Planner India"),
            ("Astrologers", "Wedding Vendors", "Astrologers Services | Wedding Planner India"),
            ("Wedding Invitation", "Wedding Vendors", "Wedding Invitation Services | Wedding Planner India"),
            ("Wedding Gift", "Wedding Vendors", "Wedding Gift Services | Wedding Planner India"),
            ("Wedding Coordinators", "Wedding Vendors", "Wedding Coordinators Services | Wedding Planner India"),
            ("Wedding Videographers", "Wedding Vendors", "Wedding Videographers Services | Wedding Planner India"),
            ("Wedding House", "Wedding Vendors", "Wedding House Services | Wedding Planner India"),
            ("Wedding Entertainment", "Wedding Vendors", "Wedding Entertainment Services | Wedding Planner India"),
            ("Wedding Planner", "Wedding Vendors", "Wedding Planner Services | Wedding Planner India"),
            ("Wedding Cakes", "Wedding Vendors", "Wedding Cakes Services | Wedding Planner India"),
            ("Wedding DJ", "Wedding Vendors", "Wedding DJ Services | Wedding Planner India"),
            ("Photobooth", "Wedding Vendors", "Photobooth Services | Wedding Planner India"),
            ("Invitation", "Wedding Vendors", "Invitation Services | Wedding Planner India"),
            ("Bridal Lahenga", "Brides", "Bridal Lahenga Services | Wedding Planner India"),
            ("Bridal Jewellery", "Brides", "Bridal Jewellery Services | Wedding Planner India"),
            ("Bridal Makeup Artist", "Brides", "Bridal Makeup Artist Services | Wedding Planner India"),
            ("Mehndi Artist", "Brides", "Mehndi Artist Services | Wedding Planner India"),
            ("Makeup Salon", "Brides", "Makeup Salon Services | Wedding Planner India"),
            ("Sherwani", "Grooms", "Sherwani Services | Wedding Planner India"),
            ("Men's Grooming", "Grooms", "Men'S Grooming Services | Wedding Planner India"),
            ("Men's Accessories", "Grooms", "Men'S Accessories Services | Wedding Planner India")
        ]
        for link_text, category, title in links:
            self.driver.get("https://marriagevendors.com/")
            # Find the specific link in the footer
            footer_link = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, f"//footer//a[normalize-space(text())='{link_text}']"))
            )
            while True:
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});", footer_link
                )
                # Check if the element is in the viewport
                in_viewport = self.driver.execute_script(
                    "var rect = arguments[0].getBoundingClientRect(); return (rect.top >= 0 && rect.bottom <= (window.innerHeight || document.documentElement.clientHeight));",
                    footer_link,
                )
                if in_viewport:
                    break
                time.sleep(0.2)
            footer_link.click()
            try:
                self.wait.until(EC.title_is(title))
                print(f"✅ Footer link '{link_text}' in category '{category}' test passed.")
            except Exception as e:
                print(f"❌ Footer link '{link_text}' in category '{category}' test failed: {e}")

        
        

if __name__ == "__main__":
    unittest.main()
