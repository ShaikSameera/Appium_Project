"""
Initializing the Appium session in the setup.
Ending the Appium session in the teardown
"""

import unittest
from appium import webdriver

class Conftest(unittest.TestCase):

    @classmethod
    def setup(self):
        "Setting up Appium"
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='8.1.0'
        desired_caps['udid']= 'dd09da270804'
        desired_caps['deviceName']='Mi A1'
        desired_caps['app']='C:\\Users\\samee\\Desktop\\apk\\eBay.apk'
        desired_caps['appPackage']='com.ebay.mobile'
        desired_caps['appActivity']='com.ebay.mobile.activities.MainActivity'
        desired_caps['noReset']= True
        hub='http://localhost:4723/wd/hub'
        self.driver = webdriver.Remote(hub,desired_caps)

    @classmethod
    def tearDown(self):
        "Quiting the appium driver"
        self.driver.quit()

if __name__=='__main__':
    unittest.main()



