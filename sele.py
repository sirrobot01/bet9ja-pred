from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


driver  = webdriver.Firefox()


driver.get('https://mobile.bet9ja.com/mobile#/login')

username = driver.find_element_by_css_selector('input.credentials__input:nth-child(1)')
username.clear()
username.send_keys('cypher01')


password = driver.find_element_by_css_selector('input.credentials__input:nth-child(2)')
password.clear()
password.send_keys('')

driver.find_element_by_css_selector('.btn').click()
driver.implicitly_wait(10)

#reload_the_pag
#Clicks


time.sleep(5)

driver.refresh()

time.sleep(5)

driver.find_element_by_css_selector('#iconslider_1549_league_link > i:nth-child(1)').click()
driver.find_element_by_css_selector('div.col-xs-6:nth-child(1) > div:nth-child(1) > div:nth-child(2)').click()
time.sleep(5)
'''try:
    time.sleep(10)
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#results > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > a:nth-child(1) > i:nth-child(1)')))
finally:'''

time.sleep(10)
driver.find_element_by_css_selector(
    '#bet > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > a:nth-child(1) > i:nth-child(1)').click()
driver.find_element_by_css_selector('#a_bet_results').click()

#'#bets-time-betContdown'
for i in range(500):
    new = open('downloads/'+str(i)+'.html', 'w')
    time.sleep(10)
    new.write(str(driver.page_source))
    time.sleep(80)
    driver.refresh()
