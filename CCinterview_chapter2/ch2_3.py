#chapter 2 problem 3 

from ch2_SetUp import Node, LinkedList 

LL = LinkedList() 
values = ['ted', 'dy', 'bear', 'stuffed', 'jalapenos']
for item in values:
    LL.push(item)

def getMiddle(val):
    start = LL.begin
    while start:
        if start.data == val:
            return start
        start = start.next
    return None


def removeMiddle(node):
    # In python a Garbage Collector will remove any items that have no reference to them 
    # So once nothing points at that middle node, the garbage collectore picks it up and discards it.
    # A begin node, or an end node would cause problems because the values would have to be reset in the Linked List.
    # self.begin would have to be set to the nextnode 
    # self.end would need to be set to the previous node
    # Because we only have access to this node, there isn't a way to reach these values or assign new pointers to them
    if node == None:
        print("Error, Value can not be None.")
    if node.next:
        nextnode = node.next
        newdata = nextnode.data
        newnext = nextnode.next
        node.data = newdata 
        node.next = newnext
    else:
        print('Error: This points to a None.')

def test1():
    node = getMiddle('bear')
    removeMiddle(node)
    LL.printList()
    print("\n---   Next test -----")
    node = getMiddle('dy')
    removeMiddle(node)
    LL.printList()

test1()

