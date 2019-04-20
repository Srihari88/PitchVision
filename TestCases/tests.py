from selenium import webdriver
import unittest
import time
from PageObject.POM import Elementspage
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
        lo.Enter_username("Admin")
        lo.Enter_Password("admin123")
        lo.Sumbitdetails()
        time.sleep(5)
        title = driver.title
        cur = driver.current_url
        assert cur in 'https://opensource-demo.orangehrmlive.com/index.php/dashboard'
        assert title in 'OrangeHRM'

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
        userpage = driver.current_url
        assert userpage in 'https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers'

    def test_FUserFourm(self):
        h5 = HomePageElements(driver)
        h5.EnterUsername("SriHari")
        h5.Userrole()

    def test_HSearch(self):
        h6 = HomePageElements(driver)
        h6.Seach_User()
        h6.Data_Search()

    def test_Kadduser(self):
        h7 = HomePageElements(driver)
        h7.Add_Addbutton()
        time.sleep(5)
        h7.user_Addrole()
        h7.add_employee("Steven Edwards")
        h7.add_username("MyDearHes")
        h7.add_status()
        h7.Addpassword("Hellomydear")
        h7.confirmpassword("Hellomydear")
        h7.SaveUser()

    def test_LverifyDetails(self):
        h8 = HomePageElements(driver)
        h8.verify_confirmpasswrod()
        h8.verify_EmplyeeName()
        h8.verify_labelUserRole()
        h8.verify_Password()
        h8.verify_helptext()
        h8.verify_Status()

    @classmethod
    def tearDownClass(cls):
        # driver.close()
        print(" Application closed")


if __name__ == '__main__':
    unittest.main()
