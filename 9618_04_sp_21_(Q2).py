class HiddenBox:
    # __BoxName STRING
    # __Creator STRING
    # __DateHidden STRING
    # __GameLocation STRING
    # __LastFinds [10] [2] STRING
    # __Active BOOLEAN
    def __init__(self, BoxName,  Creator, DateHidden, GameLocation):
        self.__BoxName = BoxName
        self.__Creator = Creator
        self.__DateHidden = DateHidden
        self.__GameLocation = GameLocation
        self.__LastFinds = [["" for i in range(2)] in range(10)]
        self.__Active = False

    def GetBoxName(self):
        return self.__Boxname
    
    def GetGameLocation(self):
        return self.__GameLocation

    
TheBoxes = [HiddenBox("","","","") for x in range(10000)]

def NewBox(TheBoxes, BoxPointer):
    Name = input("Enter Name")
    Creator = input("Enter Creator")
    DateHidden = input("Enter Date Hidden")   
    GameLocation = input("Enter Game Location")
    TheBoxes[BoxPointer] = HiddenBox(Name, Creator, DateHidden,GameLocation)
    return (BoxPointer + 1)



NewBox()


class PuzzleBox(HiddenBox):
    # PuzzleText STRING
    # Solutino STRING
    def __init__(self, BoxName,  Creator, DateHidden, GameLocation, PuzzleText, Solution):
        super().__init__(BoxName,  Creator, DateHidden, GameLocation)
        self.__PuzzleText = PuzzleText
        self.__Soltion = Solution
    
