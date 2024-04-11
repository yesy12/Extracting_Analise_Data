import re
from datetime import datetime
import names
from random import randint
from os import getcwd

from selenium.webdriver.common.by import By
 
regexDefault = "([A-z]| |á|ú|ç)+"
tableMonth = ["janeiro","fevereiro", "março", "abril", "maio", "junho","julho","agosto", "setembro", "outubro", "novembro", "dezembro"]
tableMonthComments = ["jan.","fev.", "mar.", "abr.", "mai.", "jun.","jul.","ago.", "set.", "out.", "nov.", "dez."]

default = re.compile(regexDefault)

def replace(text) -> str:
    result = default.sub(" ",text)
    return result

def replaceHours(text) -> str:
    result = re.sub(",","",text)
    return result

def replaceDateAndSplit(text):
    date = re.sub("Publicada: ","", text)
    date = re.sub(" ","", date)
    dezembro = searchText("dezembro",date)

    date = re.split("de", date)

    if dezembro:
        date[0] = date[0]
        date[1] = re.sub("zembro", "dezembro",date[2])
        date[2] = date[3]
        date.pop()

    date[0] = int(date[0])
    return date

def searchText(text, variable):
    return re.search(rf"{text}", variable)


def replaceJump(text) -> str:
    result = re.sub("\n", " " , text)
    return result

def split(text) -> str:
    result = default.split(text)
    return result

def splitSpecific(params, text) -> str:
    result = re.split(rf'{params}', text )
    return result

def getIndexsFromMonth(text) -> int:
    try:        
        index = tableMonth.index(text) + 1
        return index
    except:
        return -1
    
def getIndexsFromMonthCommnets(text) -> int:
    try:        
        index = tableMonthComments.index(text) + 1
        return index
    except:
        return -1    


def addYearDatePublish(params):
    if len(params) == 2:
        params = params + [datetime.now().year]
    return params

def addMonthDatePublish():
    return datetime.now().month

def addDayDatePublish():
    return datetime.now().day
    

def getRandomNickname() -> str:
    name = names.get_first_name()
    return f"{name}_{randint(1,100000)}"

def subSpecificParams(params, replace, text) -> str:
    result = re.sub(f"{params}", replace, text)
    return result

def saveToHtml(element, path, filename, mode="w"):
    pathComplete = f"{getcwd()}{path}{filename}"
    with open(pathComplete, mode, encoding="utf-8") as file:
        file.write(element)

def findElement(id):
    find = By.ID

    if id == 1:
        find = By.CLASS_NAME
    elif id == 2:
        find = By.TAG_NAME
    elif id == 3:
        find = By.XPATH

    return find