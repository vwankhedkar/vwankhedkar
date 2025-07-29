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
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    username_element = page.wait_for_selector('//input[@name="username"]')
    username_element.type('Admin')
    password_element = page.wait_for_selector('//input[@placeholder="Password"]')
    password_element.type('admin123')
    login_element = page.wait_for_selector('//button[@type="submit"]')
    login_element.click()
    page.wait_for_timeout(3000)
--------------------------------------------------------------------------------------
import time
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')
    # select_dropdown = page.query_selector('//select[@id="Skills"]')
    # time.sleep(1)
    # select_dropdown.select_option(label='Art Design')
    page.select_option('//select[@id="Skills"]',label='AutoCAD')
    time.sleep(2)
    page.wait_for_timeout(3000)
--------------------------------------------------------------------------------------
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    username_element = page.wait_for_selector('//input[@name="username"]')
    username_element.type('Admin')
    password_element = page.wait_for_selector('//input[@placeholder="Password"]')
    password_element.type('admin123')
    login_element = page.wait_for_selector('//button[@type="submit"]')
    login_element.click()
    page.wait_for_timeout(3000)
    # page.wait_for_selector('//p[text()="Forgot your password? "]').click()
    # page.wait_for_timeout(3000)
    # locators
    # //input[contains(@placeholder,"Username")] and //label[contains(text(), "Username")]
    # family
    # parent - //tagname[@id="xy"]/parent::input[]
    # child - //tagname[@id="xy"]/child::input[]
    # ancestor
    # sibling - //td[text()="Microsoft"]//following-sibling:: td[2]
--------------------------------------------------------------------------------------
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')
    radio_button = page.query_selector('//input[@value="FeMale"]')
    radio_button.click()
    radio_button.check()
    if radio_button.is_checked():
        print("Passed")
    else:
        print("Failed")
    page.wait_for_timeout(3000)
--------------------------------------------------------------------------------------
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html')
    radio_button = page.query_selector('//input[@value="FeMale"]')
    # radio_button.click()
    radio_button.check()
    if radio_button.is_checked():
        print("Passed")
    else:
        print("Failed")
    # page.wait_for_timeout(3000)
Chrome successfully launched
Google
--------------------------------------------------------------------------------------
from playwright.sync_api import sync_playwright
text_alert = []
def handle_dialog(dialog):
    message = dialog.message
    text_alert.append(message)
    dialog.accept()
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Alerts.html')
   # page.wait_for_selector('//div[@id="OKTab"]/button').click()
    page.wait_for_selector('//a[@href="#CancelTab"]').click()
    page.wait_for_timeout(2000)
    page.on("dialog",lambda dialog : dialog.accept())
    page.wait_for_selector('//div[@id="CancelTab"]/button').click()
    page.wait_for_timeout(2000)
    print(text_alert[0])
--------------------------------------------------------------------------------------
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://demo.automationtesting.in/Windows.html')
    page.wait_for_selector('//button[contains(text(),"    click   ")]').click()
    page.wait_for_timeout(3000)
    total_pages = context.pages
    print(len(total_pages))
    for i in total_pages:
        print(i)
2
<Page url='https://demo.automationtesting.in/Windows.html'>
<Page url='https://www.selenium.dev/'>
--------------------------------------------------------------------------------------
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://demo.automationtesting.in/Windows.html')
    page.wait_for_selector('//button[contains(text(),"    click   ")]').click()
    page.wait_for_timeout(3000)
    total_pages = context.pages
    print(len(total_pages))
    for i in total_pages:
        print(i)
    print(page.title())
    new_page = total_pages[1]
    new_page.bring_to_front()
    page.wait_for_timeout(3000)
    print(new_page.title())
    new_page.close()
    page.bring_to_front()
    page.wait_for_timeout(3000)
    browser.close()
2
<Page url='https://demo.automationtesting.in/Windows.html'>
<Page url='https://www.selenium.dev/'>
Frames & windows
Selenium
--------------------------------------------------------------------------------------
from jinja2.runtime import new_context
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.redbus.in/')
    my_cookies = page.context.cookies()
    print(my_cookies)
    page.context.clear_cookies()
    new_cookies = {
        'name' : 'ravi',
        'udid' : '4375y34975y3947595483'
    }
    page.context.add_cookies([new_cookies])
    page.screenshot(path='test.png', full_page=True)
--------------------------------------------------------------------------------------
import time

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://demo.automationtesting.in/Selectable.html')
    page.wait_for_selector('//a[text()="SwitchTo"]').hover()
    time.sleep(3)
    page.wait_for_selector('//a[text()="SwitchTo"]').click()
    time.sleep(3)
    page.wait_for_selector('//a[text()="SwitchTo"]').dblclick()
    time.sleep(3)
    page.wait_for_selector('//a[text()="SwitchTo"]').click(button="right")
    time.sleep(3)
    page.wait_for_selector('//a[text()="SwitchTo"]').click(modifiers=["Shift"])
    time.sleep(3)
    page.wait_for_selector('//a[text()="SwitchTo"]').press("A")
    time.sleep(3)
    page.wait_for_selector('//a[text()="SwitchTo"]').press("$")
    page.wait_for_timeout(2000)
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
--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------
