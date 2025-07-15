from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Adjust if needed

def test_google():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()
def test_facebook():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com")
    assert "Facebook" in driver.title
    driver.quit()
def test_insta():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    driver.get("https://www.instagram.com")
   # assert "Facebook" in driver.title
    driver.quit()
def test_gmail():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    driver.get("https://www.gmail.com")
   # assert "Facebook" in driver.title
    driver.quit()
def test_rediff():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    driver.get("https://www.rediffmail.com")
   # assert "Facebook" in driver.title
    driver.quit()

(.venv) PS C:\Users\vwank\PycharmProjects\PytestJuly25\Selenium> pip install pytest-xdist 

(.venv) PS C:\Users\vwank\PycharmProjects\PytestJuly25\Selenium> pytest -n 5 .\test_webpage_login.py
=============================================================== test session starts ===============================================================
platform win32 -- Python 3.13.1, pytest-8.4.1, pluggy-1.6.0
rootdir: C:\Users\vwank\PycharmProjects\PytestJuly25\Selenium
plugins: html-4.1.1, metadata-3.1.1, xdist-3.8.0
5 workers [5 items]     

DevTools listening on ws://127.0.0.1:60714/devtools/browser/86267bfe-fc88-41a5-a502-f3decfd1171a

DevTools listening on ws://127.0.0.1:60742/devtools/browser/1b03eb20-1af3-4f4a-91f4-6b22d5e31b70

DevTools listening on ws://127.0.0.1:60748/devtools/browser/143c5499-306b-40df-b938-83e8c60b9460

DevTools listening on ws://127.0.0.1:60751/devtools/browser/1b57ce2c-652a-4a88-a949-da9cd6272418

DevTools listening on ws://127.0.0.1:60756/devtools/browser/fb4eecc3-c183-4465-80c0-5e0fbdc58a0e
[16520:32656:0715/123803.328:ERROR:net\socket\ssl_client_socket_impl.cc:896] handshake failed; returned -1, SSL error code 1, net_error -3
[21164:35336:0715/123804.046:ERROR:gpu\ipc\client\command_buffer_proxy_impl.cc:327] GPU state invalid after WaitForGetOffsetInRange.
.....                                                                                                                                        [100%]
=============================================================== 5 passed in 50.50s ================================================================ 
(.venv) PS C:\Users\vwank\PycharmProjects\PytestJuly25\Selenium> 
