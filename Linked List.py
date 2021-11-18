n = int(input("How many values do you wish to enter "))

mll = [None for i in range(0,n)]
mllp = [i + 1 for i in range(n)]

    

mllp[n-1] = -1 
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
        print(f"""Heap pointer: {hp}
Start pointer:  {sp}
Temporary pointer:  {temp}
Linked list:  {mll}
Linked list pointers: {mllp}
Item Position:  {itemp}""")
    else:
        print("Linked List is full - can't print")
        
        

found = False


def searchll(xs):
    global itemp, sp, np, found
    found = False
    itemp= sp
    while itemp != np and not found:
        if mll[itemp] == xs:
            found = True
        else:
            itemp = mllp[itemp]
            
    if found == True:
        print(mll)
        print("Item found in position: ", itemp)
    else:
        print(mll)
        print("Item not found")
    
    
    
c = "Y"
while c == "Y" or "y":
    print("Linked List")
    print("-----------")
    print("1. insert")
    print("2. search")
    ch = int(input("Enter a choice: "))
    if ch == 1:
        item = int(input("Enter value: "))
        insert(item)
    elif ch == 2:
        items = int(input("Enter item to search"))
        searchll(items)
            
    
   
