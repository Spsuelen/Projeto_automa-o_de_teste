from appium.webdriver.common.appiumby import By
from BasePage import BasePage


class MainPage(BasePage):
    budget = self.driver.find_element(By.XPATH,
                                      "(//android.widget.TextView[contains(@text, 'Transactions')])[1]")

    def click_budget(self):
        budget_option = self.driver.find_element(*MainPage.budget)
        budget_option.click()
