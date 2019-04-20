from selenium import webdriver
import unittest


class Elementspage(object):

    def __init__(self, driver):
        self.driver = driver

        self.Username = "txtUsername"
        self.password = "txtPassword"
        self.submit = "Submit"

    def Enter_username(self, user_name):
        self.driver.find_element_by_name(self.Username).send_keys(user_name)

    def Enter_Password(self, password):
        self.driver.find_element_by_name(self.password).send_keys(password)

    def Sumbitdetails(self):
        self.driver.find_element_by_name(self.submit).click()
