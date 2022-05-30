def footshop_has_active_raffles(page):
    page.goto("https://releases.footshop.com/", timeout=120000)
    active_raffles = page.query_selector_all("div[class^=card]:not([class*=closed])")
    
    if active_raffles:
        return True

def randomshop_has_active_raffles(page):
    page.goto("https://randomshop.com/", timeout=120000)
    active_raffles = page.query_selector_all("pesho")
    
    if active_raffles:
        return True
