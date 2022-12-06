from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from subprocess import Popen

url = "https://www.franchiseball.com"
login_email = ""
login_password = ""

# driver initialization
service = Service('chromedriver')
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path = "./chromedriver.exe",options=chrome_options)

# go to website.
driver.get(url)
print("LOG: Go to FranchiseBall.")

# try to login.
username = driver.find_element("id","login_email")
password = driver.find_element("id","login_password")

username.send_keys(login_email)
password.send_keys(login_password)

driver.find_element('id',"submit").click()


# import player list from text file.
data = open('list.txt', 'r')
playerList = data.readlines()

for playerUrl in playerList:
	try:
		driver.get(playerUrl)
		WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "player-bid-button"))).click()
		WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "bid_submit"))).click()
		WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "bid_confirm_button"))).click()
		print('Bid submitted.')
	except Exception as inst:
		print("Something wrong with this player: " + playerUrl)
print('Completed')