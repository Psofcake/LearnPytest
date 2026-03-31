from playwright.sync_api import sync_playwright, Page, expect

# 엣지에서 실행하려면 pytest --browser=chromium --channel=msedge

URL = "https://the-internet.herokuapp.com/dynamic_loading/2"
EXPECTED = "Hello World!"


def test_dynamic_loading_playwright(page:Page):
    page.goto(URL)
    print(page.title())

    page.locator("#start button").click()

    # [방법 1] inner_text() 직접 가져와서 비교하기. (권장하지 않음)
    '''
    flash_msg = page.locator("#finish").inner_text()
    print(f"##{flash_msg}##")
    assert EXPECTED in flash_msg
    '''
    # #inner_text는 기다리지 않음(즉시 실행).
    # 요소가 렌더링안되면 그대로 실패할 수 있으므로 권장하지 않음.
    # inner_text로 가져오기보다는 to_have_text(자동 대기)를 권장.

    # [방법 2] to_have_text
    # Playwright의 기본 timeout은 5초이므로
    # 로딩이 오래 걸린다면 오류 발생 가능. 대기를 위해 타임아웃 추가
    '''
    flash_locator = page.locator("#finish")
    expect(flash_locator).to_have_text(EXPECTED, timeout=10000)
    '''

    # [방법 3] to_be_hidden
    # #loading 요소가 사라질 때 까지 대기. 다음 검증이 안전하게 실행되도록 타이밍 맞춰주기.
    '''
    expect(page.locator("#loading")).to_be_hidden(timeout=10000)
    flash = page.locator("#finish")
    expect(flash).to_have_text(EXPECTED) 
    '''

    # [방법 4] use_inner_text는 UI 테스트에서 숨겨진 요소를 제외하고 싶을 때.
    # #use_inner_text는 display:none,visibility:hidden,opacity:0,offscreen 텍스트를 무시함.
    # 숨겨진 텍스트(기본값에는 포함됨)는 무시하고 화면에 보이는 텍스트만 가져온다.
    # 공백 normalize 기능 : 비교 문자열 사이에 공백이나 줄바꿈이 많은 경우에도 유용함.
    '''
    flash_locator = page.locator("#finish")
    expect(flash_locator).to_have_text(EXPECTED, use_inner_text=True, timeout=10000)
    '''

    # [방법 5] HTML의 DOM 트리 구조를 타고 접근
    #expect(page.locator(".example div>h4")).to_have_text(EXPECTED, timeout=10000)

    # [방법 6] 접근성(role+name)기반 -구조에 비의존적
    # <h1>~<h6>는 자동으로 role="heading"을 가짐. (헤더 태그)
    # name = 사용자에게 보이는 텍스트 (accessible name)
    flash_locator = page.get_by_role("heading", name=EXPECTED)
    expect(flash_locator).to_have_text(EXPECTED, timeout=10000)
    
'''
def test_dynamic_loading_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=False)
        page = browser.new_page()
    
        page.goto(URL)
        print(page.title())

        page.locator("#start button").click()
        flash_locator = page.locator(flash_locator)
        expect(flash_locator).to_have_text(EXPECTED)

        browser.close()
'''
