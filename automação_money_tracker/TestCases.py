import os
import unittest
from datetime import date
from datetime import datetime
import time
from datetime import timedelta
from appium import webdriver
from selenium.webdriver import ActionChains
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from Data import TestData
from Reports import Reports
from AddExpensesPage import AddExpensesPage
from EditExpense import EditExpense
from ExclusionExpense import ExclusionExpense
from ValidatorExpense import ExpenseValidator
from ValidadorCategory import CategoryValidator
from ValidadorTitle import TitleValidator
from ReportsSelector import ExpenseListPage
from AddMoreExpenses import AddMoreExpenses
from ValidadorExpense import ValidadorExpense
from ReportsSumary import ReportsSumary


class test_TestCase(unittest.TestCase):

    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "Pixel 2 API 30",
            "appPackage": "com.blogspot.e_kanivets.moneytracker",
            "appActivity": "com.blogspot.e_kanivets.moneytracker.activity.record.MainActivity",
            "automationName": "uiautomator2",
            "autoGrantPermissions": True,
            "adbExecTimeout": 900000,
            "uiautomator2ServerInstallTimeout": 900000
        }

        capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
        self.driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)

        self.add_expenses_page = AddExpensesPage(self.driver)
        self.edit_expense = EditExpense(self.driver)
        self.exclusion_expense = ExclusionExpense(self.driver)
        self.reports_selector = ExpenseListPage(self.driver)
        self.add_more_expenses = AddMoreExpenses(self.driver)
        self.reports_sumary = ReportsSumary(self.driver)
        self.reports = Reports(self.driver)

    def test_expense(self):
        time.sleep(2)
        self.driver.implicitly_wait(5)

        self.reports.click_add_expenses_button()
        self.add_expenses_page.expense_price(TestData.expense_price)
        self.add_expenses_page.expense_title(TestData.expense_title)
        self.add_expenses_page.expense_category(TestData.expense_category)
        self.add_expenses_page.expense_date()
        self.add_expenses_page.expense_confirm_date()
        self.add_expenses_page.expense_time()
        self.add_expenses_page.expense_confirm_time()
        self.add_expenses_page.expense_done_button()

        wait = WebDriverWait(self.driver, 30)

        self.reports_selector.navigate_to_expense_list()

        wait = WebDriverWait(self.driver, 30)
        self.reports_selector.select_day_time_option()

        self.reports_sumary.list_expenses_sumary()

        wait = WebDriverWait(self.driver, 30)

        self.assertEqual("Report",
                         self.driver.find_element(By.XPATH,
                                                  '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]'
                                                  '//android.widget.TextView[contains(@text, "Report")]').
                         get_attribute(
                             'text'))

    def test_expense_more_add(self):
        self.driver.implicitly_wait(5)

        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price2(TestData.expense_price2)
        self.add_more_expenses.expense_title2(TestData.expense_title2)
        self.add_more_expenses.expense_category2(TestData.expense_category2)
        self.add_more_expenses.expense_date2()
        self.add_more_expenses.expense_confirm_date2()
        self.add_more_expenses.expense_time2()
        self.add_more_expenses.expense_confirm_time2()
        self.add_more_expenses.expense_done_button2()

        self.driver.implicitly_wait(5)

        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error(TestData.new_expense_price)
        self.add_more_expenses.expense_title_error(TestData.new_expense_title)
        self.add_more_expenses.expense_category_error(TestData.new_expense_category)
        self.add_more_expenses.expense_date_error()
        self.add_more_expenses.expense_confirm_date_error()
        self.add_more_expenses.expense_time_error()
        self.add_more_expenses.expense_confirm_time_error()
        self.add_more_expenses.expense_done_button_error()

        self.driver.implicitly_wait(5)

        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price3(TestData.expense_price3)
        self.add_more_expenses.expense_title3(TestData.expense_title3)
        self.add_more_expenses.expense_category3(TestData.expense_category3)
        self.add_more_expenses.expense_date3()
        self.add_more_expenses.expense_confirm_date3()
        self.add_more_expenses.expense_time3()
        self.add_more_expenses.expense_confirm_time3()
        self.add_more_expenses.expense_done_button3()

        self.driver.implicitly_wait(5)

        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price4(TestData.expense_price4)
        self.add_more_expenses.expense_title4(TestData.expense_title4)
        self.add_more_expenses.expense_category4(TestData.expense_category4)
        self.add_more_expenses.expense_date4()
        self.add_more_expenses.expense_confirm_date4()
        self.add_more_expenses.expense_time4()
        self.add_more_expenses.expense_confirm_time4()
        self.add_more_expenses.expense_done_button4()

        self.driver.implicitly_wait(10)

        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price_error(TestData.new_expense_price)
        self.add_more_expenses.expense_title_error(TestData.new_expense_title)
        self.add_more_expenses.expense_category_error(TestData.new_expense_category)
        self.add_more_expenses.expense_done_button_error()

        self.driver.implicitly_wait(5)

        self.reports.click_add_expenses_button()
        self.add_more_expenses.expense_price5(TestData.expense_price5)
        self.add_more_expenses.expense_title5(TestData.expense_title5)
        self.add_more_expenses.expense_category5(TestData.expense_category5)
        self.add_more_expenses.expense_date5()
        self.add_more_expenses.expense_confirm_date5()
        self.add_more_expenses.expense_time5()
        self.add_more_expenses.expense_confirm_time5()
        self.add_more_expenses.expense_done_button5()

        wait = WebDriverWait(self.driver, 30)

        self.reports_selector.navigate_to_expense_list()

        wait = WebDriverWait(self.driver, 30)
        self.reports_selector.select_all_time_option()

        wait = WebDriverWait(self.driver, 10)

        self.reports_sumary.list_expenses_sumary()

        wait = WebDriverWait(self.driver, 30)

        self.assertEqual("Report",
                         self.driver.find_element(By.XPATH,
                                                  '//*[@resource-id="com.blogspot.e_kanivets.moneytracker:id/toolbar"]'
                                                  '//android.widget.TextView[contains(@text, "Report")]').
                         get_attribute(
                             'text'))

    def tearDown(self):
        # Teardown
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
