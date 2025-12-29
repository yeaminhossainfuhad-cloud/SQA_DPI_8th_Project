from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_linkedin():
    driver = webdriver.Chrome()

    # Open Portfolio site
    driver.get("https://yhf-cs.vercel.app/")
    driver.maximize_window()

    time.sleep(3)

    about_btn = driver.find_element(By.XPATH,"/html/body/header/div/nav/ul/li[2]/a")
    about_btn.click()

    about = driver.find_element(By.XPATH, "/html/body/section[2]/div/div[1]/h2")
    assert about.text == "About Me"
    time.sleep(3)

    linkedin_btn = driver.find_element(By.XPATH, "/html/body/section[2]/div/div[2]/div[2]/div/div[4]/a[1]")
    linkedin_btn.click()
    time.sleep(5)

    driver.quit()


def test_github():
    driver = webdriver.Chrome()

    # Open Portfolio site
    driver.get("https://yhf-cs.vercel.app/")
    driver.maximize_window()

    time.sleep(3)

    about_btn = driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[2]/a")
    about_btn.click()

    about = driver.find_element(By.XPATH, "/html/body/section[2]/div/div[1]/h2")
    assert about.text == "About Me"
    time.sleep(3)

    github_btn = driver.find_element(By.XPATH, "/html/body/section[2]/div/div[2]/div[2]/div/div[4]/a[2]")
    github_btn.click()
    time.sleep(5)

    driver.quit()


def test_facebook():
    driver = webdriver.Chrome()

    # Open Portfolio site
    driver.get("https://yhf-cs.vercel.app/")
    driver.maximize_window()

    time.sleep(3)

    about_btn = driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[2]/a")
    about_btn.click()

    about = driver.find_element(By.XPATH, "/html/body/section[2]/div/div[1]/h2")
    assert about.text == "About Me"
    time.sleep(3)

    fb_btn = driver.find_element(By.XPATH, "/html/body/section[2]/div/div[2]/div[2]/div/div[4]/a[3]")
    fb_btn.click()
    time.sleep(5)

    cross_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div")
    cross_btn.click()
    time.sleep(5)

    driver.quit()