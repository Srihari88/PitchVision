from selenium import webdriver
import unittest
import time
from PageObject.Elements import Elementspage
from PageObject.HomePage import HomePageElements


class MyUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        driver = webdriver.Chrome(executable_path='/Library/Python/2.7/site-packages/chromedriver')
        driver.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(4)

    def test_ALogin(self):
        lo = Elementspage(driver)
        lo.enter_username("Admin")
        lo.enter_password("admin123")
        lo.click_submit()
        time.sleep(5)

    def test_BDistribution(self):
        h1 = HomePageElements(driver)
        h1.EmployeeDistribution()

    def test_CLegend(self):
        h2 = HomePageElements(driver)
        h2.LegendValues()

    def test_DLeave(self):
        h3 = HomePageElements(driver)
        h3.PendingLeavesRequest()

    def test_EAdminPage(self):
        h4 = HomePageElements(driver)
        h4.MoveAdminPage()
        h4.MoveUserManagement()
        h4.UserPage()

    # def test_FHomePage(self):
    #     print(" Hello second method")
    #     ho = HomePageElements(driver)
    #     ho.AWelcomeLink()
    #     time.sleep(2)
    #     ho.BLogout()

    @classmethod
    def tearDownClass(cls):
        # driver.close()
        print(" Application closed")


if __name__ == '__main__':
    unittest.main()
