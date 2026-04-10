# 테스트 페이지 - https://www.saucedemo.com/

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=500)
    page = browser.new_page()
    
    page.goto("https://www.saucedemo.com/")

    #----element----
    el_username = page.locator("#user-name")
    el_password = page.locator("#password")
    el_btn_login = page.locator("#login-button")
    el_btns_inventory = page.locator(".btn_inventory")

    #----input----
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"
    
    el_username.click()
    el_username.fill(USERNAME)

    el_password.click()
    el_password.fill(PASSWORD)

    el_btn_login.click()

    count = el_btns_inventory.count()
    for i in range(count):
        el_btns_inventory.nth(i).click()

    #page.locator("[data-test=\"shopping-cart-link\"]").click()

    page.wait_for_timeout(3000)
    browser.close()
    print('브라우저 종료 완료!')
