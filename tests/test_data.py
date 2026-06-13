import pytest
from playwright.sync_api import Page, expect


@pytest.mark.parametrize("username, password, expected", [
    ("student", "Password123", "Logged In Successfully"),   # valid
    ("nishant", "123",         "Your username is invalid!"), # invalid username
    ("student", "wrongpass",   "Your password is invalid!"), # invalid password
])
def test_login(page: Page, username, password, expected) -> None:
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Submit").click()
    expect(page.locator("body")).to_contain_text(expected)