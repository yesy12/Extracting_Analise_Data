from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from logging import debug
from time import sleep

from functions import findElement, searchText
from ..Select import Select_s

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
        find = findElement(type)

        element = WebDriverWait(self.driver, seconds).until(
            EC.visibility_of_element_located((find, elementFind))
        )

        return element
    
    def ageCheck(self) -> None:
        debug("agecheck on the link")
        link = self.driver.current_url
        find = searchText(r"agecheck",link)

        if find:
            self.setMyDateFromGetAllReviews()
            sleep(0.2)
            self.accessPage()

    def verifyContentSexualGame(self):
        try:
            contentSexualGame = self.driver.find_element(By.CLASS_NAME, "contentcheck_btns_ctn")
            button = contentSexualGame.find_element(By.CLASS_NAME, "btn_blue_steamui")
            button.click()            
        except:
            pass

    def setMyDateFromGetAllReviews(self):
        select = Select_s(self.driver)

        select.setSelector(0, "ageDay", 0)
        select.setSelector(0, "ageMonth", 0)
        select.setSelector(0, "ageYear", 0)

    def accessPage(self):
        accessPage = self.driver.find_element(By.ID, "view_product_page_btn")
        accessPage.click()
