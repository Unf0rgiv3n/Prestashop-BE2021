import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Firefox
from webdriver_manager.firefox import GeckoDriverManager
import pyautogui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import csv


def zabezpieczenia():
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
driver = Firefox(executable_path=GeckoDriverManager().install(), options=profile)
#driver = webdriver.Chrome()
driver.set_window_size(1700, 2000)
driver.get("https://localhost/admin-cinema/")
driver.find_element(By.ID, "email").send_keys("admin@admin.pl")
driver.find_element(By.ID, "passwd").send_keys("znVesDkY6f4Phpf" + Keys.ENTER)
zabezpieczenia()

timeout = 100
element_present = EC.presence_of_element_located((By.ID, 'subtab-AdminImport'))
WebDriverWait(driver, timeout).until(element_present)
elements = driver.find_elements(By.TAG_NAME, 'span')
for e in elements:
    if e.text == "Catalog":
        e.click()
        break
driver.find_element(By.ID, "subtab-AdminProducts").click()
element_present = EC.presence_of_element_located((By.ID, 'page-header-desc-configuration-add'))
WebDriverWait(driver, timeout).until(element_present)
driver.find_element(By.ID, "page-header-desc-configuration-add").click()

with open('multikino.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='|')
    line_count = 0
    for row in csv_reader:
        element_present = EC.presence_of_element_located((By.ID, 'product_form_save_new_btn'))
        WebDriverWait(driver, timeout).until(element_present)
        if line_count != 0:
            time.sleep(1)
            driver.find_element(By.ID, "form_step1_name_1").send_keys(f'{row[0]}')
            driver.find_element(By.ID, "form_step6_reference").send_keys(f'{row[0]}')
            driver.find_element(By.ID, "form_step1_qty_0_shortcut").send_keys("100")
            driver.find_element(By.ID, "form_step1_description_1_ifr").send_keys(f' {row[1]}')
            driver.find_element(By.ID, "form_step1_price_ttc_shortcut").send_keys(f'{row[2]}')
            time.sleep(10)
            """
            driver.find_element(By.ID, "product-images-dropzone").click()
            downloadsButton = pyautogui.locateOnScreen('helpers/downloads.png')
            if downloadsButton is not None:
                buttonx, buttony = pyautogui.center(downloadsButton)
                pyautogui.click(buttonx, buttony)
            searchButton = pyautogui.locateOnScreen('helpers/search1.png')
            buttonx, buttony = pyautogui.center(searchButton)
            pyautogui.click(buttonx, buttony)
            time.sleep(1)
            #pyautogui.write(f'{row[3]}', interval=0.01)
            pyautogui.write('7972251.3.jpg', interval=0.01)
            pyautogui.moveTo(buttonx, buttony)
            pyautogui.move(-200, 100)
            pyautogui.doubleClick()
            """
            driver.find_element(By.ID, "product_form_save_new_btn").click()
            time.sleep(2)
        line_count += 1
