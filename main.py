# SeleniumとChromedriverをpipでインストールしておく
from selenium import webdriver
import chromedriver_binary
import time
import random

body_temp = str(36 + random.randint(1,7)/10)
url = 'https://docs.google.com/forms/d/e/1FAIpQLScGgZ8dsBkcSVutvW3JgDLqy3pIEKk12ucjiA8mNQrKopILog/viewform?usp=pp_url&entry.1534939278=荒川智則&entry.511939456='+body_temp

# クリックの関数
def click(xpath):
    driver.find_element_by_xpath(xpath).click()

# パスワード入力の関数
def insert_pw(xpath, str):
    driver.find_element_by_xpath(xpath).send_keys(str)

driver = webdriver.Chrome()
driver.implicitly_wait(1)
driver.get(url)

moving_login_button = '/html/body/div[2]/div/div[2]/div[3]/div[2]'
time.sleep(1)

# Googleアカウントでのログインが必要な場合はログインする
if(driver.find_elements_by_xpath(moving_login_button) != []):
  click(moving_login_button)
  login_id = "{Googleアカウントのメアド}"
  login_id_xpath = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input'
  login_id_button = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div'
  insert_pw(login_id_xpath, login_id)
  click(login_id_button)
  time.sleep(1)
  login_pw = "{Googleアカウントのパスワード}"
  login_pw_xpath = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input'
  login_pw_button = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div'
  insert_pw(login_pw_xpath, login_pw)
  time.sleep(1)
  click(login_pw_button)

time.sleep(1)
submit_button = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div'
click(submit_button)

print("Done!")

driver.close
# メモリーを食い散らかすのでちゃんと終了しましょう
driver.quit
