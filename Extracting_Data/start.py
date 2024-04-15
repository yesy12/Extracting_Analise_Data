
from time import sleep
from dotenv import load_dotenv
from package.multiClass.Review import Review
from os import getcwd, environ
import logging
load_dotenv()    

quantifyGames = int(environ["quantifyReviewFOrGames"])
languagesId = environ["languagesId"].split(",")

newReview = Review()
logging.basicConfig(
    filemode="w",
    filename="Extracting_Data/logs/log.log",
    encoding="utf-8",
    level=logging.INFO,
    format='%(pathname)s\n%(levelname)s Create: %(asctime)s Line: %(lineno)d %(funcName)s Level: %(levelno)s Log: %(message)s\n'
)


diretorioAtual = f"{getcwd()}/Extracting_Data/games.txt"

with open(diretorioAtual, "r", encoding="utf-8") as lines:
    for line in lines.readlines():    
        # logging.debug(f"Jogo: {line}")   
        newReview.getLink(line)
        newReview.driverApp.ageCheck()
        newReview.getAllReviews()
        sleep(2)
        newReview.getAndSaveGame()
        
        for id in languagesId:
            newReview.defineLanguage(id)

            sleep(3)

            i=0
            while True:
                sleep(2)
                i+= 1
                newReview.setPageRow(i)
                result = newReview.exitOnThisGame(quantifyGames)

                if result == True:
                    logging.debug("Proximo")
                    break   

                newReview.getGeral()
                    
                sleep(5)
                
                lastHeight = newReview.driverApp.getScrollHeight()
                newReview.driverApp.scroll(2)
                newScrollHeight = newReview.driverApp.getScrollHeight()

                if lastHeight == newScrollHeight or newScrollHeight == -1:
                    break

