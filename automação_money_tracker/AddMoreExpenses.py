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


class AddMoreExpenses(BasePage):
    expense_price_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/etPrice')
    expense_title_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/etTitle')
    expense_category_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/etCategory')
    expense_date_locator = (By.ID, "com.blogspot.e_kanivets.moneytracker:id/tvDate")
    expense_confirm_date_locator = (By.ID, 'android:id/button1')
    expense_time_locator = (By.ID, "com.blogspot.e_kanivets.moneytracker:id/tvTime")
    expense_confirm_time_locator = (By.ID, 'android:id/button1')
    expense_done_button_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/fabDone')

    # Segunda adição de Informações
    def expense_price2(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_price = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_price_locator))
        expense_price.send_keys(TestData.expense_price2)
        ExpenseValidator.validate_price(TestData.expense_price2)

    def expense_title2(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_title = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_title_locator))
        expense_title.send_keys(TestData.expense_title2)

    def expense_category2(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_category = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_category_locator))
        expense_category.send_keys(TestData.expense_category2)

    def expense_date2(self):
        wait = WebDriverWait(self.driver, 10)
        current_date = TestData.date
        expense_date_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
        expense_date_element = wait.until(EC.element_to_be_clickable(expense_date_locator))
        expense_date_element.click()

    def expense_confirm_date2(self):
        wait = WebDriverWait(self.driver, 10)
        expense_confirm_date_locator = (By.ID, 'android:id/button1')
        expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
        expense_confirm_date_locator.click()

    def expense_time2(self):
        wait = WebDriverWait(self.driver, 10)
        current_time = datetime.now().strftime('%H:%M')
        expense_time_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTime')
        expense_time_locator = wait.until(EC.element_to_be_clickable(expense_time_locator))
        expense_time_locator.click()

    def expense_confirm_time2(self):
        wait = WebDriverWait(self.driver, 10)
        expense_confirm_date_locator = (By.ID, 'android:id/button1')
        expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
        expense_confirm_date_locator.click()

    def expense_done_button2(self):
        wait = WebDriverWait(self.driver, 10)
        expense_done_button = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_done_button_locator))
        expense_done_button.click()

    # Terceira adição de Informações
    def expense_price3(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_price = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_price_locator))
        expense_price.send_keys(TestData.expense_price3)
        ExpenseValidator.validate_price(TestData.expense_price3)

    def expense_title3(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_title = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_title_locator))
        expense_title.send_keys(TestData.expense_title3)

    def expense_category3(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_category = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_category_locator))
        expense_category.send_keys(TestData.expense_category3)

    def expense_date3(self):
        wait = WebDriverWait(self.driver, 10)
        current_date = TestData.date
        expense_date_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
        expense_date_element = wait.until(EC.element_to_be_clickable(expense_date_locator))
        expense_date_element.click()

    def expense_confirm_date3(self):
        wait = WebDriverWait(self.driver, 10)
        expense_confirm_date_locator = (By.ID, 'android:id/button1')
        expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
        expense_confirm_date_locator.click()

    def expense_time3(self):
        wait = WebDriverWait(self.driver, 10)
        current_time = datetime.now().strftime('%H:%M')
        expense_time_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTime')
        expense_time_locator = wait.until(EC.element_to_be_clickable(expense_time_locator))
        expense_time_locator.click()

    def expense_confirm_time3(self):
        wait = WebDriverWait(self.driver, 10)
        expense_confirm_date_locator = (By.ID, 'android:id/button1')
        expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
        expense_confirm_date_locator.click()

    def expense_done_button3(self):
        wait = WebDriverWait(self.driver, 10)
        expense_done_button = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_done_button_locator))
        expense_done_button.click()

    # Quarta adição de Informações
    def expense_price4(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_price = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_price_locator))
        expense_price.send_keys(TestData.expense_price4)
        ExpenseValidator.validate_price(TestData.expense_price4)

    def expense_title4(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_title = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_title_locator))
        expense_title.send_keys(TestData.expense_title4)

    def expense_category4(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_category = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_category_locator))
        expense_category.send_keys(TestData.expense_category4)

    def expense_date4(self):
        wait = WebDriverWait(self.driver, 10)
        current_date = TestData.date
        expense_date_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
        expense_date_element = wait.until(EC.element_to_be_clickable(expense_date_locator))
        expense_date_element.click()

    def expense_confirm_date4(self):
        wait = WebDriverWait(self.driver, 10)
        expense_confirm_date_locator = (By.ID, 'android:id/button1')
        expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
        expense_confirm_date_locator.click()

    def expense_time4(self):
        wait = WebDriverWait(self.driver, 10)
        current_time = datetime.now().strftime('%H:%M')
        expense_time_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTime')
        expense_time_locator = wait.until(EC.element_to_be_clickable(expense_time_locator))
        expense_time_locator.click()

    def expense_confirm_time4(self):
        wait = WebDriverWait(self.driver, 10)
        expense_confirm_date_locator = (By.ID, 'android:id/button1')
        expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
        expense_confirm_date_locator.click()

    def expense_done_button4(self):
        wait = WebDriverWait(self.driver, 10)
        expense_done_button = wait.until(
            EC.presence_of_element_located(AddMoreExpenses.expense_done_button_locator))
        expense_done_button.click()

    # Quinta adição de Informações
    def expense_price5(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_price = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_price_locator))
        expense_price.send_keys(TestData.expense_price5)
        ExpenseValidator.validate_price(TestData.expense_price5)

    def expense_title5(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_title = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_title_locator))
        expense_title.send_keys(TestData.expense_title5)

    def expense_category5(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_category = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_category_locator))
        expense_category.send_keys(TestData.expense_category5)

    def expense_date5(self):
        wait = WebDriverWait(self.driver, 10)
        current_date = TestData.date
        expense_date_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
        expense_date_element = wait.until(EC.element_to_be_clickable(expense_date_locator))
        expense_date_element.click()

    def expense_confirm_date5(self):
        wait = WebDriverWait(self.driver, 10)
        expense_confirm_date_locator = (By.ID, 'android:id/button1')
        expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
        expense_confirm_date_locator.click()

    def expense_time5(self):
        wait = WebDriverWait(self.driver, 10)
        current_time = datetime.now().strftime('%H:%M')
        expense_time_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTime')
        expense_time_locator = wait.until(EC.element_to_be_clickable(expense_time_locator))
        expense_time_locator.click()

    def expense_confirm_time5(self):
        wait = WebDriverWait(self.driver, 10)
        expense_confirm_date_locator = (By.ID, 'android:id/button1')
        expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
        expense_confirm_date_locator.click()

    def expense_done_button5(self):
        wait = WebDriverWait(self.driver, 15)
        expense_done_button = wait.until(
            EC.presence_of_element_located(AddMoreExpenses.expense_done_button_locator))
        expense_done_button.click()

    # Adicionando Informações Incorretas
    def expense_price_error(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_price = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_price_locator))
        expense_price.send_keys(TestData.new_expense_price)
        ExpenseValidator.validate_price(TestData.new_expense_price)

    def expense_title_error(self, text):
        wait = WebDriverWait(self.driver, 10)
        expense_title = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_title_locator))
        expense_title.send_keys(TestData.new_expense_title)

    def expense_category_error(self, text):
        wait = WebDriverWait(self.driver, 15)
        expense_category = wait.until(EC.presence_of_element_located(AddMoreExpenses.expense_category_locator))
        expense_category.send_keys(TestData.new_expense_category)

    def expense_date_error(self):
        wait = WebDriverWait(self.driver, 15)
        current_date = TestData.date
        expense_date_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvDate')
        expense_date_element = wait.until(EC.element_to_be_clickable(expense_date_locator))
        expense_date_element.click()

    def expense_confirm_date_error(self):
        wait = WebDriverWait(self.driver, 15)
        expense_confirm_date_locator = (By.ID, 'android:id/button1')
        expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
        expense_confirm_date_locator.click()

    def expense_time_error(self):
        wait = WebDriverWait(self.driver, 15)
        current_time = datetime.now().strftime('%H:%M')
        expense_time_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/tvTime')
        expense_time_locator = wait.until(EC.element_to_be_clickable(expense_time_locator))
        expense_time_locator.click()

    def expense_confirm_time_error(self):
        wait = WebDriverWait(self.driver, 15)
        expense_confirm_date_locator = (By.ID, 'android:id/button1')
        expense_confirm_date_locator = wait.until(EC.element_to_be_clickable(expense_confirm_date_locator))
        expense_confirm_date_locator.click()

    def expense_done_button_error(self):
        wait = WebDriverWait(self.driver, 20)
        expense_done_button = wait.until(
            EC.presence_of_element_located(AddMoreExpenses.expense_done_button_locator))
        expense_done_button.click()

