import undetected_chromedriver as webdriver
from selenium.webdriver.common.by import By
import argparse
import os
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument('passcode', metavar='P', type=int, nargs='?')

args = parser.parse_args()

PASSCODE = args.passcode
if PASSCODE is None:
    raise Exception("2FA passcode is required")

driver = webdriver.Chrome(use_subprocess=True)
driver.get(os.getenv('MYWORKSPACE_URL'))

driver.find_element(By.ID, "login").send_keys(os.getenv('USER_NAME'))
driver.find_element(By.ID, "passwd1").send_keys(os.getenv('PASSWORD'))
driver.find_element(By.ID, "passwd").send_keys(PASSCODE)
driver.find_element(By.ID, "loginBtn").click()

while True:
    pass