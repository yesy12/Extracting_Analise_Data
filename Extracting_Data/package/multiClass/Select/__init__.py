from selenium.webdriver.support.ui import Select
from functions import findElement

class Select_s:

    def __init__(self, driver):
        self.driver = driver
    
    def setSelector(self, type, element, index):
        find = findElement(type)

        selected = Select(self.driver.find_element(find,element))
        selected.select_by_index(index)