# 4.multi_pages.py
# <여러 페이지 열기 ( 같은 context 안의 여러 page )>

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel = "msedge", headless=False)

    # 컨텍스트 생성
    context = browser.new_context()

    # 내부적으로 서로 다른 콘텍스트
    page1 = context.new_page()
    page2 = context.new_page()

    page1.goto("https://www.google.com")
    page2.goto("https://www.naver.com")
    
    input("테스트용: 종료하려면 아무 키를 입력하세요")
    browser.close()
