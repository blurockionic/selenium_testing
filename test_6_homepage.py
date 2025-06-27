from base_test import BaseTest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium.webdriver.common.action_chains import ActionChains


class TestHomepage(BaseTest):

    def test_1_homepage_title(self):
        # Check if the homepage title is correct
        # wait for the page to load
        self.wait.until(EC.title_is("Wedding Services & Vendors | Marriage Vendors"))
        # self.assertEqual(self.driver.title, "Wedding Services & Vendors | Marriage Vendors")
        print("✅ Homepage title test passed.")

    def test_2_app_bar_venue_links(self):
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

        # Checking Wedding Lawns Farmhouse link in the dropdown
        wedding_lawns_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[text()='Wedding Lawns Farmhouse']")
            )
        )
        wedding_lawns_button.click()
        self.wait.until(
            EC.title_is("Wedding Lawns Farmhouse Services | Wedding Planner India")
        )
        # self.assertEqual(self.driver.title, "Wedding Lawns Farmhouse Services | Wedding Planner India")
        print("✅ Wedding Lawns Farmhouse page title test passed.")

        # Checking Hotel link in the dropdown
        hotel_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Hotel']"))
        )
        hotel_button.click()
        self.wait.until(EC.title_is("Hotel Services | Wedding Planner India"))
        # self.assertEqual(self.driver.title, "Hotel Services | Wedding Planner India")
        print("✅ Hotel page title test passed.")

        # Checking Banquet Hall link in the dropdown
        banquet_hall_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Banquet Halls']"))
        )
        banquet_hall_button.click()
        self.wait.until(EC.title_is("Banquet Halls Services | Wedding Planner India"))

        # self.assertEqual(self.driver.title, "Banquet Halls Services | Wedding Planner India")
        print("✅ Banquet Halls page title test passed.")

        # Checking Marriage Garden link in the dropdown
        marriage_garden = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Marriage Garden']"))
        )
        marriage_garden.click()
        self.wait.until(EC.title_is("Marriage Garden Services | Wedding Planner India"))

        # self.assertEqual(self.driver.title, "Marriage Garden Services | Wedding Planner India")
        print("✅ Marriage Garden page title test passed.")

        # checking Wedding Halls link in the dropdown
        wedding_halls = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Wedding Halls']"))
        )
        wedding_halls.click()
        self.wait.until(EC.title_is("Wedding Halls Services | Wedding Planner India"))
        print("✅ Wedding Halls page title test passed.")

        # checking Wedding Resorts link in the dropdown
        wedding_resorts = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Wedding Resorts']"))
        )
        wedding_resorts.click()
        self.wait.until(EC.title_is("Wedding Resorts Services | Wedding Planner India"))
        print("✅ Wedding Resorts page title test passed.")

    def test_3_app_bar_vendor_links(self):
        venue_link = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//li[.//span[text()='Vendor']]//span[contains(@class, 'cursor-pointer')]",
                )
            )
        )
        ActionChains(self.driver).move_to_element(venue_link).perform()

        # Checking Caterers link in the dropdown
        caterers_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Caterers']"))
        )
        caterers_button.click()
        self.wait.until(EC.title_is("Caterers Services | Wedding Planner India"))
        print("✅ Caterers page title test passed.")

        # Checking Wedding Decor link in the dropdown
        wedding_decor_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Wedding Decor']"))
        )
        wedding_decor_button.click()
        self.wait.until(EC.title_is("Wedding Decor Services | Wedding Planner India"))
        print("✅ Wedding Decor page title test passed.")

        # Checking Wedding Photographers link in the dropdown
        wedding_photographers_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[text()='Wedding Photographers']")
            )
        )
        wedding_photographers_button.click()
        self.wait.until(
            EC.title_is("Wedding Photographers Services | Wedding Planner India")
        )
        print("✅ Wedding Photographers page title test passed.")

        # Checking Wedding Music link in the dropdown
        wedding_music_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Wedding Music']"))
        )
        wedding_music_button.click()
        self.wait.until(EC.title_is("Wedding Music Services | Wedding Planner India"))
        print("✅ Wedding Music page title test passed.")

        # Checking Wedding Transportation link in the dropdown
        wedding_transportation_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[text()='Wedding Transportation']")
            )
        )
        wedding_transportation_button.click()
        self.wait.until(
            EC.title_is("Wedding Transportation Services | Wedding Planner India")
        )
        print("✅ Wedding Transportation page title test passed.")

        # Checking Tent House link in the dropdown
        tent_house_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Tent House']"))
        )
        tent_house_button.click()
        self.wait.until(EC.title_is("Tent House Services | Wedding Planner India"))
        print("✅ Tent House page title test passed.")

        # Checking Florists link in the dropdown
        florists_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Florists']"))
        )
        florists_button.click()
        self.wait.until(EC.title_is("Florists Services | Wedding Planner India"))
        print("✅ Florists page title test passed.")

        # Checking Wedding Decoration link in the dropdown
        wedding_decoration_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[text()='Wedding Decoration']")
            )
        )
        wedding_decoration_button.click()
        self.wait.until(
            EC.title_is("Wedding Decoration Services | Wedding Planner India")
        )
        print("✅ Wedding Decoration page title test passed.")

        # Checking Wedding Agencies link in the dropdown
        wedding_agencies_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[text()='Wedding Agencies']")
            )
        )
        wedding_agencies_button.click()
        self.wait.until(
            EC.title_is("Wedding Agencies Services | Wedding Planner India")
        )
        print("✅ Wedding Agencies page title test passed.")

        # Checking Pandit link in the dropdown
        pandit_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Pandit']"))
        )
        pandit_button.click()
        self.wait.until(EC.title_is("Pandit Services | Wedding Planner India"))
        print("✅ Pandit page title test passed.")

        # Checking Astrologers link in the dropdown
        astrologers_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Astrologers']"))
        )
        astrologers_button.click()
        self.wait.until(EC.title_is("Astrologers Services | Wedding Planner India"))
        print("✅ Astrologers page title test passed.")

        # Checking Wedding Invitation link in the dropdown
        wedding_invitation_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[text()='Wedding Invitation']")
            )
        )
        wedding_invitation_button.click()
        self.wait.until(
            EC.title_is("Wedding Invitation Services | Wedding Planner India")
        )
        print("✅ Wedding Invitation page title test passed.")

        # Checking Wedding Gift link in the dropdown
        wedding_gift_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Wedding Gift']"))
        )
        wedding_gift_button.click()
        self.wait.until(EC.title_is("Wedding Gift Services | Wedding Planner India"))
        print("✅ Wedding Gift page title test passed.")

        # Checking Wedding Coordinators link in the dropdown
        wedding_coordinators_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[text()='Wedding Coordinators']")
            )
        )
        wedding_coordinators_button.click()
        self.wait.until(
            EC.title_is("Wedding Coordinators Services | Wedding Planner India")
        )
        print("✅ Wedding Coordinators page title test passed.")

        # Checking Wedding Videographers link in the dropdown
        wedding_videographers_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[text()='Wedding Videographers']")
            )
        )
        wedding_videographers_button.click()
        self.wait.until(
            EC.title_is("Wedding Videographers Services | Wedding Planner India")
        )
        print("✅ Wedding Videographers page title test passed.")

        # Checking Wedding House link in the dropdown
        wedding_house_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Wedding House']"))
        )
        wedding_house_button.click()
        self.wait.until(EC.title_is("Wedding House Services | Wedding Planner India"))
        print("✅ Wedding House page title test passed.")

        # Checking Wedding Entertainment link in the dropdown
        wedding_entertainment_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[text()='Wedding Entertainment']")
            )
        )
        wedding_entertainment_button.click()
        self.wait.until(
            EC.title_is("Wedding Entertainment Services | Wedding Planner India")
        )
        print("✅ Wedding Entertainment page title test passed.")

        # Checking Wedding Planner link in the dropdown
        wedding_planner_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Wedding Planner']"))
        )
        wedding_planner_button.click()
        self.wait.until(EC.title_is("Wedding Planner Services | Wedding Planner India"))
        print("✅ Wedding Planner page title test passed.")

        # Checking Wedding Cakes link in the dropdown
        wedding_cakes_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Wedding Cakes']"))
        )
        wedding_cakes_button.click()
        self.wait.until(EC.title_is("Wedding Cakes Services | Wedding Planner India"))
        print("✅ Wedding Cakes page title test passed.")

        # Checking Wedding DJ link in the dropdown
        wedding_dj_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Wedding DJ']"))
        )
        wedding_dj_button.click()
        self.wait.until(EC.title_is("Wedding Dj Services | Wedding Planner India"))
        print("✅ Wedding DJ page title test passed.")

        # Checking Photobooth link in the dropdown
        photobooth_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Photobooth']"))
        )
        photobooth_button.click()
        self.wait.until(EC.title_is("Photobooth Services | Wedding Planner India"))
        print("✅ Photobooth page title test passed.")

        # Checking Invitation link in the dropdown
        invitation_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Invitation']"))
        )
        invitation_button.click()
        self.wait.until(EC.title_is("Invitation Services | Wedding Planner India"))
        print("✅ Invitation page title test passed.")

    def test_4_app_bar_brides_links(self):
        venue_link = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//li[.//span[text()='Brides']]//span[contains(@class, 'cursor-pointer')]",
                )
            )
        )
        ActionChains(self.driver).move_to_element(venue_link).perform()

        # Checking Bridal Lahenga link in the dropdown
        bridal_lahenga_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Bridal Lahenga']"))
        )
        bridal_lahenga_button.click()
        self.wait.until(EC.title_is("Bridal Lahenga Services | Wedding Planner India"))
        print("✅ Bridal Lahenga page title test passed.")

        # Checking Bridal Jewellery link in the dropdown
        bridal_jewellery_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Bridal Jewellery']"))
        )
        bridal_jewellery_button.click()
        self.wait.until(EC.title_is("Bridal Jewellery Services | Wedding Planner India"))
        print("✅ Bridal Jewellery page title test passed.")

        # Checking Bridal Makeup Artist link in the dropdown
        bridal_makeup_artist_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[text()='Bridal Makeup Artist']")
            )
        )
        bridal_makeup_artist_button.click()
        self.wait.until(EC.title_is("Bridal Makeup Artist Services | Wedding Planner India"))
        print("✅ Bridal Makeup Artist page title test passed.")

        # Checkig Mehndi Artist link in the dropdown
        mehndi_artist_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Mehndi Artist']"))
        )
        mehndi_artist_button.click()
        self.wait.until(EC.title_is("Mehndi Artist Services | Wedding Planner India"))
        print("✅ Mehndi Artist page title test passed.")

        # Makeup Salon link in the dropdown
        makeup_salon_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Makeup Salon']"))
        )
        makeup_salon_button.click()
        self.wait.until(EC.title_is("Makeup Salon Services | Wedding Planner India"))
        print("✅ Makeup Salon page title test passed.")

    def test_5_app_bar_grooms_links(self):
        venue_link = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//li[.//span[text()='Grooms']]//span[contains(@class, 'cursor-pointer')]",
                )
            )
        )
        ActionChains(self.driver).move_to_element(venue_link).perform()

        # Sherwani link in the dropdown
        sherwani_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Sherwani']"))
        )
        sherwani_button.click()
        self.wait.until(EC.title_is("Sherwani Services | Wedding Planner India"))
        print("✅ Sherwani page title test passed.")

        # Men's Grooming link in the dropdown
        mens_grooming_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()=\"Men's Grooming\"]"))
        )
        mens_grooming_button.click()
        self.wait.until(EC.title_is("Men'S Grooming Services | Wedding Planner India"))
        print("✅ Men's Grooming page title test passed.")

        # Men's Accessories link in the dropdown
        mens_accessories_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()=\"Men's Accessories\"]"))
        )
        mens_accessories_button.click()
        self.wait.until(EC.title_is("Men'S Accessories Services | Wedding Planner India"))
        print("✅ Men's Accessories page title test passed.")

    def test_6_app_bar_invitation_link(self):
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

    def test_7_app_bar_blog_link(self):
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
    
    def test_8_app_bar_other_links(self):
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

if __name__ == "__main__":
    unittest.main()
