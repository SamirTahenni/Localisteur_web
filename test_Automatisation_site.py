import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import requests
from bs4 import BeautifulSoup

# Remplir le fichier de recherche
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.github.com")
driver.maximize_window()
#driver.implicitly_wait(20)

driver.find_element(By.XPATH,"//a[@href ='/login']").click()
time.sleep(3)
driver.find_element(By.ID,"login_field").send_keys('samitahenni@live.fr')
time.sleep(3)
driver.find_element(By.ID,"password").send_keys('Azertyuiopsam1985')
time.sleep(3)
driver.find_element(By.NAME,"commit").click()
driver.find_element(By.XPATH,"(//a[@href ='/SamirTahenni/Localisteur_web'])[2]").click()
time.sleep(3)
