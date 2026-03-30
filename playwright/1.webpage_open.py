# 1.webpage_open.py
# <브라우저를 사용하여 페이지 만들기>

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    #browser = p.chromium.launch (headless=False)   # 크롬 브라우저 실행
    browser = p.chromium.launch(channel = "msedge", headless=False) # Edge 실행

    # 플레이라이트는 브라우저와 페이지의 개념이 나뉘어있다.
    page = browser.new_page()   # 새 페이지 만들기
    page.goto("https://www.google.com") # 사이트 이동
    print(page.title()) # 페이지 제목 출력
    page.screenshot(path="screenshot.png")  # 스크린샷 저장
    
    # page.pause()
    browser.close()
