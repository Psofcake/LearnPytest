# 2.webpage_open.py
# <브라우저 컨텍스트를 사용하여 페이지 만들기>
# 컨텍스트는 다른 브라우저 컨텍스트와 쿠키나 캐시를 공유하지 않는다
# - 독립된 브라우저 세션을 명시적으로 관리할 때
# - 로그인 상태 분리가 필요한 경우
# - 세션 분리가 필요한 경우

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel = "msedge", headless=False)

    context = browser.new_context() # 새 컨텍스트 만들기
    page = context.new_page()   # 새 페이지 만들기

    page.goto("https://www.google.com")
    print(page.title())
    page.screenshot(path="screenshot.png")
    
    # page.pause()
    context.close() # 컨텍스트를 먼저 닫아준다.
    browser.close()
