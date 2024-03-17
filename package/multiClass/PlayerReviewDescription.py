from selenium.webdriver.common.by import By
from package.functions import replaceDateAndSplit,getIndexsFromMonth,addYearDatePublish, splitSpecific
from lxml import html
import re

class PlayerReviewDescription():

    def __init__(self, driverApp) -> None:
        self.driverApp = driverApp

    def getPublishDay(self) -> int:
        publish = self.driverApp.find_element(By.CLASS_NAME,"date_posted").text

        publish = replaceDateAndSplit(publish)
        publish[1] = getIndexsFromMonth(publish[1])
        publish = addYearDatePublish(publish)
        publish[2] = int(publish[2])
        
        return publish

    def getReviewAboutTheGame(self) -> str:    
        html_content =  self.driverApp.get_attribute("innerHTML")        

        tree = html.fromstring(html_content)

        elements = tree.xpath('//div[not(@class="date_posted")]')
        elements_text_strip = []

        for element in elements:
            e = re.sub("\t","",element.text_content().strip())
            e = re.sub("Publicada: .+[0-9]","",e)            
            elements_text_strip.append(e)
  
        return elements_text_strip
