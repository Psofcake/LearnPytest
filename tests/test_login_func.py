#tests/test_login_func.py
#웹페이지 https://the-internet.herokuapp.com/login 테스트하기

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_success():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/login")
    
    # ID 입력 (tomsmith)
    username = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    username.clear()
    username.send_keys("tomsmith")

    # PW 입력 (SuperSecretPassword!)
    password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    password.clear()
    password.send_keys("SuperSecretPassword!")

    # 로그인 버튼 클릭
    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
    login_btn.click()

    # flash msg 가져오기
    flash_msg = wait.until(EC.visibility_of_element_located((By.ID, "flash"))).text
    assert "You logged into a secure area!" in flash_msg 

    # 링크 주소도 잘 바뀌었는지 확인 # https://the-internet.herokuapp.com/secure
    assert "/secure" in driver.current_url
