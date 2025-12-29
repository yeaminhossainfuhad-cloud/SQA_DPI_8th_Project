from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_download_resume():
    driver = webdriver.Chrome()

    # Open Portfolio site
    driver.get("https://yhf-cs.vercel.app/")
    driver.maximize_window()

    time.sleep(3)

    resume = driver.find_element(By.XPATH, "/html/body/section[1]/div/div/div[2]/a[2]")
    resume.click()

    time.sleep(10)
    driver.quit()