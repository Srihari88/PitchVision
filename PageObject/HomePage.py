from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time


class HomePageElements():

    def __init__(self, driver):
        self.driver = driver

        self.welcome = "//a[@id='welcome']"
        self.logout_link = "//a[text()='Logout']"
        self.EmplyeeDis = "//fieldset[@id='panel_resizable_1_0']"
        self.Legend = "//fieldset[@id='panel_resizable_1_1']"
        self.PendingLeave = "//fieldset[@id='panel_resizable_1_2']"
        self.Admin = "//a[@id='menu_admin_viewAdminModule']"
        self.Usermanagement = "//a[@id='menu_admin_UserManagement']"
        self.Users = "//a[@id='menu_admin_viewSystemUsers']"
        self.Username = "//input[@id='searchSystemUser_userName']"
        self.UserRole = "//select[@id='searchSystemUser_userType']"
        self.EmployeeName = "//input[@id='searchSystemUser_employeeName_empName']"
        self.Status = "//select[@id='searchSystemUser_status']"
        self.Seach = "//input[@id='searchBtn']"
        self.Data = "//form[@id='frmList_ohrmListComponent']"

        # Add user

        self.Add = "//input[@id='btnAdd']"
        self.UserAddRole = "//select[@id='systemUser_userType']"
        self.AddEmplyeeName = "//input[@id='systemUser_employeeName_empName']"
        self.AddUsername = "//input[@id='systemUser_userName']"
        self.AddStatus = "//select[@id='systemUser_status']"
        self.addpassword = "//input[@id='systemUser_password']"
        self.Addconfirmpassword = "//input[@id='systemUser_confirmPassword']"
        self.SaveAddedUser = "//input[@id='btnSave']"

        # Add user Label
        self.labelUserRole = "//label[@for='systemUser_userType']"
        self.labelEmplyeename = "//label[@for='systemUser_employeeName']"
        self.labelUsername = "//label[@for='systemUser_userName']"
        self.labelStatus = "//label[@for='systemUser_status']"
        self.labelPassword = "//label[@for='systemUser_password']"
        self.labelConfirmpassword = "//label[@for='systemUser_confirmPassword']"
        self.labelverifytext = "//div[@class='helpText']/span"

    def AWelcomeLink(self):
        self.driver.find_element_by_xpath(self.welcome).click()

    def BLogout(self):
        self.driver.find_element_by_xpath(self.logout_link).click()

    def EmployeeDistribution(self):
        Sunnit = self.driver.find_element_by_xpath(self.EmplyeeDis)
        print(Sunnit.text)

    def LegendValues(self):
        Legend_values = self.driver.find_element_by_xpath(self.Legend)
        print(Legend_values.text)

    def PendingLeavesRequest(self):
        Pending_Leave = self.driver.find_element_by_xpath(self.PendingLeave)
        print(Pending_Leave.text)
        time.sleep(3)

    def MoveAdminPage(self):
        print(" Hello Move mouse over")
        Hover = self.driver.find_element_by_xpath(self.Admin)
        action = webdriver.ActionChains(self.driver).move_to_element(Hover)
        action.perform()
        time.sleep(2)

    def MoveUserManagement(self):
        Hover1 = self.driver.find_element_by_xpath(self.Usermanagement)
        action1 = webdriver.ActionChains(self.driver).move_to_element(Hover1)
        action1.perform()
        time.sleep(2)

    def UserPage(self):
        Hover2 = self.driver.find_element_by_xpath(self.Users)
        Hover2.click()

    def EnterUsername(self, U_name):
        self.driver.find_element_by_xpath(self.Username).clear()
        self.driver.find_element_by_xpath(self.Username).send_keys(U_name)

    def Userrole(self):
        select = Select(self.driver.find_element_by_xpath(self.UserRole))
        select.select_by_index(2)

    def Seach_User(self):
        self.driver.find_element_by_xpath(self.Seach).click()

    def Data_Search(self):
        Userdata = self.driver.find_element_by_xpath(self.Data)
        print(Userdata.text)

    def Add_Addbutton(self):
        self.driver.find_element_by_xpath(self.Add).click()

    def user_Addrole(self):
        select1 = Select(self.driver.find_element_by_xpath(self.UserAddRole))
        select1.select_by_visible_text("Admin")

    def add_employee(self, empadd):
        self.driver.find_element_by_xpath(self.AddEmplyeeName).send_keys(empadd)

    def add_username(self, addusername):
        self.driver.find_element_by_xpath(self.AddUsername).send_keys(addusername)

    def add_status(self):
        addstat = Select(self.driver.find_element_by_xpath(self.AddStatus))
        addstat.select_by_visible_text("Enabled")

    def Addpassword(self, passd):
        self.driver.find_element_by_xpath(self.addpassword).send_keys(passd)

    def confirmpassword(self, con_password):
        self.driver.find_element_by_xpath(self.Addconfirmpassword).send_keys(con_password)

    def SaveUser(self):
        self.driver.find_element_by_xpath(self.SaveAddedUser).click()

    def verify_labelUserRole(self):
        userrole = self.driver.find_element_by_xpath(self.labelUserRole).text
        print(userrole)
        assert userrole in 'User Role *'

    def verify_EmplyeeName(self):
        userrole1 = self.driver.find_element_by_xpath(self.labelEmplyeename).text
        print(userrole1)
        assert userrole1 in 'Employee Name *'

    def verify_Username(self):
        userrole2 = self.driver.find_element_by_xpath(self.labelUsername).text
        print(userrole2)
        assert userrole2 in 'Username *'

    def verify_Status(self):
        userrole2 = self.driver.find_element_by_xpath(self.labelStatus).text
        print(userrole2)
        assert userrole2 in 'Status *'

    def verify_Password(self):
        userrole3 = self.driver.find_element_by_xpath(self.labelPassword).text
        print(userrole3)
        assert userrole3 in 'Password'

    def verify_confirmpasswrod(self):
        userrole4 = self.driver.find_element_by_xpath(self.labelConfirmpassword).text
        print(userrole4)
        assert userrole4 in 'Confirm Password'

    def verify_helptext(self):
        help = self.driver.find_element_by_xpath(self.labelverifytext).text
        print(help)
        assert help in 'For a strong password, please use a hard to guess combination of text with upper and lower case characters, symbols and numbers'
