import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Firefox
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui

def zabezpieczeniaFirefox():
    time.sleep(2)
    elements = driver.find_elements(By.ID, "advancedButton")
    for e in elements:
        e.click()
    elements = driver.find_elements(By.ID, "exceptionDialogButton")
    for e in elements:
        e.click()

def zabezpieczeniaChrome():
    time.sleep(2)
    elements = driver.find_elements(By.ID, "details-button")
    for e in elements:
        e.click()
    elements = driver.find_elements(By.ID, "proceed-link")
    for e in elements:
        e.click()

profile = Options()
profile.set_preference("security.insecure_field_warning.contextual.enabled", False)
profile.set_preference("security.insecure_field_warning.ignore_local_ip_address", False)

# driver = Firefox(options=profile)
#driver = Firefox(executable_path=GeckoDriverManager().install(), options=profile)
driver = webdriver.Chrome()
driver.set_window_size(1700, 2000)
driver.get("https://localhost/admin-cinema/")
zabezpieczeniaChrome()
driver.find_element(By.ID, "email").send_keys("admin@admin.pl")
driver.find_element(By.ID, "passwd").send_keys("znVesDkY6f4Phpf" + Keys.ENTER)


timeout = 100
element_present = EC.presence_of_element_located((By.ID, 'subtab-AdminImport'))
WebDriverWait(driver, timeout).until(element_present)
#driver.find_element(By.ID, 'nav-sidebar').send_keys(Keys.PAGE_DOWN)
#driver.find_element(By.CLASS_NAME, 'btn -small btn-main btn-sm onboarding-button-stop').click()
elements = driver.find_elements(By.TAG_NAME, 'span')
for e in elements:
    if e.text == "Advanced Parameters":
        e.click()
        break
time.sleep(1)
driver.find_element(By.ID, 'subtab-AdminImport').click()
element_present = EC.presence_of_element_located((By.ID, 'file'))
WebDriverWait(driver, timeout).until(element_present)
driver.find_element(By.ID, 'entity').send_keys('Products')
#driver.file_detector.is_local_file()
driver.find_element(By.ID, 'file').send_keys('/home/slimi/Downloads/multikino.csv')
time.sleep(1)
"""
downloadsButton = pyautogui.locateOnScreen('helpers/downloads.png')
buttonx, buttony = pyautogui.center(downloadsButton)
pyautogui.click(buttonx, buttony)
searchButton = pyautogui.locateOnScreen('helpers/search1.png')
buttonx, buttony = pyautogui.center(searchButton)
pyautogui.click(buttonx, buttony)
time.sleep(1)
pyautogui.write('multikino.csv', interval=0.01)
pyautogui.press(Keys.ENTER)
"""
