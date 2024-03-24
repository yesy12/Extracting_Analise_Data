
from functions import getIndexsFromMonthCommnets, splitSpecific, addYearDatePublish, subSpecificParams

class Commnents:

    def __init__(self) -> None:
        pass
        
    def formaterDate(self, comentDate) -> str:
        comentDate = splitSpecific(r"às \d+:\d+", comentDate)[0]
        if(len(comentDate) == 13):
            comentDate = splitSpecific(r"/", comentDate)

        elif(len(comentDate) == 11):
            comentDate = splitSpecific(" de ", comentDate)
        
        comentDate[1] = getIndexsFromMonthCommnets(comentDate[1][0:4])
        comentDate[0] = int(comentDate[0])
        if len(comentDate) == 3:
            comentDate[2] = int(comentDate[2])

        comentDate = addYearDatePublish(comentDate)
        return f"{comentDate[0]}-{comentDate[1]}-{comentDate[2]}"

    def formaterComment(self, commentText) -> str:
        return subSpecificParams("'","",commentText)

        
        

    