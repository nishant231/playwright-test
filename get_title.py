from playwright.sync_api import sync_playwright


def test_get_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://www.google.com")
        title = page.title()
        print(f"Page title: {title}")
        assert title == "Google"
        browser.close()
