from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from BasePage import BasePage


class ReportsSumary(BasePage):
    expenses_reports = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/recyclerView')
    list_expenses_sumary_locator = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                              'android.widget.FrameLayout/'
                                              'android.widget.LinearLayout/'
                                              'android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/'
                                              'android.view.ViewGroup/'
                                              'android.widget.LinearLayout[2]/'
                                              'androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/'
                                              'android.widget.FrameLayout/'
                                              'android.widget.LinearLayout/'
                                              'android.widget.LinearLayout[1]/android.widget.LinearLayout/'
                                              'android.widget.TextView[1]')

    def navigate_to_list_page_selector(self):
        wait = WebDriverWait(self.driver, 30)
        list_expenses_reports = wait.until(EC.element_to_be_clickable(self.expenses_reports))
        list_expenses_reports.click()

    def list_expenses_sumary(self):
        wait = WebDriverWait(self.driver, 30)
        list_expenses_sumary_locator = wait.until(EC.element_to_be_clickable(self.list_expenses_sumary_locator))
        list_expenses_sumary_locator.click()
