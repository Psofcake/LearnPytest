# 3.multi_pages.py
# <여러 페이지 열기 ( 각 페이지가 서로 다른 context )>

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel = "msedge", headless=False)

    # 각 페이지가 내부적으로 서로 다른 컨텍스트.
    page1 = browser.new_page()
    page1.goto("https://www.google.com")

    page2 = browser.new_page()
    page2.goto("https://www.naver.com")
    
    input("테스트용: 종료하려면 아무 키를 입력하세요")
    browser.close()
