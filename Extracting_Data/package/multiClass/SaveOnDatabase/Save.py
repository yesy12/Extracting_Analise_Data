from pyodbc import Error as pyErr, IntegrityError
from sql.credential import credential
from package.functions import getRandomNickname, subSpecificParams

from logging import info, debug, critical, error

class Save:

    def __init__(self) -> None:
        self.connection = credential()

    def saveGameTitle(self, idGame, title, linkGameSteam) -> bool:
        sql = f"select TOP 1 * from gameCadastrado where id = '{idGame}';"
        results = self.connection.select(sql)

        try:
            if ( len(results) > 0) == False:
                title = subSpecificParams("'",'"', title)
                
                sql = f""" insert into gameCadastrado (id, plataforma, titulo, link, dataCadastro, dataAlterado) values ({idGame}, 1, '{title}', '{linkGameSteam}', GETDATE(),GETDATE());"""
                try:
                    self.connection.insert(sql)
                    debug(f"Registered: {title}")
                except pyErr:
                    critical(f"Error on Registered title on database: {pyErr}")
        except:
            error("Erro")          
             
    def saveSteamPeople(self, link) -> int:
        sql = f"select TOP 1 id,relevancia from pessoaSteam where link = '{link}';"
        results = self.connection.select(sql)

        try:
            if(len(results) > 0) == False:
                sql = f"""insert into pessoaSteam(Nickname, link, relevancia) values ('{getRandomNickname()}', '{link}', 0)"""
                try:
                    self.connection.insert(sql)
                    self.connection.cursor.execute("SELECT SCOPE_IDENTITY() AS ID")

                    steamIDUser = self.connection.cursor.fetchone()[0]
                    debug(f"\t\tUsuario cadastrado: {steamIDUser}")
                    return steamIDUser
                
                except IntegrityError as ite:
                    print("h")
                    error("*"*100)
                    error(f"Erro: {ite}")
                
                except pyErr:
                    critical("-"*100)
                    critical(f"SQL: {sql}")
                    critical(f"Error on Registered users: {pyErr}") 
                    critical("-"*100)
                    return -1
                

            else:
                id = results[0][0]
                relevancia = results[0][1]

                sql = f"update pessoaSteam set relevancia = {relevancia} + 1 where link = '{link}';"
                self.connection.insert(sql)

                debug(f"\t\tRelevância alterada de: {relevancia} para: {relevancia+1}")
                return id
            
        except pyErr:
            critical(f"Error on Save.SaveSteamPeople: {pyErr}")
            return -1                      

    def saveGameInformation(self, player, vote, likes, playerInfo, idGame) -> None:
        sql = f"select TOP 1 id from pessoaSteam where link = '{playerInfo.getLinkPlayerSteam()}';"    
        results = self.connection.select(sql)
        result = 0

        for row in results[0]:
            result = row

        sql = f"""
            insert into reviewCompleta (descricao, horasJogadas, dataPublicada, recomendado, pessoasAcharamUtil, pessoasAcharamEngracada, pessoasReagiramEmoticon, quantidadesComentarios, quantidadeJogosNaConta, idSteam, gameCadastrado, linkSteamReview)
	        values (
                '{player.getReviewAboutTheGame()}', {vote.getHoursPlayers()}, '{player.getPublishDay()}', 
                {vote.getRecomend()}, {likes.getLikesUtil()}, {likes.getLikesFunny()}, 
                {likes.getLikesEmoticon()}, {playerInfo.getQuantifyCommentAboutFromReview()},{playerInfo.getQuantifyGameFromPlayerReview()},
                {result}, {idGame}, '{playerInfo.linkNew}')
        """
        try:
            self.connection.insert(sql)
            self.connection.cursor.execute("SELECT SCOPE_IDENTITY() AS ID")
            postIDReview = self.connection.cursor.fetchone()[0]
            debug(f"\tReview Registered : {postIDReview}")
            return postIDReview        
        
        except IntegrityError as ite:
            error("*"*100)
            error(f"Erro: {ite}")
            
        except pyErr:
            critical("-"*100)
            critical(f"SQL: {sql}")
            critical(f"Error on Review Registered: {pyErr}") 
            critical("-"*100)        

    def saveCommentsAboutReview(self, datePublished, commentText, idPostReview, idSteam) -> None:
        sql = f"""insert into reviewAboutComments(dataPublicada, comments, idPostReview, idSteam, dataCadastro, dataAlterado)
		values					('{datePublished}','{commentText}',{idPostReview},{idSteam}, GETDATE(), GETDATE())"""
        try:
            self.connection.insert(sql)
            self.connection.cursor.execute("SELECT SCOPE_IDENTITY() AS ID")
            comentIDReview = self.connection.cursor.fetchone()[0]
            debug(f"\t\tComentario Cadastrado: {comentIDReview}")
        except pyErr:
            critical(f"Error: {pyErr}")
            critical("Tabela não cadastrada")

    def CountReviewsFromIdGame(self, idGame):
        sql = f"select TOP 1 count(id) from reviewCompleta where gameCadastrado = '{idGame}';"
        results = self.connection.select(sql)

        count = results[0][0]
        return count
    
    def getSaveLinkReviewsCommentsRegistered(self, link) -> bool:
        sql = f"select TOP 1 id from commentRegistered where linkSteamReviewComment ='{link}';"
        results = self.connection.select(sql)

        if(len(results) > 0):
            return True
        else:
            return False
    
    def saveLinkReviewsComments(self, link, postIDSteamReview, idSteamGame,idSteamPeoplePostReview):
        if self.getSaveLinkReviewsCommentsRegistered(link) == False:
            sql = f"insert into commentRegistered(linkSteamReviewComment, postIDSteamReview, idSteamGame, idSteamPeoplePostReview) values ('{link}',{postIDSteamReview}, {idSteamGame}, {idSteamPeoplePostReview});"
            self.connection.insert(sql)

            info("Registered steam page comment on database")