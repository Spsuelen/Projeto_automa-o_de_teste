from datetime import date
from datetime import datetime
import time
from datetime import timedelta
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BasePage import BasePage
from ValidatorExpense import ExpenseValidator
from ValidadorCategory import CategoryValidator
from ValidadorTitle import TitleValidator
from Data import TestData


class AddExpensesPage(BasePage):

    expense_price_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/etPrice')
    expense_title_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/etTitle')
    expense_category_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/etCategory')
    expense_date_locator = (By.ID, "com.blogspot.e_kanivets.moneytracker:id/tvDate")
    expense_confirm_date_locator = (By.ID, 'android:id/button1')
    expense_time_locator = (By.ID, "com.blogspot.e_kanivets.moneytracker:id/tvTime")
    expense_confirm_time_locator = (By.ID, 'android:id/button1')
    expense_done_button_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/fabDone')

    def expense_price(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_price = wait.until(EC.presence_of_element_located(AddExpensesPage.expense_price_locator))
        expense_price.send_keys(TestData.expense_price)
        ExpenseValidator.validate_price(TestData.expense_price)

    def expense_title(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_title = wait.until(EC.presence_of_element_located(AddExpensesPage.expense_title_locator))
        expense_title.send_keys(TestData.expense_title)

    def expense_category(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_category = wait.until(EC.presence_of_element_located(AddExpensesPage.expense_category_locator))
        expense_category.send_keys(TestData.expense_category)

    def expense_account(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_account = wait.until(EC.presence_of_element_located(AddExpensesPage.expense_account_locdator))
        expense_account.send_keys(TestData.expense_account)

    def expense_date(self):
        wait = WebDriverWait(self.driver, 10)
        current_date = TestData.date
        expense_date_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
        expense_date_element = wait.until(EC.element_to_be_clickable(expense_date_locator))
        expense_date_element.click()

    def expense_confirm_date(self):
        wait = WebDriverWait(self.driver, 10)
        expense_confirm_date_locator = (By.ID, 'android:id/button1')
        expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
        expense_confirm_date_locator.click()

    def expense_time(self):
        wait = WebDriverWait(self.driver, 10)
        current_time = datetime.now().strftime('%H:%M')
        expense_time_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTime')
        expense_time_locator = wait.until(EC.element_to_be_clickable(expense_time_locator))
        expense_time_locator.click()

    def expense_confirm_time(self):
        wait = WebDriverWait(self.driver, 10)
        expense_confirm_date_locator = (By.ID, 'android:id/button1')
        expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
        expense_confirm_date_locator.click()

    def expense_done_button(self):
        wait = WebDriverWait(self.driver, 10)
        expense_done_button = wait.until(EC.presence_of_element_located(AddExpensesPage.expense_done_button_locator))
        expense_done_button.click()






