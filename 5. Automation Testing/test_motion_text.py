from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_motion_text():
    driver = webdriver.Chrome()

    # Open Portfolio site
    driver.get("https://yhf-cs.vercel.app/")
    motion_text = driver.find_element(By.XPATH, "/html/body/section[1]/div/div/div[2]/h2/span[1]")
    possible_texts = ["J","u","n","i","o","r","S","Q","A","E","n","g","i","n","e","e","r","P","y","t","h","o","n","D","e","v","e","l","o","p","e","r", "I","n","t","e","r","n", "I","T", "S","u","p","p","o","r","t", "E","n","g","i","n","e","e","r"]
    assert any(text in motion_text.text for text in possible_texts), \
        f"Text '{motion_text.text}' doesn't contain any of {possible_texts}"

    driver.maximize_window()

    time.sleep(10)
    driver.quit()
