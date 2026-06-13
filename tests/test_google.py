import re
from playwright.sync_api import expect

def test_google(page):
    page.goto("https://www.google.com/ncr")
    page.get_by_role("combobox", name="Search").fill("Playwright")
    page.keyboard.press("Enter")
    expect(page).to_have_title(re.compile("Playwright"))