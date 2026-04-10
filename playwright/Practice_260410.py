#pip install playwright
#playwright install chromium
#npx playwright install

#python -c "from playwright.sync_api import sync_playwright; print('설치 완료!')"

###  ↓↓ playwright 레코딩 기능
#npx playwright codegen

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    #브라우저열기
    browser = p.chromium.launch(headless=False,slow_mo=500)
    page = browser.new_page()
    #페이지 이동
    page.goto('http://www.google.com')

    #페이지 제목 출력
    title = page.title()
    print(f'페이지 제목 : {title}')

    page.screenshot(path='screenshots/google.png')

    #3초 대기 후 브라우저 닫기
    page.wait_for_timeout(3000)
    browser.close()
    print('브라우저 종료 완료!')
