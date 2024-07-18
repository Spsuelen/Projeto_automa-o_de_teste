from appium.webdriver.common.appiumby import By
from selenium.webdriver import ActionChains
from BasePage import BasePage


class MainPage(BasePage):
    budget_option_locator = (By.XPATH, "//android.widget.TextView[contains(@text, 'Budgets')]")
    transactions_option_location = (By.XPATH, "//android.widget.TextView[contains(@text, 'Transactions')]")

    def click_budget(self):
        budget_option = self.driver.find_element(*MainPage.budget_option_locator)
        budget_option.click()

    def click_transactions(self):
        transactions_option = self.driver.find_element(*MainPage.transactions_option_location)
        transactions_option.click()
