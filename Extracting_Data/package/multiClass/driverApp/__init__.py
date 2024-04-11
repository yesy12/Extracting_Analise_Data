from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from logging import debug
from time import sleep

class DriverApp:

    def __init__(self, driver) -> None:
        self.driver = driver

    def scroll(self,seconds):
        height = self.getScrollHeight()
        debug(f"Scroll to height: {height}")
        self.driver.execute_script(f"window.scrollTo(0,{height})")
        sleep(seconds)  

    def getScrollHeight(self) -> int:
        try:
            return self.driver.execute_script("return document.body.scrollHeight")
        except:
            return -1

    def scrollInfinite(self, seconds):
        while True:
            sleep(2)
            
            lastHeight = self.getScrollHeight()                

            self.scroll(seconds) 

            newScrollHeight = self.getScrollHeight()       
            
            if lastHeight == newScrollHeight:
                break

    def returnElement(self, seconds, type, elementFind ):
        find = By.ID

        if type == 1:
            find = By.CLASS_NAME
        elif type == 2:
            find = By.TAG_NAME
        elif type == 3:
            find = By.XPATH

        element = WebDriverWait(self.driver, seconds).until(
            EC.visibility_of_element_located((find, elementFind))
        )

        return element