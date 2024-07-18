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

from AddExpensesPage import AddExpensesPage
from IntroPage import IntroPage
from TransactionsPage import TransactionsPage
from MainPage import MainPage

class TransactionsTestCase(unittest.TestCase):

    def setUp(self):
        """
         Configurando testes iniciais.
        """
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Pixel 2 API 30 2',
            'appPackage': 'protect.budgetwatch',
            'appActivity': 'MainActivity',
            'automationName': 'uiautomator2',
            'autoGrantPermissions': 'true',
            'adbExecTimeout': 0,
            'uiautomator2ServerInstallTimeout': 0
        }

        capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
        self.driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)

    def test_create_new_expense(self):
        # Skip da tela de inicialização
        intro_page = IntroPage(self.driver)
        intro_page.click_skip()
        self.driver.implicitly_wait(30)
        # selecionar o item Budget do menu
        main_page = MainPage(self.driver)
        main_page.click_transactions()
        # Clicar para adicionar BUdget
        transaction_page = TransactionsPage(self.driver)
        transaction_page.add_transaction_click()
        add_page = AddExpensesPage(self.driver)
        self.driver.implicitly_wait(30)
        # Inserir os dados de Budget na tela de adicionar
        add_page.type_name("teste")
        add_page.budget_selector_click()
        self.driver.implicitly_wait(30)
        add_page.budget_list_select()
        add_page.type_account("teste1")
        add_page.type_value("100")
        add_page.type_note("teste teste teste teste")
        self.driver.hide_keyboard()
        add_page.date_click()
        add_page.click_save_button()

        #verificação do resultado
        self.assertEqual("Transactions",
                         self.driver.find_element(By.XPATH,
                                                  "(//android.widget.TextView[contains(@text, 'Transactions')])[1]").
                         get_attribute(
                             'text'))

if __name__ == '__main__':
    unittest.main()
