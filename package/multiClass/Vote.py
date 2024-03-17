from selenium.webdriver.common.by import By
from package.functions import replaceHours,replace
 

class Vote:

    def __init__(self, driverApp) -> None:
        self.driverApp = driverApp

    def getRecomend(self) -> int:
        recomend = self.driverApp.find_element(By.CLASS_NAME, "title").text

        if recomend == "Recomendado":
            return 1
        else:
            return -1
    
        
    def getHoursPlayers(self) -> float:
        hours = self.driverApp.find_element(By.CLASS_NAME, "hours").text
        return float (replace(replaceHours(hours)))
        