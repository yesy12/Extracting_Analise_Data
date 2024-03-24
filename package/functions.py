import re
from datetime import datetime
import names
from random import randint
 
 
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
    dezembro = re.search("dezembro",date)

    date = re.split("de", date)

    if dezembro:
        date[0] = date[0]
        date[1] = re.sub("zembro", "dezembro",date[2])
        date[2] = date[3]
        date.pop()

    date[0] = int(date[0])
    return date

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

def getRandomNickname() -> str:
    name = names.get_first_name()
    return f"{name}_{randint(1,100000)}"

def subSpecificParams(params, replace, text) -> str:
    result = re.sub(f"{params}", replace, text)
    return result