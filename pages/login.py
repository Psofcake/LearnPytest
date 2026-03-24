# pages/login.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:    # 웹페이지로그인코드
    # 로케이터를 따로 정의해두면 로케이터가 바뀔 때 여기만 수정하므로 간편!
    URL = "https://the-internet.herokuapp.com/login"
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH = (By.ID, "flash")
    LOGOUT = (By.CSS_SELECTOR, 'a[href="/logout"]')

    def __init__(self, d, timeout = 20):
        #멤버변수로 driver, wait 정의
        self.driver = d
        self.wait = WebDriverWait(d, timeout)

    def open(self): # 웹브라우저 열기
        self.driver.get(self.URL)

    def input_username(self,username):  # username = "tomsmith"
        username_input = self.wait.until(EC.visibility_of_element_located(self.USERNAME))
        username_input.clear()
        username_input.send_keys(username)

    def input_password(self,password):  # password = "SuperSecretPassword!"
        password_input = self.wait.until(EC.visibility_of_element_located(self.PASSWORD))
        password_input.clear()
        password_input.send_keys(password)

    def click_login(self):  # 로그인 클릭하기
        login_btn = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN))
        login_btn.click()

    def login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login()

    def get_flash_message(self):
        flash_msg = self.wait.until(
            EC.presence_of_element_located(self.FLASH))
        return flash_msg.text
    
    def logout(self):
        logout_btn = self.wait.until(
            EC.element_to_be_clickable(self.LOGOUT))
        logout_btn.click()

    def current_url(self):
        return self.driver.current_url

if __name__ == "__main__":  # test 실행중일때는 이하 코드가 실행되지 않도록 방지하는 조건문.(import로 호출될 때는 실행 안됨.)
    # LoginPage 클래스 동작 확인 코드 작성
    from selenium import webdriver

    driver = webdriver.Edge()

    try:
        # page = LoginPage(driver)
        # 인수를 주지 않으면 타임아웃은 위에서 default로 설정한 20초가 기본값
        page = LoginPage(driver, 10)
        page.open()
        page.login("tomsmith", "SuperSecretPassword!")
        print(f"로그인메시지: {page.flash_message()}")
        print(page.current_url())
        print(driver.title)
        
    finally :
        input("키를 눌러야 종료됩니다.")
        driver.quit()
