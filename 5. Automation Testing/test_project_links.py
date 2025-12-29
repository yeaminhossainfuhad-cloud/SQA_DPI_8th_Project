from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_project1_manual_links():
    driver = webdriver.Chrome()

    # Open Portfolio site
    driver.get("https://yhf-cs.vercel.app/")
    driver.maximize_window()

    time.sleep(3)

    project_btn = driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[5]/a")
    project_btn.click()

    project = driver.find_element(By.XPATH, "/html/body/section[5]/div/div[1]/h2")
    assert project.text == "Practice Projects"
    time.sleep(2)

    driver.execute_script("window.scrollBy(0,100);")
    time.sleep(5)

    project1 = driver.find_element(By.XPATH,"/html/body/section[5]/div/div[2]/div[1]")
    project1.click()
    time.sleep(3)

    manual_link = driver.find_element(By.XPATH,"/html/body/section[5]/div/div[2]/div[1]/div/p[2]/a[1]")
    manual_link.click()
    time.sleep(10)
    driver.quit()


def test_project1_automation_links():
    driver = webdriver.Chrome()

    # Open Portfolio site
    driver.get("https://yhf-cs.vercel.app/")
    driver.maximize_window()

    time.sleep(3)

    project_btn = driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[5]/a")
    project_btn.click()

    project = driver.find_element(By.XPATH, "/html/body/section[5]/div/div[1]/h2")
    assert project.text == "Practice Projects"
    time.sleep(2)

    driver.execute_script("window.scrollBy(0,100);")
    time.sleep(5)

    project1 = driver.find_element(By.XPATH,"/html/body/section[5]/div/div[2]/div[1]")
    project1.click()
    time.sleep(3)

    automation_link = driver.find_element(By.XPATH,"/html/body/section[5]/div/div[2]/div[1]/div/p[2]/a[2]")
    automation_link.click()
    time.sleep(10)
    driver.quit()


def test_project2_links():
    driver = webdriver.Chrome()

    # Open Portfolio site
    driver.get("https://yhf-cs.vercel.app/")
    driver.maximize_window()

    time.sleep(3)

    project_btn = driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[5]/a")
    project_btn.click()

    project = driver.find_element(By.XPATH, "/html/body/section[5]/div/div[1]/h2")
    assert project.text == "Practice Projects"
    time.sleep(2)

    driver.execute_script("window.scrollBy(0,100);")
    time.sleep(5)

    project2 = driver.find_element(By.XPATH,"/html/body/section[5]/div/div[2]/div[2]")
    project2.click()
    time.sleep(3)

    project_link = driver.find_element(By.XPATH,"/html/body/section[5]/div/div[2]/div[2]/div/p[2]/a")
    project_link.click()
    time.sleep(10)
    driver.quit()


def test_project3_links():
    driver = webdriver.Chrome()

    # Open Portfolio site
    driver.get("https://yhf-cs.vercel.app/")
    driver.maximize_window()

    time.sleep(3)

    project_btn = driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[5]/a")
    project_btn.click()

    project = driver.find_element(By.XPATH, "/html/body/section[5]/div/div[1]/h2")
    assert project.text == "Practice Projects"
    time.sleep(2)

    driver.execute_script("window.scrollBy(0,100);")
    time.sleep(5)

    project3 = driver.find_element(By.XPATH,"/html/body/section[5]/div/div[2]/div[3]")
    project3.click()
    time.sleep(3)

    project3_link = driver.find_element(By.XPATH,"/html/body/section[5]/div/div[2]/div[3]/div/p[2]/a")
    project3_link.click()
    time.sleep(10)
    driver.quit()