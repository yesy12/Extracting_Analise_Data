from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

from os import path
from sys import path as path2

root_dir = path.dirname(path.abspath(__file__))
path2.append(path.join(root_dir, ".."))

from package.multiClass.Reviews.PlayerReviewDescription import PlayerReviewDescription

from package.multiClass.Descriptions.Likes import Likes
from package.multiClass.Descriptions.Vote import Vote

from package.multiClass.PlayerAboutInformation.PlayerInfos import PlayerInfo
from package.multiClass.PlayerAboutInformation.Comments.Comments import Commnents

from package.multiClass.SaveOnDatabase.Save import Save

import re

class Review():

    def __init__(self, ) -> None:
        self.driver = webdriver.Edge()
        self.index = 0
        self.save = Save()

        self.postIDReview = 0
        self.steamIDUser = 0

    def getLink(self, link) -> None:
        self.driver.get(link)

    def ageCheck(self) -> None:
        link = self.driver.current_url
        find = re.search(r"agecheck",link)

        if find:
            self.setMyDateFromGetAllReviews()
            sleep(0.2)
            self.accessPage()



    def setMyDateFromGetAllReviews(self):
        ageDay = Select(self.driver.find_element(By.ID,"ageDay"))
        ageMonth = Select(self.driver.find_element(By.ID,"ageMonth"))
        ageYear = Select(self.driver.find_element(By.ID,"ageYear"))

        ageDay.select_by_index(0)
        ageMonth.select_by_index(0)
        ageYear.select_by_index(0)

    def accessPage(self):
        accessPage = self.driver.find_element(By.ID, "view_product_page_btn")
        accessPage.click()


    def getAllReviews(self)-> None:
        while True:
            lastHeight = self.getScrollHeight()
            self.scroll()
            newScrollHeight = self.getScrollHeight()
            if lastHeight == newScrollHeight:
                break
        
        sleep(2)
        allReview = self.driver.find_element(By.CLASS_NAME, "view_all_reviews_btn")
        allReview.click()
        

    def gameActual(self):
        div = self.driver.find_element(By.CLASS_NAME, "apphub_OtherSiteInfo")                   
        appID = div.find_element(By.CLASS_NAME, "btnv6_blue_hoverfade")

        self.AppIDGame = appID.get_attribute("data-appid") 
        linkGameSteam = appID.get_attribute("href")

        title = div = self.driver.find_element(By.CLASS_NAME, "apphub_AppName").text

        self.save.saveGameTitle(self.AppIDGame, title, linkGameSteam)

    def setPageRow(self, pageIndex, indexUnique=False) -> None:
        pageRow = self.driver.find_element(By.ID, f"page{pageIndex}")
        print(f"Página: {pageIndex}")

        self.divCardRows = pageRow.find_elements(By.XPATH,"//div[@class='apphub_CardRow' ]")

        if(indexUnique == True):
            self.divCardRow = pageRow.find_element(By.ID, "page_1_row_1_template_twoSmall")
   
    def exitOnThisGame(self, quantify):
        return self.save.CountReviewsFromIdGame(self.AppIDGame)  > quantify

    def getUnique(self) -> None:
        pass
        # divCardRowReviewUniquePlayer = self.divCardRow.find_element(By.CLASS_NAME, "apphub_Card")
        # geral = divCardRowReviewUniquePlayer.find_element(By.CLASS_NAME, "apphub_CardContentMain")
        # appReviews = geral.find_element(By.CLASS_NAME,"apphub_UserReviewCardContent") 
                            
        # self.getDescriptionForLikes(appReviews)
        # self.getDescriptionForVote(appReviews)
        # self.getDescriptionForRewiew(appReviews)

        # self.getPlayerInfo(divCardRowReviewUniquePlayer)
        # self.save.saveSteamPeople(self.playerInfo.getLinkPlayerSteam())
        # self.postIDReview = self.save.saveGameInformation(self.player, self.vote, self.likes, self.playerInfo, self.AppIDGame)
        # sleep(3)

        # self.getComments()

    def getGeral(self) -> None:
        for divCardRow in self.divCardRows:                
            divCardRowRewiewUniquePlayers = divCardRow.find_elements(By.CLASS_NAME, "apphub_Card")
        
            for divCardRowReviewUniquePlayer in divCardRowRewiewUniquePlayers:
                self.index+= 1
                geral = divCardRowReviewUniquePlayer.find_element(By.CLASS_NAME, "apphub_CardContentMain")
                appReviews = geral.find_element(By.CLASS_NAME,"apphub_UserReviewCardContent") 
                            
                self.getDescriptionForLikes(appReviews)
                self.getDescriptionForVote(appReviews)
                self.getDescriptionForRewiew(appReviews)

                self.getPlayerInfo(divCardRowReviewUniquePlayer)
                self.save.saveSteamPeople(self.playerInfo.getLinkPlayerSteam())
                self.postIDReview = self.save.saveGameInformation(self.player, self.vote, self.likes, self.playerInfo, self.AppIDGame)

                if self.getComments() == True:
                    sleep(3)                 
                    handles = self.driver.window_handles                    
                    self.driver.switch_to.window(handles[0])

                
        print("-"*100)
        
    def getScrollHeight(self) -> int:
        return self.driver.execute_script("return document.body.scrollHeight")

    def scroll(self):
        self.driver.execute_script(f"window.scrollTo(0,{self.getScrollHeight()})")
        sleep(2)      

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
        self.linkReviews = divCardRowRewiewUniquePlayerDriver.get_attribute("data-modal-content-url")        
        self.playerInfo = PlayerInfo(appPlayersInfo,self.linkReviews, self.driver)

    def getComments(self) -> bool:
        comentarios = self.playerInfo.clickQuantifyComment()

        if(len(comentarios) > 0):
            for comentario in comentarios:
                comment_ = Commnents()

                comentario[1] = comment_.formaterDate(comentario[1])
                comentario[2] = comment_.formaterComment(comentario[2])

                self.steamIDUser = self.save.saveSteamPeople(comentario[0])
                if self.steamIDUser != -1 and self.postIDReview != -1:
                    self.save.saveCommentsAboutReview(comentario[1], comentario[2], self.postIDReview, self.steamIDUser)
            return True

        return False
              