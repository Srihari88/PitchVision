from selenium import webdriver
import unittest
import time
from PageObject.POM import Elementspage
from PageObject.Maintenance import Maintenance
import pytest


class Maintence(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        driver = webdriver.Chrome(executable_path='/Library/Python/2.7/site-packages/chromedriver')
        driver.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(4)

    def test_ALogin(self):
        lo = Elementspage(driver)
        lo.Enter_username("Admin")
        lo.Enter_Password("admin123")
        lo.Sumbitdetails()
        time.sleep(5)
        title = driver.title
        cur = driver.current_url
        assert cur in 'https://opensource-demo.orangehrmlive.com/index.php/dashboard'
        assert title in 'OrangeHRM'

    def test_BMaintence(self):
        t2 = Maintenance(driver)
        t2.Maintenance()
        t2.SecondPurgeRecords()
        time.sleep(3)
        t2.SecondEmployeeRecords()
        time.sleep(5)
        cure = driver.current_url
        self.assertEqual(cure, 'https://opensource-demo.orangehrmlive.com/index.php/maintenance/purgeCandidateData')
        print(cure)

    def test_CvertifyTests(self):
        t3 = Maintenance(driver)
        t3.verifyPasswordText()
        t3.verfiyHeaderText()

    @classmethod
    def tearDownClass(cls):
        # driver.close()
        print("Application closed")


if __name__ == '__main__':
    unittest.main()
