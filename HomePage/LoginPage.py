from selenium import webdriver
import unittest
import time


class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        driver = webdriver.Chrome(executable_path='/Library/Python/2.7/site-packages/chromedriver')
        driver.get("https://www.pitchvision.com/#/login")
        time.sleep(8)

    # def test_verifyLink(self):
    #     Link = driver.find_element_by_xpath("//a[text()='Log In']")
    #     Link.click()

    def test_AenterLogin(self):
        Username = driver.find_element_by_xpath("//form[@name='pvLoginform']/div/input[@name='username']")
        Username.send_keys("daisy.dalia")

        Password = driver.find_element_by_xpath("//form[@name='pvLoginform']/div/input[@name='password']")
        Password.send_keys("dentrain")

        Submit = driver.find_element_by_xpath("//form[@name='pvLoginform']/div/input[@value='Log In']")
        Submit.click()

        time.sleep(10)

    def test_BVerifyUser(self):
        url = driver.current_url
        print(url)
        assert url in 'https://www.pitchvision.com/#/daisy'

    @classmethod
    def tearDownClass(cls):
        driver.close()
        print("Close Application")


if __name__ == '__main__':
    unittest.main()
