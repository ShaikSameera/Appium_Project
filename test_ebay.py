import unittest
from Conftest import Conftest
import time


class TestEbay(Conftest):

    """Changing the location to Australia"""
    def test_updating_location(self):
        Conftest.setup()
        time.sleep(15)
        main_menu=self.driver.find_element_by_accessibility_id("Main navigation, open").click()
        time.sleep(10)
        #scrolling till settings button and click
        elem_to_tap=self.driver.find_element_by_id("com.ebay.mobile:id/navigation_header_container")
        elem_to_drag=self.driver.find_element_by_id("com.ebay.mobile:id/menuitem_myebay_header")
        self.driver.scroll(elem_to_drag,elem_to_tap)
        settings=self.driver.find_element_by_id("com.ebay.mobile:id/menuitem_settings").click()
        time.sleep(10)
        #click on country/region
        region=self.driver.find_element_by_accessibility_id("Country / region button").click()
        time.sleep(5)
        auto_detect=self.driver.find_element_by_id("android:id/widget_frame").click()
        country=self.driver.find_element_by_xpath("//android.widget.ListView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.TextView[1]").click()
        time.sleep(10)
        filter=self.driver.find_element_by_id("com.ebay.mobile:id/filter").send_keys("Australia")
        time.sleep(5)
        select_Australia=self.driver.find_element_by_accessibility_id("EBAY-AU").click()
        time.sleep(10)
        navigate_back=self.driver.find_element_by_accessibility_id("Navigate up").click()
        time.sleep(15)

    """SignIn to the app"""
    def test_signin(self, username="abc@gmail.com", password="ebay@123"):
        Conftest.setup()
        time.sleep(15)
        main_menu = self.driver.find_element_by_accessibility_id("Main navigation, open").click()
        time.sleep(10)
        sign_in = self.driver.find_element_by_accessibility_id("Sign in,double tap to activate").click()
        time.sleep(10)
        signin_type=self.driver.find_element_by_id("com.ebay.mobile:id/button_classic").click()
        time.sleep(10)
        uname = self.driver.find_element_by_id("com.ebay.mobile:id/edit_text_username")
        uname.send_keys(username)
        time.sleep(10)
        password=self.driver.find_element_by_id("com.ebay.mobile:id/view_password_layout").click()
        password.send_keys(password)
        time.sleep(10)
        signin_button=self.driver.find_element_by_id("com.ebay.mobile:id/button_sign_in").click()
        signin_button.click()

    """Searching for the item and verify the information of the item selected"""
    def test_search_verify_tv(self):
        Conftest.setup()
        time.sleep(10)
        self.driver.find_element_by_id("com.ebay.mobile:id/search_box").click()
        time.sleep(10)
        self.driver.find_element_by_id("com.ebay.mobile:id/search_src_text").send_keys("65 inc TV")
        time.sleep(10)
        self.driver.find_element_by_id("com.ebay.mobile:id/text").click()
        self.driver.find_element_by_id("com.ebay.mobile:id/popup_container").click()
        time.sleep(5)
        self.driver.find_element_by_id("com.ebay.mobile:id/search_item_text").click()
        time.sleep(10)
        assert self.driver.find_element_by_id("com.ebay.mobile:id/textview_item_name"),"Name of the item is not found"
        assert self.driver.find_element_by_id("com.ebay.mobile:id/textview_item_price"),"Price of the item is not found"


if __name__=='__main__':
    unittest.main()
