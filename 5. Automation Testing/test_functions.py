from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_all_functions():
    driver = webdriver.Chrome()

    # Open Portfolio site
    driver.get("https://yhf-cs.vercel.app/")
    driver.maximize_window()

    time.sleep(3)

    about_btn = driver.find_element(By.XPATH,"/html/body/header/div/nav/ul/li[2]/a")
    about_btn.click()

    about = driver.find_element(By.XPATH, "/html/body/section[2]/div/div[1]/h2")
    assert about.text == "About Me"
    time.sleep(5)

    edu_btn = driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[3]/a")
    edu_btn.click()

    edu = driver.find_element(By.XPATH, "/html/body/section[3]/div/div[1]/h2")
    assert edu.text == "Education & Experience"
    time.sleep(3)

    driver.execute_script("window.scrollBy(0,600);")
    time.sleep(3)

    skill_btn = driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[4]/a")
    skill_btn.click()

    skill = driver.find_element(By.XPATH, "/html/body/section[4]/div/div[1]/h2")
    assert skill.text == "Technical Skills"
    time.sleep(4)

    driver.execute_script("window.scrollBy(0,750);")
    time.sleep(3)

    project_btn = driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[5]/a")
    project_btn.click()

    project = driver.find_element(By.XPATH, "/html/body/section[5]/div/div[1]/h2")
    assert project.text == "Practice Projects"
    time.sleep(1)

    driver.execute_script("window.scrollBy(0,100);")
    time.sleep(5)

    contact_btn = driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[6]/a")
    contact_btn.click()

    contact = driver.find_element(By.XPATH, "/html/body/section[6]/div/div[1]/h2")
    assert contact.text == "Contact Me"
    time.sleep(5)

    home_btn = driver.find_element(By.XPATH, "/html/body/header/div/nav/ul/li[1]/a")
    home_btn.click()

    home = driver.find_element(By.XPATH, "/html/body/section[1]/div/div/div[2]/h1")
    assert home.text == "MD YEAMIN HOSSAIN FUHAD"
    time.sleep(5)

    getintouch_btn = driver.find_element(By.XPATH, "/html/body/section[1]/div/div/div[2]/a[1]")
    getintouch_btn.click()

    get = driver.find_element(By.XPATH, "/html/body/section[6]/div/div[2]/div/h3")
    assert get.text == "Get In Touch"
    time.sleep(5)

    logo_btn = driver.find_element(By.XPATH, "/html/body/header/div/nav/div[1]/a/span")
    logo_btn.click()

    logo = driver.find_element(By.XPATH, "/html/body/section[1]/div/div/div[2]/h1")
    assert logo.text == "MD YEAMIN HOSSAIN FUHAD"
    time.sleep(5)

    time.sleep(5)
    driver.quit()