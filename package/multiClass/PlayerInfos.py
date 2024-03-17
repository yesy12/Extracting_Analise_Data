from selenium.webdriver.common.by import By
from package.functions import replace
import names
from random import randint

class PlayerInfo:

    def __init__(self, driverApp) -> None:
        self.driverApp = driverApp
   
        

    def getLinkPlayerSteam(self) -> str:

        apphub_friend_block_container = self.driverApp.find_element(By.CLASS_NAME, "apphub_friend_block_container")
        steamlinkPlayers  = apphub_friend_block_container.find_element(By.TAG_NAME, "a").get_attribute("href")
        
        return steamlinkPlayers
    
    def getQuantifyGameFromPlayerReview(self) -> int:
        quantify = self.driverApp.find_element(By.CLASS_NAME, "apphub_CardContentMoreLink").text
        try:
            return int(replace(quantify))
        except:
            return -1

    
    def getQuantifyCommentAboutFromReview(self) -> int:
        quantify = self.driverApp.find_element(By.CLASS_NAME,"apphub_UserReviewCardStats")
        return int(quantify.text)
        
    def getRandomNickname(self) -> str:
        name = names.get_first_name()
        return f"{name}_{randint(1,100000)}"
    
    
    def clickQuantifyComment(self) -> None:
        pass
        