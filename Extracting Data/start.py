
from time import sleep

from package.multiClass.Review import Review

# link = "https://steamcommunity.com/app/678950/reviews/?browsefilter=toprated&snr=1_5_100010_"
link = "https://steamcommunity.com/app/1310410/reviews/?browsefilter=toprated&snr=1_5_100010_"
infos = []

newReview = Review()
newReview.getLink(link)
newReview.gameActual()

for i in range(1,1000):
    sleep(1)
    newReview.setPageRow(i)
    newReview.getGeral()

    lastHeight = newReview.getScrollHeight()
    newReview.scroll()
    newScrollHeight = newReview.getScrollHeight()

    if lastHeight == newScrollHeight:
        break

