import unittest

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager



class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print('Try to clear all page cache')
        self.browser.delete_all_cookies();

    def tearDown(self):
        self.browser.quit()
    
    def test_user_cant_check_any_pages_before_login(self):
        # Robert go to the home.intensifly.io for using our cool features
        self.browser.get('http://localhost:8000/')

        # He notice the page title is
        self.assertIn('Intensifly', self.browser.title)

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()