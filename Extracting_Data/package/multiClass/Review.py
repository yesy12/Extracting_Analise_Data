from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from os import path
from sys import path as path2

root_dir = path.dirname(path.abspath(__file__))
path2.append(path.join(root_dir, ".."))


from package.multiClass.SaveOnDatabase.Save import Save

from .driverApp import DriverApp as driverAppFunctions
from .gameActual import gameActual 
import package.multiClass.ReviewsCompletes as rc

import logging

from functions import saveToHtml

class Review():

    def __init__(self, ) -> None:
        self.driver = webdriver.Edge()
        self.index = 0
        self.save = Save()

        self.driverApp = driverAppFunctions(self.driver)
        self.game = gameActual(self.driver)

        self.postIDReview = 0
        self.steamIDUser = 0
        self.AppIDGame = 0
        self.LanguageId = 0 
        self.linkReference = ""

    def getLink(self, link) -> None:
        self.driver.get(link)

    def getLinkLanguage(self, params):
        print(f"Idioma Params: "+params)
        self.driver.get( self.driver.current_url + f"&filterLanguage={params}")

    def getAllReviews(self)-> None:
        self.driverApp.scrollInfinite(5)
        
        sleep(2)
        logging.debug("Get all reviews page")
        allReview = self.driverApp.returnElement(20, 1, "view_all_reviews_btn")
        allReview.click()
        self.driverApp.verifyContentSexualGame()

    def getAndSaveGame(self):
        title,self.AppIDGame, link = self.game.getGame()
        self.save.saveGameTitle(self.AppIDGame, title, link)

    def exitOnThisGame(self, quantify):
        try:
            return self.save.CountReviewsFromIdGame(self.AppIDGame, self.LanguageId)  > quantify
        except:
            return False

    def setPageRow(self, pageIndex, indexUnique=False) -> None:
        self.pageIndex = pageIndex
        pageRow = self.driver.find_element(By.ID, f"page{pageIndex}")
        print(f"Page: {pageIndex}")

        saveToHtml(pageRow.get_attribute('innerHTML'),"/Extracting_Data/htmls/pageId/", f"page_{pageIndex}.html")

        self.divCardRows = pageRow.find_elements(By.XPATH,"//div[@class='apphub_CardRow' ]")

    def defineLanguage(self, idLanguage):
        self.LanguageId = idLanguage
        self.linkReference = self.save.getLinkRefenceLanguage(self.LanguageId)
        self.getLinkLanguage(self.linkReference)
       

    def getGeral(self) -> None:
        for divCardRow in self.divCardRows:                
                divCardRowRewiewUniquePlayers = divCardRow.find_elements(By.CLASS_NAME, "apphub_Card")

                for divCardRowReviewUniquePlayer in divCardRowRewiewUniquePlayers:
                    self.index += 1                        
                    geral = divCardRowReviewUniquePlayer.find_element(By.CLASS_NAME, "apphub_CardContentMain")

                    appReviews = geral.find_element(By.CLASS_NAME,"apphub_UserReviewCardContent")                                 
                                
                    self.likes = rc.getDescriptionForLikes(appReviews)
                    self.vote = rc.getDescriptionForVote(appReviews)
                    self.player = rc.getDescriptionForRewiew(appReviews)
                    self.playerInfo = rc.getPlayerInfo(divCardRowReviewUniquePlayer, self.driver)

                    if self.save.getReviewForLink(self.playerInfo.linkNew) == False:
                        self.steamIDUser = self.save.saveSteamPeople(self.playerInfo.getLinkPlayerSteam())
                        self.postIDReview = self.save.saveGameInformation(self.player, self.vote, self.likes, self.playerInfo, self.AppIDGame, self.LanguageId)
                    
                    # if self.getComments() == True:                    
                    #     sleep(3)                
                    #     logging.debug("Comment") 
                    #     handles = self.driver.window_handles                    
                    #     self.driver.switch_to.window(handles[0])
                
        print("-"*100)
        




    # def getComments(self) -> bool:
    #     getCommentsBool = self.save.getSaveLinkReviewsCommentsRegistered(self.playerInfo.linkNew)

    #     if( getCommentsBool == False):
    #         comentarios = self.playerInfo.clickQuantifyComment()

    #         if(len(comentarios) > 0):
    #             self.save.saveLinkReviewsComments(self.playerInfo.linkNew, self.postIDReview, self.AppIDGame, self.steamIDUser)        

    #             for comentario in comentarios:
    #                 comment_ = Commnents()

    #                 comentario[1] = comment_.formaterDate(comentario[1])
    #                 comentario[2] = comment_.formaterComment(comentario[2])

    #                 self.steamIDUser = self.save.saveSteamPeople(comentario[0])
    #                 if self.steamIDUser != -1 and self.postIDReview != -1:
    #                     self.save.saveCommentsAboutReview(comentario[1], comentario[2], self.postIDReview, self.steamIDUser)
    #             return True
    #     else:
    #         logging.info("Exists comments on database")
    #     return False
              