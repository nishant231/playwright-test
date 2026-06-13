from playwright.sync_api import Playwright, sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto("https://selectorshub.com/xpath-practice-page/")
    # page.get_by_placeholder("Enter email").click()
    # page.get_by_placeholder("Enter email").fill("nishant123@gmail.com")
    # page.get_by_placeholder("Enter Password").click()
    # page.locator("xpath=//input[@id='shub19']").click()
    # page.get_by_placeholder("Enter Password").fill("Password123")
    page.locator("xpath=//input[@name='company']").first.click()
    page.locator("xpath=//input[@name='company']").first.fill("Nishant's Company")

    page.locator("xpath=//input[@id=cardName]").click()
    page.locator("xpath=//input[@id=cardName]").fill("Nishant")
    browser.close()