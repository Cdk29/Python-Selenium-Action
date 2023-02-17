import selenium
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
        
    def test_that_the_website_exist(self):
        self.browser.get('https://www.projet-ipf2023.com/')
        title = self.browser.title
        self.assertIn('', title)

unittest.main()

