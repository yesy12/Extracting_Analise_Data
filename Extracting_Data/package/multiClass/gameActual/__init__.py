from selenium.webdriver.common.by import By

class gameActual:

    def __init__(self, driverApp) -> None:
        self.driver = driverApp

    def getGame(self):
        
        div = self.driver.find_element(By.CLASS_NAME, "apphub_OtherSiteInfo")                   
        appID = div.find_element(By.CLASS_NAME, "btnv6_blue_hoverfade")

        try:
            AppIDGame = int(appID.get_attribute("data-appid"))            
        except:
            appID = 0

        linkGameSteam = appID.get_attribute("href")

        title = div = self.driver.find_element(By.CLASS_NAME, "apphub_AppName").text

        return [title, AppIDGame, linkGameSteam]
        