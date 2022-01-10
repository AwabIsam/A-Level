size = int(input("Enter size of the Linked List: "))

linkedlist = [None for i in range(size)]
listpointers = [i + 1 for i in range(size + 2)]
startpointer = -1
null = -1
heappointer = 0
oldindex = startpointer
initial_run = True


def add(x):
    global startpointer, heappointer, listpointers, initial_run
    if heappointer != null and heappointer != size:
        temp = startpointer
        startpointer = heappointer
        heappointer = listpointers[heappointer]
        linkedlist[startpointer] = x
        listpointers[startpointer] = temp
        if initial_run:
            listpointers[0], listpointers[-1] = null, null
            initial_run = False
    else:
        print("Linked List is Full - can't Insert")


def remove(x):
    global startpointer, heappointer, oldindex
    if startpointer != null:
        index = startpointer
        while linkedlist[index] != x and index != null:
            oldindex = index
            index = listpointers[index]
        if index == null:
            print(x, "not found")
        else:
            linkedlist[index] = None
            temp = listpointers[index]
            listpointers[index] = heappointer
            heappointer = index
            listpointers[oldindex] = temp
    else:
        print("Linked List is Empty, can't Delete")


def search(key):
    for n in range(len(linkedlist)):
        if linkedlist[n] == key:
            print('Found at position', n + 1)
            break
    else:
        print('Not found')


while True:
    menu = int(input(f"""Choose an option:
1. Add
2. Delete
3. Search
4. Display
5. Exit

Linked List: {linkedlist}
List Pointers: {listpointers}
-> """))
    if menu == 1:
        item = int(input("Enter item to be Inserted: "))
        add(item)
        print(startpointer)
        print(heappointer)
    elif menu == 2:
        item = int(input("Enter item to be Deleted: "))
        remove(item)
        print(startpointer)
        print(heappointer)
    elif menu == 3:
        value = int(input("Enter item to Search: "))
        search(value)
    elif menu == 4:
        print(linkedlist)
        print(listpointers)
    elif menu == 5:
        break
    else:
        print("Enter a value between 1 - 4")
