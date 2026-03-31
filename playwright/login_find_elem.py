#playwright/login_find_elem.py

from playwright.sync_api import sync_playwright

URL = "https://the-internet.herokuapp.com/login"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    
    # 페이지 접속
    page.goto(URL)
    
    # 아이디 입력칸 찾기 후 입력
    username_input = page.locator("#username")
    username_input.fill("tomsmith")

    # 비밀번호 입력칸 찾기 후 입력
    password_input = page.locator("#password")
    password_input.fill("SuperSecretPassword!")
    
    # 로그인버튼 찾기 후 클릭
    login_button = page.locator("button[type='submit']")
    login_button.click()

    page.wait_for_timeout(3000)
    browser.close()
