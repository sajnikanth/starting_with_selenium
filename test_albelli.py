import selenium.webdriver
import unittest

class AlbelliTest(unittest.TestCase):
    def setUp(self):
        self.driver.get(self.driver._holmium_config['environment'])

    def test_home_page(self):
        home_page_banner = self.driver.find_element_by_id('hero-shot')
        assert home_page_banner.is_displayed()
