from playwright.sync_api import sync_playwright, Page, expect

# 엣지에서 실행하려면 pytest --browser=chromium --channel=msedge

URL = "https://the-internet.herokuapp.com/dynamic_loading/2"
EXPECTED = "Hello World!"


def test_dynamic_loading_playwright(page:Page):
    page.goto(URL)
    print(page.title())

    page.locator("#start button").click()

    # assert EXPECTED in page.locator(flash_locator).text
    flash_locator = page.locator(flash_locator)
    expect(flash_locator).to_have_text(EXPECTED)

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
