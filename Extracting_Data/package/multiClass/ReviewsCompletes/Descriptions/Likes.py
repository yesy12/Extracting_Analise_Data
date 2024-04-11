from selenium.webdriver.common.by import By
from package.functions import replaceJump,split
from math import floor

from logging import warning

class Likes:

    def __init__(self, driverApp) -> None:
        self.driverApp = driverApp
        found = replaceJump(self.driverApp)  

        self.foundSplit = split(found)      
    
    def getLikesEmoticon(self) -> int:
        try:
            return int( self.foundSplit[ len( self.foundSplit) -1 ] )
        except:
            warning(f"{self.foundSplit} with errors: Emoticon")
            return 0
    
    def getLikesFunny(self) -> int:
        try:
            return int(self.foundSplit[ floor( len(self.foundSplit)/2 ) ] )
        except:
            warning(f"{self.foundSplit} with errors: Funny")
            return 0
    
    def getLikesUtil(self) -> int:
        try:
            return int(self.foundSplit[0])
        except:
            warning(f"{self.foundSplit} with errors: Util")
            return 0