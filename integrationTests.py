# based on https://stackoverflow.com/questions/49930377/how-do-integration-tests-on-a-very-simple-webpage-in-flask

import unittest
from selenium import webdriver
from app import db
from app.models import Driver, WearableInfo, PhysData


class PageLoadTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_wearableInfo(self):
        self.driver.get('/werable_info')
        # Make sure all wearables are listed
        # Get Wearable names from Database
        wearables = WearableInfo.query.all()
        wearableNames = list()
        for wearable in wearables:
            wearableNames.append(wearable.name)
        # Get Wearable names from Drop down
        # element_to_check = self.driver.

    def test_physData(self):
        self.driver.get('/phys_data')

    def test_drivers(self):
        self.driver.get('/drivers')

    # def test_main_page(self):
    #     self.driver.get('/subpage/sub')
    #     element_to_check = self.driver.find_element_by_tag_name(
    #         'name_of_element_tag_you_want_to_check')
    #     self.assertEqual(element_to_check.text, 'text that should be there')


if __name__ == '__main__':
    unittest.main()
