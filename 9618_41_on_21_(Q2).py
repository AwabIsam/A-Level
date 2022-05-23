from tkinter import Y


class Picture():
    # Description STRING
    # Width INTEGER
    # Height INTEGER
    # FrameColour STRING
    def __init__(self, Description, Width, Height, Framecolour):
        self.__Description = Description 
        self.__Width = int(Width)
        self.__Height = int(Height)
        self.__FrameColour = Framecolour

    
    def GetDescription(self):
        return self.__Description
    
    def GetHeight(self):
        return self.__Height

    def GetWidth(self):
        return self.__Width

    def GetColour(self):
        return self.__FrameColour

    def setDescription(self, nDescription):
        self.__Description = nDescription


PictureArray = [Picture("", 0, 0, "") for i in range(100)]


def ReadData():
    global PictureArray
    y = 0
    filename = "Pictures.txt"
    try:
        with open(filename, "r") as file:
            data = file.readline().strip().lower()
            while data != "" and y != 100:
                Desc = data.lower()
                Width = int(file.readline().strip())
                Height = int(file.readline().strip())
                FrameColour = file.readline().strip().lower()
                PictureArray[y] = Picture(Desc, Width, Height, FrameColour)
                y += 1
                data = file.readline().strip().lower()
    except FileNotFoundError:
        print("File not found")
    return y, PictureArray


NumofPic, PictureArray = ReadData()

ColourofFrame = input("Enter Colour of Frame: ").lower()
WidthofPic = int(input("Enter Width: "))
HeightofPic = int(input("Enter Height: "))




for x in range(NumofPic):
    if ColourofFrame == PictureArray[x].GetColour():
        if WidthofPic >= PictureArray[x].GetWidth():
            if HeightofPic >= PictureArray[x].GetHeight():
                print(PictureArray[x].GetDescription(), PictureArray[x].GetWidth(), PictureArray[x].GetHeight())
