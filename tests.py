# based on https://stackoverflow.com/questions/49930377/how-do-integration-tests-on-a-very-simple-webpage-in-flask

import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from app import db
from app.models import Driver, WearableInfo, PhysData, UserSettings
from insert import userSettings as userSettings_from_insert

PATH = 'http://127.0.0.1:5000'


class PageLoadTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.driver.quit()

    # def test_wearableInfo(self):
    #     '''
    #     test_wearableInfo ensures that the wearables are loaded into the selection menu
    #     '''
    #     self.driver.get(PATH + '/wearable_info')
    #     wearables = WearableInfo.query.all()
    #     # Get Wearable names from Database
    #     wearableNamesDatabase = list()
    #     for wearable in wearables:
    #         wearableNamesDatabase.append(wearable.name)
    #     # Get Wearable names from Drop down
    #     wearableNamesWeb = list()
    #     for index in range(len(wearableNamesDatabase)):
    #         xpath = '//*[@id="wearable_name"]/option[' + str(index + 1) + ']'
    #         element_to_check = self.driver.find_element_by_xpath(xpath)
    #         wearableNamesWeb.append(element_to_check.text)
    #     # Check that both sets are equal
    #     self.assertEqual(set(wearableNamesWeb), set(wearableNamesDatabase))

    # def test_physData(self):
    #     '''
    #     '''
    #     self.driver.get(PATH + '/phys_data')
    #     physData = PhysData.query.all()

    # def test_drivers(self):
    #     '''
    #     '''
    #     self.driver.get(PATH + '/drivers')
    #     drivers = Driver.query.all()

    #     # Make sure that Wearable Names populated the correct corresponding database data
    #     # Get Wearable names from Database
    #     wearables = WearableInfo.query.all()
    #     wearableNamesDatabase = list()
    #     for wearable in wearables:
    #         wearableNamesDatabase.append(wearable.name)
    #     # Get Wearable names from Drop down
    #     wearableNamesWeb = list()
    #     for index in range(len(wearableNamesDatabase)):
    #         xpath = '//*[@id="select_wearable"]/option[' + str(index + 1) + ']'
    #         element_to_check = self.driver.find_element_by_xpath(xpath)
    #         wearableNamesWeb.append(element_to_check.text)
    #     # Check that both sets are equal
    #     self.assertEqual(set(wearableNamesWeb), set(wearableNamesDatabase))

    def test_UserSettingsLoaded(self):
        '''
        Make sure the user settings are properly loaded on the page and match the database
        '''
        self.driver.get(PATH + '/settings')

        # Get the data from the user settings table.
        userSettings_table = UserSettings.query.all()[0]

        # Get the values from the page
        userSettings_page = UserSettings()
        userSettings_page.shock = self.driver.find_element_by_xpath(
            '//*[@id="shock"]').is_selected()
        userSettings_page.noise = self.driver.find_element_by_xpath(
            '//*[@id="noise"]').is_selected()
        userSettings_page.vibration = self.driver.find_element_by_xpath(
            '//*[@id="vibration"]').is_selected()
        userSettings_page.alertFrequency = self.driver.find_element_by_xpath(
            '//*[@id="alertFrequency"]').get_attribute("value")
        userSettings_page.drowsinessThreshold = self.driver.find_element_by_xpath(
            '//*[@id="drowsinessThreshold"]').get_attribute("value")

        # Check that both objects have the same values
        self.assertEqual(bool(userSettings_table.shock),
                         userSettings_page.shock)
        self.assertEqual(bool(userSettings_table.noise),
                         userSettings_page.noise)
        self.assertEqual(bool(userSettings_table.vibration),
                         userSettings_page.vibration)
        self.assertEqual(userSettings_table.alertFrequency,
                         int(userSettings_page.alertFrequency))
        self.assertEqual(userSettings_table.drowsinessThreshold,
                         float(userSettings_page.drowsinessThreshold))


if __name__ == '__main__':
    # Database Unit Tests
    # Unit Test 1 - Queried Data matches data from insert.py
    usersettings = UserSettings.query.all()[0]
    if (usersettings.shock == userSettings_from_insert.shock and
        usersettings.noise == userSettings_from_insert.noise and
        usersettings.vibration == userSettings_from_insert.vibration and
        usersettings.alertFrequency == userSettings_from_insert.alertFrequency and
            usersettings.drowsinessThreshold == userSettings_from_insert.drowsinessThreshold):
        print("Test 1: PASSED Queried Data matches data from insert.py\n")
    else:
        print("Test 1: FAILED Queried Data does not match data from insert.py\n")

    # # Unit Test 2 - Change Value
    # s1 = UserSettings.query.all()[0]
    # s1.shock = 0
    # s1.noise = 0
    # s1.vibration = 1
    # db.session.commit()
    # s2 = UserSettings.query.all()[0]
    # if (s2.shock == 1 and s2.noise == 0 and s2.vibration == 0):
    #     print("Test 2: PASSED Be able to correctly update data\n")
    # else:
    #     print("Test 2: FAILED Not be able to update data\n")

    # # Integration Tests
    unittest.main()
