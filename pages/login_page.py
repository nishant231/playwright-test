from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Submit")

    def goto(self):
        self.page.goto("https://practicetestautomation.com/practice-test-login/")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()