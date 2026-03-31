# pages/login_by_playwright.py

from playwright.sync_api import Page, sync_playwright

class LoginPage:    # 웹페이지 로그인 코드
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page:Page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.flash = page.locator("#flash")
        self.logout_button = page.locator('a[href="/logout"]')
        
    def open(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def logout(self):
        self.logout_button.click()

    def get_flash_msg(self):
        return self.flash.inner_text()

if __name__ == "__main__":
    # LoginPage 클래스 동작 확인 코드
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(channel = "msedge", headless=False, slow_mo=200)
        # slow_mo = 각 액션(action) 사이에 인위적으로 지연(delay)을 넣는 것.
        # (= 모든 Playwright 명령 사이에 200ms(0.2초) 지연을 추가)
        # 디버깅 동작을 눈으로 확인할 때만 사용. 빠른 자동화 속도를 위해서는 제거 권장.

        page = browser.new_page()

        login_page = LoginPage(page)

        login_page.open()
        login_page.login("tomsmith", "SuperSecretPassword!")
        print(login_page.get_flash_msg())

        browser.close()
