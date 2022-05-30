from time import sleep
from playwright.sync_api import sync_playwright
import site_scrapers

with sync_playwright() as p:
    browser = p.webkit.launch()
    page = browser.new_page()
    # page.goto("https://releases.footshop.com/", timeout=0)
    
    # while True:
    #     page.screenshot(path="footshop_raffle_page.png", full_page=True)
    #     active_raffles = page.query_selector_all("div[class^=card]:not([class*=closed])")
    #     closed_raffles = page.query_selector_all("div[class^=card][class*=closed]")

    #     print(f"active raffles: {len(active_raffles)}")
    #     print(f"closed raffles: {len(closed_raffles)}")

    #     # sleep(5)
    #     page.reload(timeout=0)

    #     # document.querySelectorAll('div[class^=card]:not([class*=closed])')
    
    while True:
        if site_scrapers.footshop_has_active_raffles(page):
            ...
        if site_scrapers.randomshop_has_active_raffles(page):
            ...

        sleep(10)
        
    browser.close()
