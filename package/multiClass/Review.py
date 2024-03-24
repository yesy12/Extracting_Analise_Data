from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pyodbc import Error as pyErr

import os

from os import path
from sys import path as path2

root_dir = path.dirname(path.abspath(__file__))
path2.append(path.join(root_dir, ".."))

from functions import getRandomNickname

from package.multiClass.Reviews.PlayerReviewDescription import PlayerReviewDescription

from package.multiClass.Descriptions.Likes import Likes
from package.multiClass.Descriptions.Vote import Vote

from package.multiClass.PlayerAboutInformation.PlayerInfos import PlayerInfo
from package.multiClass.PlayerAboutInformation.Comments.Comments import Commnents


from sql.credential import credential

class Review():

    def __init__(self, ) -> None:
        self.driver = webdriver.Edge()
        self.conection = credential()
        self.index = 0

        self.postIDReview = 0
        self.steamIDUser = 0

    def getLink(self, link) -> None:
        self.driver.get(link)

    def gameActual(self):
        div = self.driver.find_element(By.CLASS_NAME, "apphub_OtherSiteInfo")                   
        appID = div.find_element(By.CLASS_NAME, "btnv6_blue_hoverfade")
        self.AppIDGame = appID.get_attribute("data-appid") 
        self.linkGameSteam = appID.get_attribute("href")

        self.title = div = self.driver.find_element(By.CLASS_NAME, "apphub_AppName").text

    def setPageRow(self, pageIndex) -> None:
        pageRow = self.driver.find_element(By.ID, f"page{pageIndex}")
        print(f"Página: {pageIndex}")

        # self.divCardRows = pageRow.find_elements(By.XPATH,"//div[@class='apphub_CardRow' ]")
        self.divCardRow = pageRow.find_element(By.ID, "page_1_row_6_template_largeFallback")
   
    def getUnique(self) -> None:
        divCardRowReviewUniquePlayer = self.divCardRow.find_element(By.CLASS_NAME, "apphub_Card")
        geral = divCardRowReviewUniquePlayer.find_element(By.CLASS_NAME, "apphub_CardContentMain")
        appReviews = geral.find_element(By.CLASS_NAME,"apphub_UserReviewCardContent") 
                            
        self.getDescriptionForLikes(appReviews)
        self.getDescriptionForVote(appReviews)
        self.getDescriptionForRewiew(appReviews)

        self.getPlayerInfo(divCardRowReviewUniquePlayer)
        self.saveSteamPeople(self.playerInfo.getLinkPlayerSteam())
        self.saveGameInformation()
        sleep(3)

        self.getComments()

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
                self.saveSteamPeople(self.playerInfo.getLinkPlayerSteam())
                self.saveGameInformation() 
                
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

    def getComments(self) -> None:
        comentarios = self.playerInfo.clickQuantifyComment()
        print(self.postIDReview)

        if(len(comentarios) > 0):
            for comentario in comentarios:
                comment_ = Commnents()
                comentario[1] = comment_.formaterDate(comentario[1])
                comentario[2] = comment_.formaterComment(comentario[2])

                self.saveSteamPeople(comentario[0])
                self.saveCommentsAboutReview(comentario[1], comentario[2], self.postIDReview, self.steamIDUser)


    def saveGameTitle(self) -> None:
        sql = f"select TOP 1 * from gameCadastrado where id = {self.AppIDGame};"
        results = self.conection.select(sql)
        
        if (len(results) > 0) == False:
            sql = f""" insert into gameCadastrado (id, plataforma, titulo, link, dataCadastro, dataAlterado)
                values ({self.AppIDGame}, 1, '{self.title}', '{self.linkGameSteam}', GETDATE(),GETDATE());
            """
            try:
                self.conection.insert(sql)
                print(f"Cadastrado: {self.title}")
            except pyErr:
                print(pyErr)
                                
# # plataforma = self.conection.select("select top 1 id from dbo.plataforma where nome='Steam';")
    
    def saveSteamPeople(self, link) -> None:
        sql = f"select id from pessoaSteam where link = '{link}';"
        results = self.conection.select(sql)

        try:
            if(len(results) > 0) == False:
                sql = f"""insert into pessoaSteam(Nickname, link, relevancia) values ('{getRandomNickname()}', '{link}', 0)"""
                try:
                    self.conection.insert(sql)
                    self.conection.cursor.execute("SELECT SCOPE_IDENTITY() AS ID")
                    self.steamIDUser = self.conection.cursor.fetchone()[0]
                    print(f"Usuario cadastrado: {self.steamIDUser}")
                except pyErr:
                    print("-"*100)
                    print(f"SQL: {sql}")
                    print(f"Erro em usuario cadastrado: {pyErr}") 
                    print("-"*100)
            else:
                for row in results[0]:
                    self.steamIDUser = row
        except:
            print("Tabela não cadastradas")

    def saveGameInformation(self) -> None:
        sql = f"select TOP 1 id from pessoaSteam where link = '{self.playerInfo.getLinkPlayerSteam()}';"    
        results = self.conection.select(sql)
        result = 0

        for row in results[0]:
            result = row

        sql = f"""
            insert into reviewCompleta (
                descricao, horasJogadas, dataPublicada, 
                recomendado, pessoasAcharamUtil, pessoasAcharamEngracada, 
                pessoasReagiramEmoticon, quantidadesComentarios, quantidadeJogosNaConta, 
                idSteam, gameCadastrado)
	        values (
                '{self.player.getReviewAboutTheGame()}', {self.vote.getHoursPlayers()}, '{self.player.getPublishDay()}', 
                {self.vote.getRecomend()}, {self.likes.getLikesUtil()}, {self.likes.getLikesFunny()}, 
                {self.likes.getLikesEmoticon()}, {self.playerInfo.getQuantifyCommentAboutFromReview()},{self.playerInfo.getQuantifyGameFromPlayerReview()},
                {result}, {self.AppIDGame})
        """
        try:
            self.conection.insert(sql)
            self.conection.cursor.execute("SELECT SCOPE_IDENTITY() AS ID")
            self.postIDReview = self.conection.cursor.fetchone()[0]
            print(f"\tCadastrado: {self.index}")
        except pyErr:
                print("-"*100)
                print(f"SQL: {sql}")
                print(f"Erro em cadastrado de review: {pyErr}") 
                print("-"*100)
        
    def saveCommentsAboutReview(self, datePublished, commentText, idPostReview, idSteam) -> None:
        sql = f"""insert into reviewAboutComments(dataPublicada, comments, idPostReview, idSteam, dataCadastro, dataAlterado)
		values					('{datePublished}','{commentText}',{idPostReview},{idSteam}, GETDATE(), GETDATE())"""
        try:
            self.conection.insert(sql)
            print("\tComentario Publicado")
        except:
            print("Tabela não cadastrada")
              