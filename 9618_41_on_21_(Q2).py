class Picture():
    # Description STRING
    # Width INTEGER
    # Height INTEGER
    # FrameColour STRING
    def __init__(self, Description, Width, Height, Framecolour):
        self.__Description = Description 
        self.__Width = Width
        self.__Height = Height
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


PictureArray = [Picture("", "", "", "") for i in range(100)]


def ReadData():
    i = 0
    filename = "Pictures.txt"
    try:
        with open(filename, "r") as file:
            data = file.readline().strip()
            while data != "" and i != 100:
                Desc = data
                Width = file.readline().strip()
                Height = file.readline().strip()
                FrameColour = file.readline().strip()
                PictureArray[i] = Picture(Desc, Width, Height, FrameColour)
                i += 1
                desc = file.readline().strip()
    except FileNotFoundError:
        print("File not found")
    return i, PictureArray


NumofPic, PictureArray = ReadData()

ColourofFrame = input("Enter Colour of Frame: ")
WidthofPic = int(input("Enter Width: "))
HeightofPic = int(input("Enter Height: "))

found = False



for x in range(NumofPic):
    PFrame = PictureArray[x].GetColour
    PWidth = PictureArray[x].GetWidth
    PHeight = PictureArray[x].GetHeight
    if ColourofFrame == PFrame:
        if WidthofPic >= PWidth:
            if HeightofPic >= PHeight:
                print(PictureArray[x].GetDescription, PictureArray[x].GetWidth, PictureArray[x].GetHeight )
else:
    print("ssss")

