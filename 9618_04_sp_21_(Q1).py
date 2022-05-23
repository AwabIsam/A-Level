TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]


def InsertionSort(TheData):
    for count in range(len(TheData)):
        DataToInsert = TheData[count]
        Inserted = 0 
        NextValue = count - 1
        while NextValue >= 0 and Inserted != 1:
            if DataToInsert < TheData[NextValue]:
                TheData[NextValue + 1] = TheData[NextValue]
                NextValue -= 1
                TheData[NextValue + 1] = DataToInsert
            else:
                Inserted = 1


def Print():
    for i in range(len(TheData)):
        print("[", TheData[i], "]", end="")


def Search():
    key = int(input("Enter a Whole Number: "))
    for i in range(len(TheData)):
        if TheData[i] == key:
            print("found")
            return True
    else:
        print("not found")
        return False

print("Before Sorting")
print("--------------")
Print()
InsertionSort(TheData)
print("--------------")
print("After Sorting")
print("--------------")
Print()
print("--------------")
Search()

