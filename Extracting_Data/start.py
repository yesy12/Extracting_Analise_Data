
from time import sleep

from package.multiClass.Review import Review
from os import getcwd
import logging


newReview = Review()
logging.basicConfig(
    filemode="w",
    filename="Extracting_Data/logs/log.log",
    encoding="utf-8",
    level=logging.INFO
)


diretorioAtual = f"{getcwd()}/Extracting_Data/games.txt"

with open(diretorioAtual, "r", encoding="utf-8") as lines:
    for line in lines.readlines():    
        logging.debug(f"Jogo: {line}")   

        newReview.getLink(line)
        newReview.driverApp.ageCheck()
        newReview.getAllReviews()

        sleep(2)
        newReview.getAndSaveGame()

        for i in range(1,10000):
            sleep(1)
            newReview.setPageRow(i)
            result = newReview.exitOnThisGame(100000)

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

