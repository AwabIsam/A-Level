class TreasureChest:
    def __init__(self, question, answer, points):
        self.__question = question  # STRING
        self.__answer = int(answer)      # INTEGER
        self.__points = int(points)      # INTEGER

    def getQuestion(self):
        return self.__question
        
    def checkAnswer(self, Uanswer):
        if Uanswer == self.__answer:
            return True
        else:
            return False

    def getPoints(self, Attempts):
        if Attempts == 1:
            return self.__points
        elif Attempts == 2:
            return ((self.__points) // 2)
        elif Attempts == 3 or Attempts == 4:
            return ((self.__points) // 4)
        else:
            return 0

TreasureArray = []

def readData():
    global TreasureArray
    filename = "TreasureChestData.txt"
    try:
        with open(filename, "r") as file:
            data = file.readline().strip()
            while data != "":
                question = data
                answer = int(file.readline().strip())
                points = int(file.readline().strip())
                TreasureArray.append(TreasureChest(question, answer, points))
                data = file.readline().strip()
    except FileNotFoundError:
        print("File Not Found")


readData()
qNum = int(input("Enter a question number: "))
if qNum > 0 and qNum < 6:

    result = False
    Attempts = 0
    while not result:
        print(TreasureArray[qNum - 1].getQuestion())
        answer = int(input("Enter Answer: "))
        result = TreasureArray[qNum -1].checkAnswer(answer)
        Attempts += 1
print(TreasureArray[qNum- 1].getPoints(Attempts))


