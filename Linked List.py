n = int(input("How many values do you wish to enter: "))

mll = [None for i in range(0, n)]
mllp = [None for i in range(0, n)]

for i in range(0, n):
    mllp[i] = i + 1


mllp[n - 1] = -1
sp = -1
hp = 0
np = -1
temp = 0
itemp = -1


def insert(x):
    global sp, hp, np, temp, itemp
    if hp != np:
        itemp = itemp + 1
        temp = sp
        sp = hp
        hp = mllp[hp]
        mll[sp] = x
        mllp[sp] = temp
        print(hp, ",", sp, ",", temp)
        print(mll)
        print(mllp)
        print("Item Position : ", itemp)
    else:
        print("Linked List is Full - can't insert")


found = False


def searchll(xs):
    global itemp, sp, np, found
    found = False
    itemp = sp
    while itemp != np and not found:
        if mll[itemp] == xs:
            found = True
        else:
            itemp = mllp[itemp]

    if found:
        print(mll)
        print("Item found in position : ", itemp + 1)
    else:
        print(mll)
        print("Item not found")
    return itemp


def delete():
    global sp, hp, temp, itemp
    if hp != np:
        mllp[sp] = hp
        mll[sp] = None
        sp = sp - 1
        hp = sp + 1
        temp = mll[hp]
        itemp = itemp - 1
        print(hp, ",", sp, ",", temp)
        print(mll)
        print(mllp)
        print("Item Position : ", itemp)
    else:
        print("Linked list is Empty - can't delete")


c = "Y"
while c == "Y" or "y":
    print("Linked List")
    print("------")
    print("1. insert")
    print("2. delete")
    print("3. search")
    ch = int(input("Enter a Choice"))
    if ch == 1:
        item = int(input("Enter value : "))
        insert(item)
    elif ch == 2:
        delete()
    elif ch == 3:
        items = int(input("Enter item to search"))
        searchll(items)

    c = input("Do you wish to continue?(Y/N)")
