import selenium.webdriver
import unittest

class AlbelliTest(unittest.TestCase):
    def setUp(self):
        self.driver = selenium.webdriver.Firefox()
        self.url = 'http://albelli.nl'

    def test_home_page(self):
        self.driver.get(self.url)
        home_page_banner = self.driver.find_element_by_id('hero-shot')
        assert home_page_banner.is_displayed()

    def tearDown(self):
        self.driver.quit()
