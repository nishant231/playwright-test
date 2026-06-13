from playwright.sync_api import expect
from pages.login_page import LoginPage


def test_valid_login(page):
    login = LoginPage(page)
    login.goto()
    login.login("student", "Password123")
    expect(page).to_have_url("https://practicetestautomation.com/logged-in-successfully/")
    expect(page.get_by_role("heading", name="Logged In Successfully")).to_be_visible()


def test_invalid_login(page):
    login = LoginPage(page)
    login.goto()
    login.login("wronguser", "wrongpassword")
    expect(page.locator("#error")).to_be_visible()