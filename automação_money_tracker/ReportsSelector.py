import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from BasePage import BasePage


class ExpenseListPage(BasePage):
    expenses_reports = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/recyclerView')
    list_expenses_button_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/spinner')
    all_time_option_locator = (By.XPATH,
                               '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
                               'android.widget.ListView/android.widget.TextView[5]')
    day_time_option_locator = (By.XPATH,
                               '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
                               'android.widget.ListView/android.widget.TextView[1]')

    def navigate_to_list_page_selector(self):
        wait = WebDriverWait(self.driver, 10)
        list_expenses_reports = wait.until(EC.element_to_be_clickable(self.expenses_reports))
        list_expenses_reports.click()

    def navigate_to_expense_list(self):
        wait = WebDriverWait(self.driver, 30)
        list_expenses_button_locator = wait.until(EC.element_to_be_clickable(self.list_expenses_button_locator))
        list_expenses_button_locator.click()

    def select_day_time_option(self):
        wait = WebDriverWait(self.driver, 30)
        day_time_option_locator = wait.until(EC.element_to_be_clickable(self.day_time_option_locator))
        day_time_option_locator.click()

    def select_all_time_option(self):
        wait = WebDriverWait(self.driver, 30)
        all_time_option_locator = wait.until(EC.element_to_be_clickable(self.all_time_option_locator))
        all_time_option_locator.click()
