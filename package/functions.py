import re
from datetime import datetime
 
 
regexDefault = "([A-z]| |á|ú|ç)+"
tableMonth = ["janeiro","fevereiro", "março", "abril", "maio", "junho","julho","agosto", "setembro", "outubro", "novembro", "dezembro"]

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
    date = re.split("de", date)
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
    
def addYearDatePublish(params):
    if len(params) == 2:
        params = params + [datetime.now().year]
    return params