
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
        newReview.ageCheck()
        newReview.getAllReviews()
        sleep(2)
        newReview.gameActual()

        for i in range(1,10000):
            sleep(1)
            newReview.setPageRow(i)
            result = newReview.exitOnThisGame(1000)

            if result == True:
                logging.debug("Proximo")
                break   

            newReview.getGeral()

            lastHeight = newReview.getScrollHeight()
            newReview.scroll()
            newScrollHeight = newReview.getScrollHeight()

            if lastHeight == newScrollHeight:
                break

