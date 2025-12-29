from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_linkedin():
    driver = webdriver.Chrome()

    # Open Portfolio site
    driver.get("https://yhf-cs.vercel.app/")
    driver.maximize_window()

    time.sleep(3)

    getintouch_btn = driver.find_element(By.XPATH, "/html/body/section[1]/div/div/div[2]/a[1]")
    getintouch_btn.click()

    get = driver.find_element(By.XPATH, "/html/body/section[6]/div/div[2]/div/h3")
    assert get.text == "Get In Touch"
    time.sleep(2)

    linkedin_btn = driver.find_element(By.XPATH, "/html/body/section[6]/div/div[2]/div/div[4]/a[1]")
    linkedin_btn.click()
    time.sleep(5)

    linkedin = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[1]/span/a/h1")
    assert linkedin.text == "Md Yeamin Hossain Fuhad"
    time.sleep(5)

    driver.quit()


def test_github():
    driver = webdriver.Chrome()

    # Open Portfolio site
    driver.get("https://yhf-cs.vercel.app/")
    driver.maximize_window()

    time.sleep(3)

    getintouch_btn = driver.find_element(By.XPATH, "/html/body/section[1]/div/div/div[2]/a[1]")
    getintouch_btn.click()

    get = driver.find_element(By.XPATH, "/html/body/section[6]/div/div[2]/div/h3")
    assert get.text == "Get In Touch"
    time.sleep(2)

    github_btn = driver.find_element(By.XPATH, "/html/body/section[6]/div/div[2]/div/div[4]/a[2]")
    github_btn.click()
    time.sleep(5)

    driver.quit()


def test_facebook():
    driver = webdriver.Chrome()

    # Open Portfolio site
    driver.get("https://yhf-cs.vercel.app/")
    driver.maximize_window()

    time.sleep(3)

    getintouch_btn = driver.find_element(By.XPATH, "/html/body/section[1]/div/div/div[2]/a[1]")
    getintouch_btn.click()

    get = driver.find_element(By.XPATH, "/html/body/section[6]/div/div[2]/div/h3")
    assert get.text == "Get In Touch"
    time.sleep(2)

    fb_btn = driver.find_element(By.XPATH, "/html/body/section[6]/div/div[2]/div/div[4]/a[3]")
    fb_btn.click()
    time.sleep(5)

    cross_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div")
    cross_btn.click()
    time.sleep(5)

    driver.quit()