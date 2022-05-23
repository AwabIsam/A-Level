arraydata =[10, 5, 6, 7, 1, 12, 13, 15, 21, 28] 


def linearsearch(key):
    for i in range(len(arraydata)):
        if key == arraydata[i]:
            return True


key = int(input("Enter Item to search; "))
returnValue = linearsearch(key)
if returnValue == True:
    print("Item Found")
else:
    print("Item not Found")


def bubblesort():
    for x in range(len(theArray)):
        for y in range(len(theArray)):
            if theArray[y] < theArray[y+1]:
                temp = theArray[y]
                theArray[y] = theArray[y+1]
                theArray[y + 1] = temp



