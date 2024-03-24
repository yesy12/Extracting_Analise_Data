from selenium.webdriver.common.by import By
from package.functions import replace
from time import sleep

from .PlayerInfosReviewComments import PlayerInfosReviewComments

class PlayerInfo:

    def __init__(self, driverApp, linkNew, driver) -> None:
        self.driverApp = driverApp
        self.linkNew = linkNew
        self.comments = PlayerInfosReviewComments(driver, self.linkNew)

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
        

    
    def clickQuantifyComment(self) :
        if self.getQuantifyCommentAboutFromReview() > 0:
            self.comments.openNewTab()
            sleep(2)
            comentarios = self.comments.getComentarios()

            self.comments.closeTab()
            return comentarios
        else:
            return []
        
    