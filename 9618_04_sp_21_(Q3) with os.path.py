import os


QueueData = ["" for i in range(20)]
StartPointer = 0
EndPointer = -1


def Enqueue(Item):
    global EndPointer
    if EndPointer == 19:
        return False
    else:
        EndPointer += 1
        QueueData[EndPointer] = Item
        return True


def ReadFile():
    filename = input("Enter File Name: ")
    if os.path.isfile(filename):
        with open(filename, "r") as file:
            DataToInsert = (file.readline()).strip()
            Flag = True
            while DataToInsert != "" and Flag:
                Flag = Enqueue(DataToInsert)
                DataToInsert = file.readline().strip()
            if Flag:
                return 2
            elif not Flag:
                return 1
    else:
        return -1


ReturnValue = ReadFile()
if ReturnValue == 2:
    print("all items were added to the queue")
elif ReturnValue == 1:
    print("the queue was full")
elif ReturnValue == -1:
    print("the textfile could not be found")


