
from time import sleep

from package.multiClass.Review import Review
from os import getcwd
# # link = "https://steamcommunity.com/app/678950/reviews/?browsefilter=toprated&snr=1_5_100010_"
link = "https://store.steampowered.com/app/2420110/Horizon_Forbidden_West__Edio_Completa/"
# diretorioAtual = f"{getcwd()}/Extracting_Data/games.txt"
# print(diretorioAtual)
# with open(diretorioAtual, "r", encoding="utf-8") as lines:
#     for line in lines.readlines():
#         print(line)


newReview = Review()
newReview.getLink(link)
newReview.ageCheck()
newReview.getAllReviews()
sleep(2)
newReview.gameActual()

for i in range(1,1000):
    sleep(1)
    newReview.setPageRow(i)
    result = newReview.exitOnThisGame(120)

    if result == True:
        print("Proximo")
        break   

    newReview.getGeral()

    lastHeight = newReview.getScrollHeight()
    newReview.scroll()
    newScrollHeight = newReview.getScrollHeight()

    if lastHeight == newScrollHeight:
        break

