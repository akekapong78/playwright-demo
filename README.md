# 🧪 Playwright Python Demo

A simple demo project using [Playwright](https://playwright.dev/python/) with `pytest` and [uv](https://github.com/astral-sh/uv) for fast dependency management.

---

## 📦 Setup Instructions
```bash
# 1. Initialize the project
uv init playwright-demo
cd playwright-demo

# 2. Create a virtual environment
uv venv

# 3. Install Playwright + pytest plugin
uv pip install pytest-playwright

# 4. Install browser binaries
uv run playwright install
```


## ✅ Example Test Case (prepix. test_xxxx.py)
```python
import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
```

🚀 Running Tests
```bash
# Run tests in headless mode
uv run pytest

# Run tests in headed mode (shows browser UI)
uv run pytest --headed
```


## 🔁 Code Generation
```bash
uv run playwright codegen www.google.com

# copy recorded-gen-code to main.py
uv run main.py
```

🚀 Running browser
```python
import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect

async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://www.google.com/")
    await browser.close()

async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
```




