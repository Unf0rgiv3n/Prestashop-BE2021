import time
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys


browser = webdriver.Firefox(executable_path=sys.argv[1])
browser.accept_untrusted_certs = True
browser.implicitly_wait(20)
browser.get('https://localhost/pl/')
numbers = ["1", "2", "3", "1", "2", "3", "1", "2", "3", "6"]

for i in range(1):
	element_to_hover_over = browser.find_element(By.ID, "category-3")
	hover = ActionChains(browser).move_to_element(element_to_hover_over)
	hover.perform()
	browser.find_element(By.ID, "category-5").click()
	navigate = browser.find_element(By.ID, "main")
	navigate = navigate.find_element(By.ID, "products")
	listOfMovies = navigate.find_elements(By.CSS_SELECTOR, ".product")
	listOfMovies[i].click()
	navigate1 = browser.find_element(By.NAME, "qty")
	navigate1.send_keys(Keys.DELETE)
	navigate1.send_keys(numbers[i])
	navigate1.send_keys(Keys.RETURN)
	time.sleep(1)
	navigate2 = browser.find_element(By.CLASS_NAME, "btn-secondary")
	time.sleep(1)
	ActionChains(browser).move_to_element(navigate2).click().pause(1).perform()
	
	
for i in range(1):
	element_to_hover_over = browser.find_element(By.ID, "category-3")
	hover = ActionChains(browser).move_to_element(element_to_hover_over)
	hover.perform()
	browser.find_element(By.ID, "category-6").click()
	navigate = browser.find_element(By.ID, "main")
	navigate = navigate.find_element(By.ID, "products")
	listOfMovies = navigate.find_elements(By.CSS_SELECTOR, ".product")
	listOfMovies[i].click()
	navigate1 = browser.find_element(By.NAME, "qty")
	navigate1.send_keys(Keys.DELETE)
	navigate1.send_keys(numbers[i+7])
	navigate1.send_keys(Keys.RETURN)
	time.sleep(1)
	navigate2 = browser.find_element(By.CLASS_NAME, "btn-secondary")
	time.sleep(1)
	ActionChains(browser).move_to_element(navigate2).click().pause(1).perform()
	
time.sleep(1)

navigate3 = browser.find_element(By.CSS_SELECTOR, ".cart-products-count").click()
time.sleep(1)
navigate4list = browser.find_elements(By.CSS_SELECTOR, ".cart-item")
navigate4 = navigate4list[0].find_element(By.CSS_SELECTOR, ".remove-from-cart").click()
time.sleep(1)

navigate5 = browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
navigate6 = browser.find_element(By.ID, "field-id_gender-2").click()
navigate6 = browser.find_element(By.ID, "field-firstname")
navigate6.send_keys("Draze")
navigate6 = browser.find_element(By.ID, "field-lastname")
navigate6.send_keys("Korsarze")
navigate6 = browser.find_element(By.ID, "field-email")
navigate6.send_keys(sys.argv[2])
navigate6 = browser.find_element(By.ID, "field-password")
navigate6.send_keys("12341234")
navigate6 = browser.find_element(By.NAME, "customer_privacy").click()
navigate6 = browser.find_element(By.ID, "field-password")
navigate6.send_keys(Keys.RETURN)

navigate7 = browser.find_element(By.ID, "field-address1")
navigate7.send_keys("cokolwiek")
navigate7 = browser.find_element(By.ID, "field-postcode")
navigate7.send_keys("00-000")
navigate7 = browser.find_element(By.ID, "field-city")
navigate7.send_keys("tezcokolwiek")
navigate7 = browser.find_element(By.ID, "field-address1")
navigate7.send_keys(Keys.RETURN)
time.sleep(1)

navigate8 = browser.find_element(By.NAME, "confirmDeliveryOption").click()

navigate9 = browser.find_element(By.ID, "payment-option-2").click()
navigate9 = browser.find_element(By.ID, "conditions_to_approve[terms-and-conditions]").click()
time.sleep(1)
navigate9 = browser.find_element(By.ID, "payment-confirmation")
navigate9 = navigate9.find_element(By.TAG_NAME, "button").click()
time.sleep(1)

navigate5 = browser.find_element(By.CSS_SELECTOR, ".account").click()
navigate5 = browser.find_element(By.ID, "history-link").click()
navigate6 = browser.find_element(By.CSS_SELECTOR, "a[data-link-action='view-order-details']").click()
time.sleep(1)
#browser.close()

