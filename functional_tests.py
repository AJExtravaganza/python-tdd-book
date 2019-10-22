from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
                self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # User navigates to the homepage
        self.browser.get('http://localhost:8000')

        # The page title shows 'To-Do'
        self.assertIn('To-Do', self.browser.title)
        
        # User is invited to enter a to-do item immediately
        self.fail('Finish this test!')

        # User types "Buy peacock feathers" into a text box


        # When user hits enter, the page updates, and now lists
        # '1: Buy peacock feathers' as an item in a to-do list


        # There is still a text box inviting her to add another item.
        # User enters "Use peacock feathers to make a fly"


        # The page updates again, now showing both items on her list

        # The site has generated a unique URL for the user

        # There is some explanatory text to that effect

        # User visits the url - the to-do list has persisted and been recalled

        browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
