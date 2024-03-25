from selenium.webdriver.common.by import By

from logging import error, debug

class PlayerInfosReviewComments:

    def __init__(self,driverApp ,link) -> None:
        self.driverApp = driverApp
        self.link = link
        

    def openNewTab(self) -> None:
        self.driverApp.execute_script(f"window.open('{self.link}', '_blank');")
        handles = self.driverApp.window_handles
        self.driverApp.switch_to.window(handles[1])

    def getComentarios(self) -> None:
        comentariosPublicados = []
        try:
            divComentarios = self.driverApp.find_element(By.CLASS_NAME, "commentthread_comments")
            divComentario = divComentarios.find_elements(By.CLASS_NAME, "commentthread_comment")

            for div in divComentario:
                divComentContent = div.find_element(By.CLASS_NAME, "commentthread_comment_content")

                Author = divComentContent.find_element(By.CLASS_NAME, "commentthread_comment_author")
                link = Author.find_element(By.CLASS_NAME, "hoverunderline").get_attribute("href")

                publish = divComentContent.find_element(By.CLASS_NAME, "commentthread_comment_timestamp").text

                comentario = divComentContent.find_element(By.CLASS_NAME, "commentthread_comment_text").text

                comentariosPublicados.append([link, publish, comentario])
        except:
            error("Erro no comentarios")

        return comentariosPublicados

    def closeTab(self) -> None:
        debug("Fechado")
        self.driverApp.close()