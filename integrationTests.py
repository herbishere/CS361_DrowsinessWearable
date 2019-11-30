# based on https://stackoverflow.com/questions/49930377/how-do-integration-tests-on-a-very-simple-webpage-in-flask

import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from app import db
from app.models import Driver, WearableInfo, PhysData

PATH = 'http://127.0.0.1:5000'


class PageLoadTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.driver.quit()

    def test_wearableInfo(self):
        '''
        test_wearableInfo ensures that the wearables are loaded into the selection menu
        '''
        self.driver.get(PATH + '/wearable_info')
        wearables = WearableInfo.query.all()
        # Get Wearable names from Database
        wearableNamesDatabase = list()
        for wearable in wearables:
            wearableNamesDatabase.append(wearable.name)
        # Get Wearable names from Drop down
        wearableNamesWeb = list()
        for index in range(len(wearableNamesDatabase)):
            xpath = '//*[@id="wearable_name"]/option[' + str(index + 1) + ']'
            element_to_check = self.driver.find_element_by_xpath(xpath)
            wearableNamesWeb.append(element_to_check.text)
        # Check that both sets are equal
        self.assertEqual(set(wearableNamesWeb), set(wearableNamesDatabase))

    def test_physData(self):
        '''
        '''
        self.driver.get(PATH + '/phys_data')
        physData = PhysData.query.all()

    def test_drivers(self):
        '''
        '''
        self.driver.get(PATH + '/drivers')
        drivers = Driver.query.all()


if __name__ == '__main__':
    unittest.main()
