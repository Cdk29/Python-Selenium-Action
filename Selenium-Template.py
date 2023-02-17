import selenium
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import FirefoxOptions
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        self.browser = webdriver.Firefox(options=opts)

    def tearDown(self):
        self.browser.quit()
        
    def test_that_the_website_exist(self):
        self.browser.get('https://www.projet-ipf2023.com/')
        title = self.browser.title
        self.assertIn('', title)

unittest.main()

