from pyodbc import Error as pyErr
from sql.credential import credential
from package.functions import getRandomNickname

class Save:

    def __init__(self) -> None:
        self.connection = credential()

    def saveGameTitle(self, idGame, title, linkGameSteam) -> bool:
        sql = f"select TOP 1 * from gameCadastrado where id = {idGame};"
        results = self.connection.select(sql)

        if (len(results) > 0) == False:
            sql = f""" insert into gameCadastrado (id, plataforma, titulo, link, dataCadastro, dataAlterado) values ({idGame}, 1, '{title}', '{linkGameSteam}', GETDATE(),GETDATE());"""
            try:
                self.connection.insert(sql)
                print(f"Cadastrado: {title}")
            except pyErr:
                print(pyErr)

    def saveSteamPeople(self, link) -> int:
        sql = f"select id from pessoaSteam where link = '{link}';"
        results = self.connection.select(sql)

        try:
            if(len(results) > 0) == False:
                sql = f"""insert into pessoaSteam(Nickname, link, relevancia) values ('{getRandomNickname()}', '{link}', 0)"""
                try:
                    self.connection.insert(sql)
                    self.connection.cursor.execute("SELECT SCOPE_IDENTITY() AS ID")

                    steamIDUser = self.connection.cursor.fetchone()[0]
                    print(f"Usuario cadastrado: {steamIDUser}")
                    return steamIDUser
                
                except pyErr:
                    print("-"*100)
                    print(f"SQL: {sql}")
                    print(f"Erro em usuario cadastrado: {pyErr}") 
                    print("-"*100)
                    return -1
            else:
                for row in results[0]:
                    return row

        except:
            print("Tabela não cadastradas") 
            return -1                      

    def saveGameInformation(self, player, vote, likes, playerInfo, idGame, index) -> None:
        sql = f"select TOP 1 id from pessoaSteam where link = '{playerInfo.getLinkPlayerSteam()}';"    
        results = self.connection.select(sql)
        result = 0

        for row in results[0]:
            result = row

        sql = f"""
            insert into reviewCompleta (descricao, horasJogadas, dataPublicada, recomendado, pessoasAcharamUtil, pessoasAcharamEngracada, pessoasReagiramEmoticon, quantidadesComentarios, quantidadeJogosNaConta, idSteam, gameCadastrado)
	        values (
                '{player.getReviewAboutTheGame()}', {vote.getHoursPlayers()}, '{player.getPublishDay()}', 
                {vote.getRecomend()}, {likes.getLikesUtil()}, {likes.getLikesFunny()}, 
                {likes.getLikesEmoticon()}, {playerInfo.getQuantifyCommentAboutFromReview()},{playerInfo.getQuantifyGameFromPlayerReview()},
                {result}, {idGame})
        """

        try:
            self.connection.insert(sql)
            self.connection.cursor.execute("SELECT SCOPE_IDENTITY() AS ID")
            postIDReview = self.connection.cursor.fetchone()[0]
            print(f"\tCadastrado: {index}")
            return postIDReview
        except pyErr:
                print("-"*100)
                print(f"SQL: {sql}")
                print(f"Erro em cadastrado de review: {pyErr}") 
                print("-"*100)        

    def saveCommentsAboutReview(self, datePublished, commentText, idPostReview, idSteam) -> None:
        sql = f"""insert into reviewAboutComments(dataPublicada, comments, idPostReview, idSteam, dataCadastro, dataAlterado)
		values					('{datePublished}','{commentText}',{idPostReview},{idSteam}, GETDATE(), GETDATE())"""
        try:
            self.connection.insert(sql)
            print("\tComentario Publicado")
        except pyErr:
            print(f"Error: {pyErr}")
            print("Tabela não cadastrada")