
from functions import getIndexsFromMonthCommnets, splitSpecific, addYearDatePublish, subSpecificParams,searchText
from functions import addMonthDatePublish,addDayDatePublish

from logging import error

class Commnents:

    def __init__(self) -> None:
        pass
        
    def formaterDate(self, comentDate):
        exists = searchText("há \d+ horas", comentDate)
        
        if exists == None:            
            comentDate_ = splitSpecific(r"às \d+:\d+", comentDate)[0]
            if(len(comentDate_) == 13):
                comentDate_ = splitSpecific(r"/", comentDate_)

            elif(len(comentDate_) == 11):
                comentDate_ = splitSpecific(" de ", comentDate_)
                comentDate_[1] = comentDate_[1][0:4]
                        
            if type(comentDate_) == str:
                comentDate_ = splitSpecific("/", comentDate_)        

            # print(comentDate) ""
            # ['6 de fev. ']
            try:
                comentDate_[1] = getIndexsFromMonthCommnets(comentDate_[1])

                if len(comentDate_) == 3:
                    comentDate_[2] = int(comentDate_[2])
                else:
                    comentDate_ = addYearDatePublish(comentDate_)    

                return f"{comentDate_[0]}-{comentDate_[1]}-{comentDate_[2]}"
            except:
                error(f"Erro em data: {comentDate}")
                return "01-01-2000"

        else:
            comentDate = []
            comentDate.append(addDayDatePublish())
            comentDate.append(addMonthDatePublish())
            comentDate = addYearDatePublish(comentDate)
        
        return f"{comentDate[0]}-{comentDate[1]}-{comentDate[2]}"

    def formaterComment(self, commentText) -> str:
        return subSpecificParams("'","",commentText)

        
        

    