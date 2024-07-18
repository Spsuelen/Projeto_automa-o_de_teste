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
from BasePage import BasePage


class AndroidBudget(unittest.TestCase):

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

    # Verifica a adição das informações
    def test_app_budget_add(self):
        self.skipIntro()

        self.home_device()
        self.activate_app()

        self.driver.implicitly_wait(5)

        budget = self.driver.find_element(By.XPATH,
                                          "(//android.widget.TextView[contains(@text, 'Transactions')])[1]")
        budget.click()

        add = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_add"]')
        add.click()

        name = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/nameEdit"]')
        name.send_keys(TestData.budget_type)

        account = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/accountEdit"]')
        account.send_keys(TestData.budget_account)

        value = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/valueEdit"]')
        value.send_keys(TestData.budget_value)

        note = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/noteEdit"]')
        note.send_keys(TestData.budget_note)

        wait = WebDriverWait(self.driver, 10)

        date = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/dateEdit"]')
        date.click()

        confirmar = wait.until(EC.element_to_be_clickable((By.ID, 'android:id/button1')))
        confirmar.click()

        save = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_save"]')
        save.click()

        self.assertEqual("Transactions",
                         self.driver.find_element(By.XPATH,
                                                  "(//android.widget.TextView[contains(@text, 'Transactions')])[1]").
                         get_attribute(
                             'text'))

    # Verifica se o campo Name não aceita valores vazios durante a adição
    def test_app_budget_add_name_empty(self):
        self.skipIntro()

        self.home_device()
        self.activate_app()

        self.driver.implicitly_wait(5)

        budget = self.driver.find_element(By.XPATH,
                                          "(//android.widget.TextView[contains(@text, 'Transactions')])[1]")
        budget.click()

        add = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_add"]')
        add.click()

        name = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/nameEdit"]')
        name.clear()
        name.send_keys(TestData.new_budget_type)

        account = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/accountEdit"]')
        account.send_keys(TestData.budget_account)

        value = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/valueEdit"]')
        value.send_keys(TestData.budget_value)

        note = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/noteEdit"]')
        note.send_keys(TestData.budget_note)

        wait = WebDriverWait(self.driver, 10)

        date = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/dateEdit"]')
        date.click()

        confirmar = wait.until(EC.element_to_be_clickable((By.ID, 'android:id/button1')))
        confirmar.click()

        wait = WebDriverWait(self.driver, 10)

        save = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_save"]')
        save.click()

        self.assertEqual("Transactions",
                         self.driver.find_element(By.XPATH,
                                                  "(//android.widget.TextView[contains(@text, 'Transactions')])[1]").
                         get_attribute(
                             'text'))

    # Verifica se o campo 'Name' contem menos de 2 caracteres durante a adição
    def test_app_budget_add_name_with_minimum_quantity(self):
        self.skipIntro()

        self.home_device()
        self.activate_app()

        self.driver.implicitly_wait(5)

        budget = self.driver.find_element(By.XPATH,
                                          "(//android.widget.TextView[contains(@text, 'Transactions')])[1]")
        budget.click()

        add = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_add"]')
        add.click()

        name = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/nameEdit"]')
        name.clear()
        name.send_keys(TestData.new_budget_type2)

        account = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/accountEdit"]')
        account.send_keys(TestData.budget_account)

        value = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/valueEdit"]')
        value.send_keys(TestData.budget_value)

        note = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/noteEdit"]')
        note.send_keys(TestData.budget_note)

        wait = WebDriverWait(self.driver, 10)

        date = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/dateEdit"]')
        date.click()

        confirmar = wait.until(EC.element_to_be_clickable((By.ID, 'android:id/button1')))
        confirmar.click()

        wait = WebDriverWait(self.driver, 10)

        save = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_save"]')
        save.click()

        self.assertEqual("Transactions",
                         self.driver.find_element(By.XPATH,
                                                  "(//android.widget.TextView[contains(@text, 'Transactions')])[1]").
                         get_attribute(
                             'text'))

    # Verifica se o campo Name contem mais  de 20 caracteres durante a adição
    def test_app_budget_add_name_with_quantity_above_permitted(self):
        self.skipIntro()

        self.home_device()
        self.activate_app()

        self.driver.implicitly_wait(5)

        budget = self.driver.find_element(By.XPATH,
                                          "(//android.widget.TextView[contains(@text, 'Transactions')])[1]")
        budget.click()

        add = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_add"]')
        add.click()

        name = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/nameEdit"]')
        name.clear()
        name.send_keys(TestData.new_budget_type3)

        account = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/accountEdit"]')
        account.send_keys(TestData.budget_account)

        value = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/valueEdit"]')
        value.send_keys(TestData.budget_value)

        note = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/noteEdit"]')
        note.send_keys(TestData.budget_note)

        wait = WebDriverWait(self.driver, 10)

        date = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/dateEdit"]')
        date.click()

        confirmar = wait.until(EC.element_to_be_clickable((By.ID, 'android:id/button1')))
        confirmar.click()

        wait = WebDriverWait(self.driver, 10)

        save = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_save"]')
        save.click()

        self.assertEqual("Transactions",
                         self.driver.find_element(By.XPATH,
                                                  "(//android.widget.TextView[contains(@text, 'Transactions')])[1]").
                         get_attribute(
                             'text'))

    # Verifica se o campo Valor não aceita valores vazios durante a adição
    def test_app_budget_add_value_empty(self):
        self.skipIntro()

        self.home_device()
        self.activate_app()

        self.driver.implicitly_wait(5)

        budget = self.driver.find_element(By.XPATH,
                                          "(//android.widget.TextView[contains(@text, 'Transactions')])[1]")
        budget.click()

        add = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_add"]')
        add.click()

        name = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/nameEdit"]')
        name.send_keys(TestData.budget_type)

        account = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/accountEdit"]')
        account.send_keys(TestData.budget_account)

        value = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/valueEdit"]')
        value.clear()
        value.send_keys(TestData.new_budget_value)

        note = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/noteEdit"]')
        note.send_keys(TestData.budget_note)

        wait = WebDriverWait(self.driver, 10)

        date = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/dateEdit"]')
        date.click()

        confirmar = wait.until(EC.element_to_be_clickable((By.ID, 'android:id/button1')))
        confirmar.click()

        wait = WebDriverWait(self.driver, 10)

        save = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_save"]')
        save.click()

        self.assertEqual("Transactions",
                         self.driver.find_element(By.XPATH,
                                                  "(//android.widget.TextView[contains(@text, 'Transactions')])[1]").
                         get_attribute(
                             'text'))

    # Verifica se o campo Valor aceita somente numeros inteiros durante a adição
    def test_app_budget_add_value_with_integers(self):
        self.skipIntro()

        self.home_device()
        self.activate_app()

        self.driver.implicitly_wait(5)

        budget = self.driver.find_element(By.XPATH,
                                          "(//android.widget.TextView[contains(@text, 'Transactions')])[1]")
        budget.click()

        add = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_add"]')
        add.click()

        name = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/nameEdit"]')
        name.send_keys(TestData.budget_type)

        account = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/accountEdit"]')
        account.send_keys(TestData.budget_account)

        value = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/valueEdit"]')
        value.clear()
        value.send_keys(TestData.new_budget_value2)

        note = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/noteEdit"]')
        note.send_keys(TestData.budget_note)

        wait = WebDriverWait(self.driver, 10)

        date = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/dateEdit"]')
        date.click()

        confirmar = wait.until(EC.element_to_be_clickable((By.ID, 'android:id/button1')))
        confirmar.click()

        wait = WebDriverWait(self.driver, 10)

        save = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_save"]')
        save.click()

        self.assertEqual("Transactions",
                         self.driver.find_element(By.XPATH,
                                                  "(//android.widget.TextView[contains(@text, 'Transactions')])[1]").
                         get_attribute(
                             'text'))

    # Verifica se o campo Valor aceita numeros de até duas casas decimais durante a adição
    def test_app_budget_add_value_with_value_numbers_up_to_2_decimals(self):
        self.skipIntro()

        self.home_device()
        self.activate_app()

        self.driver.implicitly_wait(5)

        budget = self.driver.find_element(By.XPATH,
                                          "(//android.widget.TextView[contains(@text, 'Transactions')])[1]")
        budget.click()

        add = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_add"]')
        add.click()

        name = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/nameEdit"]')
        name.send_keys(TestData.budget_type)

        account = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/accountEdit"]')
        account.send_keys(TestData.budget_account)

        value = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/valueEdit"]')
        value.clear()
        value.send_keys(TestData.new_budget_value3)

        note = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/noteEdit"]')
        note.send_keys(TestData.budget_note)

        wait = WebDriverWait(self.driver, 10)

        date = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/dateEdit"]')
        date.click()

        confirmar = wait.until(EC.element_to_be_clickable((By.ID, 'android:id/button1')))
        confirmar.click()

        wait = WebDriverWait(self.driver, 10)

        save = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_save"]')
        save.click()

        self.assertEqual("Transactions",
                         self.driver.find_element(By.XPATH,
                                                  "(//android.widget.TextView[contains(@text, 'Transactions')])[1]").
                         get_attribute(
                             'text'))

    # Verifica se o campo Conta não aceita valores vazios durante a adição
    def test_app_budget_add_account_empty(self):
        self.skipIntro()

        self.home_device()
        self.activate_app()

        self.driver.implicitly_wait(5)

        budget = self.driver.find_element(By.XPATH,
                                          "(//android.widget.TextView[contains(@text, 'Transactions')])[1]")
        budget.click()

        add = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_add"]')
        add.click()

        name = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/nameEdit"]')
        name.send_keys(TestData.budget_type)

        account = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/accountEdit"]')
        account.clear()
        account.send_keys(TestData.new_budget_account)

        value = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/valueEdit"]')
        value.send_keys(TestData.budget_value)

        note = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/noteEdit"]')
        note.send_keys(TestData.budget_note)

        self.driver.implicitly_wait(10)

        save = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_save"]')
        save.click()

        self.assertEqual("Transactions",
                         self.driver.find_element(By.XPATH,
                                                  "(//android.widget.TextView[contains(@text, 'Transactions')])[1]").
                         get_attribute(
                             'text'))

    # Verifica se o campo Conta contem menos de 3 caracteres durante a adição
    def test_app_budget_add_account_with_minimum_quantity(self):
        self.skipIntro()

        self.home_device()
        self.activate_app()

        self.driver.implicitly_wait(5)

        budget = self.driver.find_element(By.XPATH,
                                          "(//android.widget.TextView[contains(@text, 'Transactions')])[1]")
        budget.click()

        add = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_add"]')
        add.click()

        name = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/nameEdit"]')
        name.send_keys(TestData.budget_type)

        account = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/accountEdit"]')
        account.clear()
        account.send_keys(TestData.new_budget_account2)

        value = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/valueEdit"]')
        value.send_keys(TestData.budget_value)

        note = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/noteEdit"]')
        note.send_keys(TestData.budget_note)

        wait = WebDriverWait(self.driver, 10)

        save = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_save"]')
        save.click()

        self.assertEqual("Transactions",
                         self.driver.find_element(By.XPATH,
                                                  "(//android.widget.TextView[contains(@text, 'Transactions')])[1]").
                         get_attribute(
                             'text'))

    # Verifica se o campo Conta contem mais de 8 caracteres durante a adição
    def test_app_budget_add_account_with_quantity_above_permitted(self):
        self.skipIntro()

        self.home_device()
        self.activate_app()

        self.driver.implicitly_wait(5)

        budget = self.driver.find_element(By.XPATH,
                                          "(//android.widget.TextView[contains(@text, 'Transactions')])[1]")
        budget.click()

        add = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_add"]')
        add.click()

        name = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/nameEdit"]')
        name.send_keys(TestData.budget_type)

        account = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/accountEdit"]')
        account.clear()
        account.send_keys(TestData.new_budget_account3)

        value = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/valueEdit"]')
        value.send_keys(TestData.budget_value)

        note = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/noteEdit"]')
        note.send_keys(TestData.budget_note)

        wait = WebDriverWait(self.driver, 10)

        date = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/dateEdit"]')
        date.click()

        confirmar = wait.until(EC.element_to_be_clickable((By.ID, 'android:id/button1')))
        confirmar.click()

        save = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_save"]')
        save.click()

        self.assertEqual("Transactions",
                         self.driver.find_element(By.XPATH,
                                                  "(//android.widget.TextView[contains(@text, 'Transactions')])[1]").
                         get_attribute(
                             'text'))

    # Verifica se o campo Conta contem  caractere especial "-"
    def test_app_budget_add_account_with_special_character(self):
        self.skipIntro()

        self.home_device()
        self.activate_app()

        self.driver.implicitly_wait(5)

        budget = self.driver.find_element(By.XPATH,
                                          "(//android.widget.TextView[contains(@text, 'Transactions')])[1]")
        budget.click()

        add = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_add"]')
        add.click()

        name = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/nameEdit"]')
        name.send_keys(TestData.budget_type)

        account = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/accountEdit"]')
        account.clear()
        account.send_keys(TestData.new_budget_account4)

        value = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/valueEdit"]')
        value.send_keys(TestData.budget_value)

        note = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/noteEdit"]')
        note.send_keys(TestData.budget_note)

        wait = WebDriverWait(self.driver, 10)

        date = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/dateEdit"]')
        date.click()

        confirmar = wait.until(EC.element_to_be_clickable((By.ID, 'android:id/button1')))
        confirmar.click()

        save = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_save"]')
        save.click()

        self.assertEqual("Transactions",
                         self.driver.find_element(By.XPATH,
                                                  "(//android.widget.TextView[contains(@text, 'Transactions')])[1]").
                         get_attribute(
                             'text'))

    # Verifica se o campo Note não aceita valores vazios durante a adição
    def test_app_budget_add_note_empty(self):
        self.skipIntro()

        self.home_device()
        self.activate_app()

        self.driver.implicitly_wait(5)

        budget = self.driver.find_element(By.XPATH,
                                          "(//android.widget.TextView[contains(@text, 'Transactions')])[1]")
        budget.click()

        add = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_add"]')
        add.click()

        name = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/nameEdit"]')
        name.send_keys(TestData.budget_type)

        account = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/accountEdit"]')
        account.send_keys(TestData.budget_account)

        value = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/valueEdit"]')
        value.send_keys(TestData.budget_value)

        note = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/noteEdit"]')
        note.clear()
        note.send_keys(TestData.new_budget_note)

        wait = WebDriverWait(self.driver, 10)

        date = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/dateEdit"]')
        date.click()

        confirmar = wait.until(EC.element_to_be_clickable((By.ID, 'android:id/button1')))
        confirmar.click()

        wait = WebDriverWait(self.driver, 10)

        save = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_save"]')
        save.click()

        self.assertEqual("Transactions",
                         self.driver.find_element(By.XPATH,
                                                  "(//android.widget.TextView[contains(@text, 'Transactions')])[1]").
                         get_attribute(
                             'text'))

    # Verifica se o campo Note contem mais de 20 caracteres durante a adição
    def test_app_budget_add_note_with_quantity_above_permitted(self):
        self.skipIntro()

        self.home_device()
        self.activate_app()

        self.driver.implicitly_wait(5)

        budget = self.driver.find_element(By.XPATH,
                                          "(//android.widget.TextView[contains(@text, 'Transactions')])[1]")
        budget.click()

        add = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_add"]')
        add.click()

        name = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/nameEdit"]')
        name.send_keys(TestData.budget_type)

        account = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/accountEdit"]')
        account.send_keys(TestData.budget_account)

        value = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/valueEdit"]')
        value.send_keys(TestData.budget_value)

        note = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/noteEdit"]')
        note.clear()
        note.send_keys(TestData.new_budget_note2)

        wait = WebDriverWait(self.driver, 10)

        date = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/dateEdit"]')
        date.click()

        confirmar = wait.until(EC.element_to_be_clickable((By.ID, 'android:id/button1')))
        confirmar.click()

        wait = WebDriverWait(self.driver, 10)

        save = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_save"]')
        save.click()

        self.assertEqual("Transactions",
                         self.driver.find_element(By.XPATH,
                                                  "(//android.widget.TextView[contains(@text, 'Transactions')])[1]").
                         get_attribute(
                             'text'))

    # Verifica se o campo Date aceita datas Futuras
    def test_app_budget_add_date_future(self):
        self.skipIntro()

        self.home_device()
        self.activate_app()

        self.driver.implicitly_wait(5)

        budget = self.driver.find_element(By.XPATH,
                                          "(//android.widget.TextView[contains(@text, 'Transactions')])[1]")
        budget.click()

        add = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_add"]')
        add.click()

        name = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/nameEdit"]')
        name.send_keys(TestData.budget_type)

        account = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/accountEdit"]')
        account.send_keys(TestData.budget_account)

        value = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/valueEdit"]')
        value.send_keys(TestData.budget_value)

        note = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/noteEdit"]')
        note.send_keys(TestData.budget_note)

        wait = WebDriverWait(self.driver, 10)

        date = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/dateEdit"]')
        date.click()

        self.driver.implicitly_wait(5)

        day_element = self.driver.find_element(By.XPATH, '(//android.view.View[@index="29"])[1]')
        day_element.click()

        confirmar = wait.until(EC.element_to_be_clickable((By.ID, 'android:id/button1')))
        confirmar.click()

        wait = WebDriverWait(self.driver, 10)

        save = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_save"]')
        save.click()

        self.driver.implicitly_wait(5)

        selected_date = self.driver.find_element(By.XPATH,
                                                 '//*[@resource-id="protect.budgetwatch:id/dateEdit"]').get_attribute(
            'value')

        self.assertEqual("Transactions",
                         self.driver.find_element(By.XPATH,
                                                  "(//android.widget.TextView[contains(@text, 'Transactions')])[1]").
                         get_attribute(
                             'text'))

    # Verifica o valor do campo Nome apos sua atualização
    def test_app_budget_edit_name(self):
        self.skipIntro()
        self.test_app_budget_add()

        self.driver.implicitly_wait(10)

        budget = self.driver.find_element(By.XPATH, "(//android.widget.TextView[contains(@text, 'Transactions')])[1]")
        budget.click()

        budget_to_edit = self.driver.find_element(By.XPATH, f'//android.widget.TextView'
                                                            f'[contains(@text, "{TestData.budget_type}")]')
        budget_to_edit.click()

        edit = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_edit"]')
        edit.click()

        name = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/nameEdit"]')
        name.clear()
        name.send_keys(TestData.update_budget_type)

        wait = WebDriverWait(self.driver, 10)

        save = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_save"]')
        save.click()

        self.driver.implicitly_wait(10)

        edited_name = self.driver.find_element(By.XPATH, f'//android.widget.TextView'
                                                         f'[contains(@text, "{TestData.update_budget_type}")]')

        self.assertEqual(edited_name.get_attribute('text'), TestData.update_budget_type, "Campo aceito.")

    # Verifica o campo Valor apos sua atualização
    def test_app_budget_edit_value(self):
        self.skipIntro()
        self.test_app_budget_add()

        self.driver.implicitly_wait(10)

        budget = self.driver.find_element(By.XPATH,
                                          "(//android.widget.TextView[contains(@text, 'Transactions')])[1]")
        budget.click()

        budget_to_edit = self.driver.find_element(By.XPATH, f'//android.widget.TextView'
                                                            f'[contains(@text, "{TestData.budget_type}")]')
        budget_to_edit.click()

        edit = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_edit"]')
        edit.click()

        value = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/valueEdit"]')
        value.clear()
        value.send_keys(TestData.update_budget_value)

        wait = WebDriverWait(self.driver, 10)

        save = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_save"]')
        save.click()

        self.driver.implicitly_wait(10)

        edited_value = self.driver.find_element(By.XPATH, f'//android.widget.TextView'
                                                          f'[contains(@text, "{TestData.update_budget_value}")]')

        self.assertEqual(edited_value.get_attribute('text'), TestData.update_budget_value, "Campo aceito.")

    # Verifica o campo Note apos sua atualização
    def test_app_budget_edit_note(self):
        self.skipIntro()
        self.test_app_budget_add()

        self.driver.implicitly_wait(10)

        budget = self.driver.find_element(By.XPATH, "(//android.widget.TextView[contains(@text, 'Transactions')])[1]")
        budget.click()

        budget_to_edit = self.driver.find_element(By.XPATH, f'//android.widget.TextView'
                                                            f'[contains(@text, "{TestData.budget_type}")]')
        budget_to_edit.click()

        edit = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_edit"]')
        edit.click()

        note = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/noteEdit"]')
        note.clear()
        note.send_keys(TestData.update_budget_note)

        save = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_save"]')
        save.click()

        self.driver.implicitly_wait(10)

        edited_note = self.driver.find_element(By.XPATH, f'//android.widget.TextView'
                                                         f'[contains(@text, "{TestData.update_budget_note}")]')

        self.assertEqual(edited_note.get_attribute('text'), TestData.update_budget_note, "Campo aceito.")

    # Verifica o campo Account apos sua atualização
    def test_app_budget_edit_account(self):
        self.skipIntro()
        self.test_app_budget_add()

        self.driver.implicitly_wait(10)

        budget = self.driver.find_element(By.XPATH,
                                          "(//android.widget.TextView[contains(@text, 'Transactions')])[1]")
        budget.click()

        budget_to_edit = self.driver.find_element(By.XPATH, f'//android.widget.TextView'
                                                            f'[contains(@text, "{TestData.budget_type}")]')
        budget_to_edit.click()

        edit = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_edit"]')
        edit.click()

        account = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/accountEdit"]')
        account.clear()
        account.send_keys(TestData.update_budget_account)

        save = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_save"]')
        save.click()

        self.assertEqual("Transactions",
                         self.driver.find_element(By.XPATH,
                                                  "(//android.widget.TextView[contains(@text, 'Transactions')])[1]").
                         get_attribute(
                             'text'))

    # Verifica a exclusao das informações adicionadas
    def test_app_budget_exclusion(self):
        self.skipIntro()
        self.test_app_budget_add()

        self.driver.implicitly_wait(10)
        # clicar em budget
        budget = self.driver.find_element(By.XPATH, "(//android.widget.TextView[contains(@text, 'Transactions')])[1]")
        budget.click()

        budget_to_edit = self.driver.find_element(By.XPATH, f'//android.widget.TextView'
                                                            f'[contains(@text, "{TestData.budget_type}")]')
        budget_to_edit.click()

        wait = WebDriverWait(self.driver, 2)

        edit = self.driver.find_element(By.XPATH, '//*[@resource-id="protect.budgetwatch:id/action_edit"]')
        edit.click()

        options = self.driver.find_element(By.XPATH,
                                           "(//android.widget.ImageView[contains(@content-desc, 'Mais opções')])[1]")
        options.click()

        delete = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Delete')]")
        delete.click()

        wait = WebDriverWait(self.driver, 10)

        confirm = self.driver.find_element(By.ID, "android:id/button1")
        confirm.click()

        self.assertEqual("You don't have any expense transactions at the moment. Click the + (plus) button up top "
                         'to get started.',
                         self.driver.find_element(By.ID, "protect.budgetwatch:id/helpText").get_attribute('text'))

    def skipIntro(self):
        try:
            intro_element = self.wait_for_element(By.XPATH, "//android.widget.TextView"
                                                            "[contains(@text, 'Welcome to Budget Watch')]")
            if intro_element:
                skip_button = self.wait_for_element(By.ID, 'protect.budgetwatch:id/skip', timeout=5)
                skip_button.click()
        except TimeoutException:
            pass

    def landscape_device(self):
        """
          pass
        """
        self.driver.orientation = "LANDSCAPE"

    def portrait_device(self):
        """
          pass
        """
        self.driver.orientation = "PORTRAIT"

    def home_device(self):
        """
         pass
        :return:
        """
        return self.driver.press_keycode(3)

    def back_device(self):
        """
         pass
        :return:
        """
        return self.driver.press_keycode(4)

    def activate_app(self):
        """
          pass
        :return:
        """
        return self.driver.activate_app('protect.budgetwatch')

    def tearDown(self):
        """
             pass
            """
        self.driver.quit()

    def wait_for_element(self, by, value, timeout=1):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            raise TimeoutException(f"Element by {by} with value {value} not found within {timeout} seconds.")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidBudget)
    unittest.TextTestRunner(verbosity=2).run(suite)
