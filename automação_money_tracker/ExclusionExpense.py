from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time
from BasePage import BasePage
from Data import TestData


class ExclusionExpense(BasePage):
    reports_title_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/textViewRecords')
    expense_delete_button_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/action_delete')

    def delete_expense(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(ExclusionExpense.expense_delete_button_locator))

        expense_delete_button = self.driver.find_element(*ExclusionExpense.expense_delete_button_locator)
        expense_delete_button.click()

        wait.until_not(EC.visibility_of_element_located(ExclusionExpense.expense_delete_button_locator))
