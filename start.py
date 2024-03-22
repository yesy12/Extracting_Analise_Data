
from time import sleep

from package.multiClass.Review import Review

link = "https://steamcommunity.com/app/678950/reviews/?browsefilter=toprated&snr=1_5_100010_"
infos = []

newReview = Review()
newReview.getLink(link)
newReview.gameActual()
newReview.saveGameTitle()


sleep(1)

newReview.setPageRow(1)
newReview.getGeral()
