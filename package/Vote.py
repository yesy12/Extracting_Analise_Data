from selenium.webdriver.common.by import By
from functions import replace

class Vote:

    def __init__(self, driverApp) -> None:
        self.driverApp = driverApp

    def getVote(self):
        self.vote = self.driverApp.find_element(By.CLASS_NAME, "vote_header")

    def getRecomend(self) -> int:
        title = self.vote.find_element(By.CLASS_NAME, "title").text

        if "Recomendado" == title:
            return  1
        else:
            return 0

    def getHoursPlayers(self) -> float:
        hours = self.vote.find_element(By.CLASS_NAME, "hours").text

        return float(replace(hours))
            