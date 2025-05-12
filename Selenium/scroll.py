TestScroll.py

from scroll import ScrollBar
class Test:
    def test_method(self):
        test_url = "https://support.smartbear.com/testcomplete/docs/reference/test-objects/controls/desktop/general/scroll-bar/index.html"
        scroll = ScrollBar()
        scroll.open_site(test_url)
        scroll_height, offset_height = scroll.get_scroll_height()
        assert scroll_height > offset_height

scroll.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class ScrollBar:
    driver = ""
    scroll_bar = "//div[@class='aqActiveTabContent']//div[@class='aqTabScrollData']"

    def open_site(self, url):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

        self.driver.get(url)

    def get_scroll_height(self):
        scroll_height = self.driver.find_element(By.XPATH, self.scroll_bar).get_attribute('scrollHeight')
        offset_height = self.driver.find_element(By.XPATH, self.scroll_bar).get_attribute('offsetHeight')
        print("scroll_height, offset_height", scroll_height, offset_height)
        return scroll_height, offset_height
