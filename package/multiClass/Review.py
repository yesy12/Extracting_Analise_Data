from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from package.multiClass.PlayerReviewDescription import PlayerReviewDescription
from package.multiClass.Likes import Likes
from package.multiClass.Vote import Vote
from package.multiClass.PlayerInfos import PlayerInfo

from sql.credential import credential

class Review():

    def __init__(self, ) -> None:
        self.driver = webdriver.Edge()
        self.conection = credential()
        self.index = 0

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

        self.divCardRows = pageRow.find_elements(By.XPATH,"//div[@class='apphub_CardRow' ]")
   
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
                self.saveSteamPeople()
                self.saveGameInformation() 
        
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
        self.playerInfo = PlayerInfo(appPlayersInfo)

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
            except pyodbc.Error as Error:
                print(Error)
                
                
        # # plataforma = self.conection.select("select top 1 id from dbo.plataforma where nome='Steam';")
    
    def saveSteamPeople(self) -> None:
        sql = f"select * from pessoaSteam where link = '{self.playerInfo.getLinkPlayerSteam()}';"        
        results = self.conection.select(sql)
        
        if(len(results) > 0) == False:
            sql = f"""
            insert into pessoaSteam(
                Nickname, link, relevancia) 
            values ('{self.playerInfo.getRandomNickname()}', '{self.playerInfo.getLinkPlayerSteam()}', 0)
            """
            try:
                self.conection.insert(sql)
                print("Usuario cadastrado")
            except pyodbc.Error as Error:
                print(Error) 

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
            print(f"\tCadastrado: {self.index}")
        except pyodbc.Error as Error:
            print(Error)
        
        