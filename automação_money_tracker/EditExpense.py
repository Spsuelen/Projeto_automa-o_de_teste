from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from datetime import datetime
import time
from BasePage import BasePage
from ValidatorExpense import ExpenseValidator
from ValidadorCategory import CategoryValidator
from ValidadorTitle import TitleValidator
from Data import TestData




class EditExpense(BasePage):
    expense_price_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/etPrice')
    expense_done_button_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/fabDone')
    reports_title_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/textViewRecords')

    def edit_specific_expense(self, new_price):
        time.sleep(2)
        expense_price = self.driver.find_element(*EditExpense.expense_price_locator)
        expense_price.clear()
        expense_price.send_keys(new_price)

        expense_done_button = self.driver.find_element(*EditExpense.expense_done_button_locator)
        expense_done_button.click()

        ExpenseValidator.validate_price(new_price)

        time.sleep(2)

        wait = WebDriverWait(self.driver, 10)

        wait.until_not(EC.visibility_of_element_located(EditExpense.expense_done_button_locator))
