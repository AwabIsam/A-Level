class node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode


startPointer = 0
emptyList = 5

LinkedList = [node(1, 1), node(5, 4), node(6, 7), node(7, -1), node(2, 2), node(0, 6), node(0, 8), node(56, 3), node(0 , 9), node(0, -1)]


def outputNodes(Array, Start):
    while Start != -1:
        print(LinkedList[Start].data)
        print(LinkedList[Start].nextNode)
        Start = LinkedList[Start].nextNode
    
    

def addNode(Array, Start, End):
    item = int(input("Enter value to Add to Linked List: "))
    
    if End < 0 and End > 9:
        print("Linked List is Full")
        return False
    else:
        LinkedList[End].data = item
        LinkedList[End].nextNode = -1
    prev = 0
    while Start != -1:
        prev = Start 
        Start = LinkedList[Start].nextNode
    LinkedList[prev].nextNode = End
    End = LinkedList[End].nextNode
    print("Item Added")
    return True


outputNodes(LinkedList, startPointer)
addNode(LinkedList, startPointer, emptyList)
outputNodes(LinkedList, startPointer)

        
    
print("-----------------------------------------------")
for i in range(10):
    print(f"""{LinkedList[i].data}  {LinkedList[i].nextNode}
     """)
