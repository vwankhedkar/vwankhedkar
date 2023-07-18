from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def test_google():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("http://www.google.com")
    assert driver.title == "Google"
    driver.quit()

def test_facebook():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("http://www.facebook.com")
    assert  driver.title == "Facebook-log in or sign up"
    driver.quit()

def test_insta():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("http://www.instagram.com")
    assert driver.title == "Instagram"
    driver.quit()

def test_gmail():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("http://www.gmail.com")
    assert driver.title == "Gmail"
    driver.quit()

def test_rediff():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("http://www.rediff.com")
    assert driver.title == "Rediff.com: News | Rediffmail | Stock Quotes | Shopping"
    driver.quit()


OUTPUT:
-----
PS D:\pytestProject\nopCommerceApp\pytestsessions> py.test .\test_login_webpage.py
=============================================================== test session starts ===============================================================
platform win32 -- Python 3.11.4, pytest-7.4.0, pluggy-1.2.0
rootdir: D:\pytestProject\nopCommerceApp\pytestsessions
collected 5 items

test_login_webpage.py
DevTools listening on ws://127.0.0.1:54031/devtools/browser/eb12e103-f667-41f2-b3da-6ea899557653
.
DevTools listening on ws://127.0.0.1:54063/devtools/browser/be88077a-735b-4e4e-a495-bf5ac19a3e6d
F
DevTools listening on ws://127.0.0.1:54084/devtools/browser/7e2d00d0-d7f3-43c2-928b-dc17821c3863
.
DevTools listening on ws://127.0.0.1:54118/devtools/browser/a8506cc2-429d-4d98-888d-60a729b74040
.
DevTools listening on ws://127.0.0.1:54162/devtools/browser/94c4c640-81ce-4150-8fd3-766667546a77


PS D:\pytestProject\nopCommerceApp\pytestsessions> py.test -n 5  

