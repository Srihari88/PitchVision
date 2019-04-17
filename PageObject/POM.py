from selenium import webdriver
from PageObject.Elements import Elementspage
import unittest


class Login(object):

    def __init__(self, driver):
        self.driver = driver

    def Username(self, user_name):
        self.driver.find_element_by_name("txtUsername").send_keys(user_name)

    def Password(self, password):
        self.driver.find_element_by_name("txtPassword").send_keys(password)

    def Sumbitdetails(self):
        self.driver.find_element_by_name("Submit").click()
