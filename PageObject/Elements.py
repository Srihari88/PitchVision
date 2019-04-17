from selenium import webdriver


class Elementspage():

    def __init__(self, driver):
        self.driver = driver

        self.UName = "txtUsername"
        self.Pass = "txtPassword"
        self.Submit = "Submit"

    def enter_username(self, user_name):
        self.driver.find_element_by_name(self.UName).clear()
        self.driver.find_element_by_name(self.UName).send_keys(user_name)

    def enter_password(self, password):
        self.driver.find_element_by_name(self.Pass).clear()
        self.driver.find_element_by_name(self.Pass).send_keys(password)

    def click_submit(self):
        self.driver.find_element_by_name(self.Submit).click()
