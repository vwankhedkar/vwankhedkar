from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.google.com')
    print("Chrome successfully launched")
    print(page.title())
    page.wait_for_timeout(3000)
OUTPUT  
Chrome successfully launched
Google
--------------------------------------------------------------------------------------
from playwright.sync_api import sync_playwright
with sync_playwright() as play:
    browser = play.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/')
    emailtxtbox = page.wait_for_selector('#email')
    emailtxtbox.type('testmail@gmail.com')
    btnlogin = page.wait_for_selector('#enterimg')
    btnlogin.click()
    page.wait_for_timeout(3000)
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    username = page.wait_for_selector('input[name="username"]')
    username.type('Admin')
    password = page.wait_for_selector('input[type="password"]')
    password.type('admin123')
    loginbutton = page.wait_for_selector('button[type="submit"]')
    loginbutton.click()
    page.wait_for_timeout(3000)
--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------
