from playwright.sync_api import (
    Browser as PWBrowser,
    BrowserContext,
    Page,
    Playwright,
    sync_playwright,
)


class Browser:

    def __init__(self):

        self.playwright: Playwright | None = None
        self.browser: PWBrowser | None = None
        self.context: BrowserContext | None = None
        self.page: Page | None = None

    def start(self, headless: bool = False):

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=headless
        )

        self.context = self.browser.new_context()

        self.page = self.context.new_page()

    def open(self, url: str):

        if self.page is None:
            raise RuntimeError("Browser not started.")

        self.page.goto(
            url,
            wait_until="networkidle"
        )

    def title(self):

        if self.page is None:
            raise RuntimeError("Browser not started.")

        return self.page.title()

    def close(self):

        if self.context:
            self.context.close()

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()


browser = Browser()