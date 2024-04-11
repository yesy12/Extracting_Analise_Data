from selenium.webdriver.common.by import By
from package.functions import replaceDateAndSplit,getIndexsFromMonth,addYearDatePublish, splitSpecific,subSpecificParams
from lxml import html
from logging import debug

class PlayerReviewDescription():

    def __init__(self, driverApp) -> None:
        self.driverApp = driverApp

    def getPublishDay(self) -> str:
        publish = self.driverApp.find_element(By.CLASS_NAME,"date_posted").text

        publish = replaceDateAndSplit(publish)
        publish[1] = getIndexsFromMonth(publish[1])
        publish = addYearDatePublish(publish)
        publish[2] = int(publish[2])
        
        publish = f"{publish[2]}-{publish[1]}-{publish[0]}"
        debug("Publish day")
        return publish

    def getReviewAboutTheGame(self) -> str:    
        html_content =  self.driverApp.get_attribute("innerHTML")        

        tree = html.fromstring(html_content)

        elements = tree.xpath('//div[not(@class="date_posted")]')
        elements_text_strip = []
        
        for element in elements:
            e = subSpecificParams("\t","",element.text_content().strip())
            e = subSpecificParams("Publicada: [0-9].+\n","",e)
                      
            elements_text_strip.append(e)
  
        element = ""
        for element_text in elements_text_strip:
            element += element_text

        element = subSpecificParams("'","", element)

        debug("Review from player")
        return element
