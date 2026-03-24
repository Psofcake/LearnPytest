# pages/signup.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignupPage:   # 회원가입코드
    URL = "file:///C:/Users/EDU01-14/Documents/swtest/signup.html"
    
    #LOCATORS
    EMAIL    = (By.ID, "email")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    CONFIRM  = (By.ID, "confirm")
    TERMS    = (By.ID, "terms")
    SUBMIT   = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH    = (By.ID, "flash")

    def __init__(self,driver,timeout = 20):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)

    def open(self):
        self.driver.get(self.URL)

    def clear_and_send_keys(self,locator,value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value or "")
        #or:value가 참이면 value, 거짓(None,빈 문자열,False 등)이면 "" 반환
        pass

    def set_checkbox(self,locator,should_be_checked):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        if element.is_selected() != should_be_checked: #원하는 상태와 다르면 클릭
            element.click()

    def signup(self, email="", username="", password="", confirm="", terms=False):
        self.clear_and_send_keys(self.EMAIL, email)
        self.clear_and_send_keys(self.USERNAME, username)
        self.clear_and_send_keys(self.PASSWORD, password)
        self.clear_and_send_keys(self.CONFIRM, confirm)
        self.set_checkbox(self.TERMS, terms)    
        
        submit_btn = self.wait.until(EC.element_to_be_clickable(self.SUBMIT))
        submit_btn.click()

    def flash_message(self):
        msg = self.wait.until(
            EC.presence_of_element_located(self.FLASH)).text
        return msg.strip()


if __name__ == "__main__":  # SignupPage클래스 동작 확인 코드 작성
    options = Options()
    options.add_argument("--window-size=1280,900")
    driver = webdriver.Edge(options=options)

    try:
        page = SignupPage(driver)
        page.open()
        page.signup(email="user@example.com", username="tester",
            password="abc12345", confirm="abc12345", terms=True)
        print("Flash 메시지:",page.flash_message())

    finally:
        input("키를 누르면 종료")
        driver.quit()
