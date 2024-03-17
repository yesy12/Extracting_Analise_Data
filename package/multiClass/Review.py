from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from package.multiClass.PlayerReviewDescription import PlayerReviewDescription
from package.multiClass.Likes import Likes
from package.multiClass.Vote import Vote
from package.multiClass.PlayerInfos import PlayerInfo

class Review():

    def __init__(self, ) -> None:
        self.driver = webdriver.Edge()

    def getLink(self, link) -> None:
        self.driver.get(link)

    def setPageRow(self, pageIndex) -> None:
        pageRow = self.driver.find_element(By.ID, f"page{pageIndex}")

        self.divCardRows = pageRow.find_elements(By.XPATH,"//div[@class='apphub_CardRow' ]")


    
    def getGeral(self) -> None:
        i = 0
        for divCardRow in self.divCardRows:                
            divCardRowRewiewUniquePlayers = divCardRow.find_elements(By.CLASS_NAME, "apphub_Card")
        

            for divCardRowReviewUniquePlayer in divCardRowRewiewUniquePlayers:
                i+= 1
                geral = divCardRowReviewUniquePlayer.find_element(By.CLASS_NAME, "apphub_CardContentMain")
                appReviews = geral.find_element(By.CLASS_NAME,"apphub_UserReviewCardContent") 
                            
                self.getDescriptionForLikes(appReviews)
                self.getDescriptionForVote(appReviews)
                self.getDescriptionForRewiew(appReviews)

                self.getPlayerInfo(divCardRowReviewUniquePlayer)
                self.getInfo()
                
        

    def getDescriptionForLikes(self, appReviewsDriver) -> None:
        found = appReviewsDriver.find_element(By.CLASS_NAME, "found_helpful").text
        self.likes = Likes(found)        

    def getDescriptionForVote(self, appReviewsDriver) -> None:
        vote = appReviewsDriver.find_element(By.CLASS_NAME, "vote_header")
        self.vote = Vote(vote)

    def getDescriptionForRewiew(self, appReviewsDriver) -> None:
        cardContextReview = appReviewsDriver.find_element(By.CLASS_NAME, "apphub_CardTextContent")
        self.player =  PlayerReviewDescription(cardContextReview)
    
    def getPlayerInfo(self, divCardRowRewiewUniquePlayerDriver) -> None:
        appPlayersInfo = divCardRowRewiewUniquePlayerDriver.find_element(By.CLASS_NAME,"apphub_CardContentAuthorBlock")
        self.playerInfo = PlayerInfo(appPlayersInfo)

    def getInfo(self) -> None:
        print("-"*100)
        print("Likes")
        
        print(f"\tEmoticon: {self.likes.getLikesEmoticon()}, Util: {self.likes.getLikesUtil()}, Engraçada: {self.likes.getLikesFunny()}\n")

        print("Votes")
        print(f"\tRecomend: {self.vote.getRecomend()}, Horas jogadas: {self.vote.getHoursPlayers()}\n")

        print("Review")
        print(f"\tPublicado em: {self.player.getPublishDay()}")
        print(f"\tReview: {self.player.getReviewAboutTheGame()}\n")        

        print("Informações do player")
        print(f"\tLink da steam: [{self.playerInfo.getLinkPlayerSteam()}]")
        print(f"\tNickname: {self.playerInfo.getRandomNickname()}")
        print(f"\tQuantidade de Games: {self.playerInfo.getQuantifyGameFromPlayerReview()}")
        print(f"\tQuantidade de Comentarios: {self.playerInfo.getQuantifyCommentAboutFromReview()}\n")
        print("-"*100+"\n\n")