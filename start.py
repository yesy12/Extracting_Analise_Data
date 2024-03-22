
from time import sleep

from package.multiClass.Review import Review
# from sql.credential import credential

# new =credential()
# new.initStructure()

link = "https://steamcommunity.com/app/678950/reviews/?browsefilter=toprated&snr=1_5_100010_"
infos = []

newReview = Review()
newReview.getLink(link)
newReview.gameActual()
newReview.saveGameTitle()


# sleep(5)

# newReview.setPageRow(1)
# newReview.getGeral()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Edge()
# link = "https://steamcommunity.com/app/678950/reviews/?browsefilter=toprated&snr=1_5_100010_"
# driver.get(link)

# div = driver.find_element(By.CLASS_NAME, "apphub_AppName")                   



