from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
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
        action2 = webdriver.ActionChains(self.driver).move_to_element(Hover2)
        action2.click()
        time.sleep(2)
