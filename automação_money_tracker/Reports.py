from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from BasePage import BasePage


class Reports(BasePage):
    expenses_reports_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/recyclerView')
    #list_expenses_button_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/spinner')
    add_expenses_button_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/btnAddExpense')

    def navigate(self):
        wait = WebDriverWait(self.driver, 20)
        expenses_reports = wait.until(EC.presence_of_element_located(self.expenses_reports_locator))


    def navigate_to_list_page(self):
        wait = WebDriverWait(self.driver, 20)
        list_expenses_reports_locator = wait.until(EC.element_to_be_clickable(self.expenses_reports_locator))
        list_expenses_reports_locator.click()

    def click_add_expenses_button(self):
        wait = WebDriverWait(self.driver, 20)
        add_expenses_button_locator = wait.until(EC.element_to_be_clickable(self.add_expenses_button_locator))
        add_expenses_button_locator.click()
