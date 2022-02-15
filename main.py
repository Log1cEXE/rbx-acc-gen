import selenium
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
f = open("D:\\generated_accounts.txt","a")

for i in range(15):
    driver.get("https://www.roblox.com")

    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/section/div/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/div/div/div[1]/select")))
    except:
        pass

    # --
    element = driver.find_element_by_xpath("/html/body/div[4]/div/div/section/div/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/div/div/div[1]/select")
    drp=Select(element)

    drp.select_by_visible_text("February")

    # --
    element = driver.find_element_by_xpath("/html/body/div[4]/div/div/section/div/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/div/div/div[2]/select")
    drp=Select(element)

    drp.select_by_visible_text("02")
    # --
    element = driver.find_element_by_xpath("/html/body/div[4]/div/div/section/div/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/div/div/div[3]/select")
    drp=Select(element)

    drp.select_by_visible_text("2000")

    # -----
    keyword = "invisible"
    random_username = keyword + str(random.randint(22222,55555))
    random_password = keyword + str(random.randint(22222,55555))


    f.write(random_username + ":" + random_password + "\n")

    username_field = driver.find_element_by_xpath("/html/body/div[4]/div/div/section/div/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/div[3]/input")
    username_field.send_keys(random_username)

    password_field = driver.find_element_by_xpath("/html/body/div[4]/div/div/section/div/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/div[4]/input")
    password_field.send_keys(random_password)

    # ---

    gender_field = driver.find_element_by_xpath("/html/body/div[4]/div/div/section/div/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/div[5]/div/div/button[2]")
    gender_field.click()

    # ---

    sign_button = driver.find_element_by_xpath("/html/body/div[4]/div/div/section/div/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/button")
    sign_button.click()
    time.sleep(0.5)
    sign_button.click()

#    time.sleep(20)
    try:
        WebDriverWait(driver, 80).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div[1]/div[1]/div/div[2]/div[2]/ul/li[4]/span/span[1]")))
    except:
        pass

    settings_btn = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/div/div[2]/div[2]/ul/li[4]/span/span[1]")
    settings_btn.click()

    logout_btn = driver.find_element_by_xpath("/html/body/div[21]/div[2]/div/ul/li[4]/a")
    logout_btn.click()

    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[22]/div[2]/div/div/div[3]/div/button[2]")))
    except:
        pass

    accept_risk = driver.find_element_by_xpath("/html/body/div[22]/div[2]/div/div/div[3]/div/button[2]")
    accept_risk.click()

#    time.sleep(1)
    driver.get("https://www.roblox.com")

#    time.sleep(2.5)
