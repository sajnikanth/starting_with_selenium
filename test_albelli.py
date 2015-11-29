import selenium.webdriver
import unittest
from holmium.core import Page, Element, Locators

class AlbelliHomePage(Page):
    home_page_banner = Element(Locators.ID, 'hero-shot', timeout=5)

class AlbelliTest(unittest.TestCase):
    def setUp(self):
        self.page = AlbelliHomePage(self.driver, self.driver._holmium_config['environment'])

    def test_home_page(self):
        assert self.page.home_page_banner.is_displayed()
