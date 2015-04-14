import urllib, os

from pyvirtualdisplay import Display

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Firefox()

driver.get("http://www.google.com")
#try:
#    element = WebDriverWait(driver, 10).until(
#        EC.presence_of_element_located((By.CSS_SELECTOR, ".list_comm > ul > li"))
#    )
#finally:
#    html = driver.page_source
driver.quit()
display.stop()
