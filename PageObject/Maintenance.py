from selenium import webdriver
import time


class Maintenance():
    def __init__(self, driver):
        self.driver = driver
        self.Maintence = "//a[@id='menu_maintenance_purgeEmployee']"
        self.PurgeRecords = "//a[@id='menu_maintenance_PurgeRecords']"
        self.EmployeeRecords = "//ul/li[2]/a[@id='menu_maintenance_purgeCandidateData']"
        self.label_VerifyPassword = "//label[@for='confirm_password']"
        self.head = "//div[@class='head']"

    def Maintenance(self):
        Hover_Maintenace = self.driver.find_element_by_xpath(self.Maintence)
        action = webdriver.ActionChains(self.driver).move_to_element(Hover_Maintenace)
        action.perform()
        time.sleep(2)

    def SecondPurgeRecords(self):
        Hover_PurgeRecords = self.driver.find_element_by_xpath(self.PurgeRecords)
        action = webdriver.ActionChains(self.driver).move_to_element(Hover_PurgeRecords)
        action.perform()
        time.sleep(2)

    def SecondEmployeeRecords(self):
        Hover_EmployeeRecords = self.driver.find_element_by_xpath(self.EmployeeRecords)
        Hover_EmployeeRecords.click()
        time.sleep(5)

    def verifyPasswordText(self):
        Passtext = self.driver.find_element_by_xpath(self.label_VerifyPassword).text
        print(Passtext)
        assert Passtext in 'Verify Password *'

    def verfiyHeaderText(self):
        Head = self.driver.find_element_by_xpath(self.head).text
        print(Head)
        assert Head in 'Purge Employee Records'
