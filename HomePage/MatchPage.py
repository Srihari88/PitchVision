"""
Author: Srihari
Website: PitchVision match page, Verifying the match page matches.

"""
from selenium import webdriver
import unittest
import time


class MatchPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        driver = webdriver.Chrome(executable_path='/Library/Python/2.7/site-packages/chromedriver')
        print("Open PitchVision Application")
        driver.get("https://www.pitchvision.com/")
        time.sleep(4)

    def test_JatchLink_Verify(self):
        Matches = driver.find_element_by_xpath("//a[@href='/#/pv-matches']")
        Matches.click()
        MatchURL = driver.current_url
        print(MatchURL)
        assert MatchURL in 'https://www.pitchvision.com/#/pv-matches'

    @classmethod
    def tearDownClass(cls):
        # driver.close()
        print("Close Application")


if __name__ == '__main__':
    unittest.main()
