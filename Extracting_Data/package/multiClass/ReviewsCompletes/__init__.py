from .Descriptions.Vote import Vote
from .Descriptions.Likes import Likes

from .PlayerAboutInformation.PlayerInfos import PlayerInfo
from .PlayerAboutInformation.PlayerInfosReviewComments import PlayerInfosReviewComments

from .Reviews.PlayerReviewDescription import PlayerReviewDescription
from selenium.webdriver.common.by import By

def getDescriptionForLikes(element) -> None:
    found = element.find_element(By.CLASS_NAME, "found_helpful").text
    likes = Likes(found)
    return likes

def getDescriptionForVote(element) -> None:
    voteHeader = element.find_element(By.CLASS_NAME, "vote_header")
    return Vote(voteHeader)

def getDescriptionForRewiew(element) -> None:
    cardContextReview = element.find_element(By.CLASS_NAME, "apphub_CardTextContent")
    return PlayerReviewDescription(cardContextReview)

    
def getPlayerInfo(element, driver) -> None:
    appPlayersInfo = element.find_element(By.CLASS_NAME,"apphub_CardContentAuthorBlock")
    linkReviews = element.get_attribute("data-modal-content-url")       
    return PlayerInfo(appPlayersInfo,linkReviews, driver)




