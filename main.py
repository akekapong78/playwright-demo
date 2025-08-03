import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://www.google.com/")
    await page.get_by_role("combobox", name="ค้นหา").click()
    await page.get_by_role("combobox", name="ค้นหา").fill("playwright")
    await page.goto("https://www.google.com/sorry/index?continue=https://www.google.com/search%3Fq%3Dplaywright%26sca_esv%3D29b06b32b8894029%26source%3Dhp%26ei%3DcjiPaP27LZqNnesPy6iSmQ8%26iflsig%3DAOw8s4IAAAAAaI9Gghp7iVL0zRwLxAVQbgFU0CN0T14x%26ved%3D0ahUKEwj9vNP4te6OAxWaRmcHHUuUJPMQ4dUDCA0%26uact%3D5%26oq%3Dplaywright%26gs_lp%3DEgdnd3Mtd2l6IgpwbGF5d3JpZ2h0MgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEjBsgFQ7VZYuGxwAXgAkAEAmAGSAaABogiqAQM1LjW4AQPIAQD4AQGYAgugAskIqAIKwgIKEAAYAxjqAhiPAcICChAuGAMY6gIYjwHCAgsQABiABBixAxiDAcICCBAAGIAEGLEDwgIREC4YgAQYsQMY0QMYgwEYxwHCAgsQLhiABBjRAxjHAcICDhAAGIAEGLEDGIMBGIoFwgILEC4YgAQYxwEYrwHCAgUQLhiABJgDBPEFANbukm3Eum-SBwM2LjWgB9omsgcDNS41uAfFCMIHBzAuNy4zLjHIBx8%26sclient%3Dgws-wiz%26sei%3DkziPaJqRF-ShnesPpoy-mQg&q=EgTKlwchGJPxvMQGIjB2dAvxUoEjAOWzbdXh93QPwE3KL8plXdpBCcurRgIrRpjRnbDDLswIswE4CjkThJ0yAVJaAUM")
    await page.locator("iframe[name=\"a-dxmmcwdwwust\"]").content_frame.get_by_role("checkbox", name="I'm not a robot").click()
    await page.locator("iframe[name=\"c-dxmmcwdwwust\"]").content_frame.locator(".rc-imageselect-tile").first.click()
    await page.locator("iframe[name=\"c-dxmmcwdwwust\"]").content_frame.locator("tr:nth-child(2) > td:nth-child(2)").click()
    await page.locator("iframe[name=\"c-dxmmcwdwwust\"]").content_frame.locator("tr:nth-child(2) > td:nth-child(3)").click()
    await page.locator("iframe[name=\"c-dxmmcwdwwust\"]").content_frame.get_by_role("button", name="Verify").click()

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
