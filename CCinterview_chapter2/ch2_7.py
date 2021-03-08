#chapter 2 problem 7 
from ch2_SetUp import Node, LinkedList 



LL1 = LinkedList()
LL2 = LinkedList()
LL3 = LinkedList()
for char in "LIST":
    LL3.push(char)

for char2 in "0101linked":
    LL2.push(char2)

for char3 in "LINK2D":
    LL1.push(char3)
nextNode = LL3.begin
LL1.pushNode(nextNode)
LL2.pushNode(nextNode)

#LL1.printList()
#print('-' * 10)
#LL2.printList()
#worst case is no intersection

LL4 = LinkedList()
LL5 = LinkedList() 

for char4 in 'notintersecting':    
    LL4.push(char4)
    LL5.push(char4)


def findIntersection(linkedlist1, linkedlist2):
    node1 = linkedlist1.begin 
    node2 = linkedlist2.begin
    node1end = linkedlist1.begin 
    node2end = linkedlist2.begin
    node2temp = linkedlist2.begin
    count = 0
    
    #worst case check
    # SEE TEST 3.  This does not prevent a 'worst case'
    # A worst case is when the end node is the intersection.
    while node1end:
        if node1end.next == None:
            break 
        else:
            node1end = node1end.next 
        count += 1

    while node2end:
        if node2end.next == None:
            break
        else:
            node2end = node2end.next 
        count += 1

    if node1end != node2end:
        print("No intersection")
        print("count=", count)
        return None, None

    else:
        while node1 and node2temp:
       
            if node1 == node2:
                print("intersection found.")
                print("count=", count)
                return node1, node2 
            if node1.next == node2:
                print("intersection found.")
                print("count=", count)
                return node1.next, node2 
            if node2.next == node1:
                print("intersection found.")
                print("count=", count)
                return node2.next, node1
            while node2:
                #print('node1:', node1)
                #print('node2:', node2)
                #print("*********************************")
           
                if node1 == node2:
                    print("intersection found.")
                    print("count=", count)
                    return node1, node2
                if node1.next == node2:
                    print("intersection found.")
                    print("count=", count)
                    return node1.next, node2
                if node2.next == node1:
                    print("intersection found.")
                    print("count=", count)
                    return node1, node2.next
                node2 = node2.next
                count += 1

            node1 = node1.next 
            node2 = node2temp
            count += 1
    print("end nodes where the same, but no intersection occured")
    # FAILSAFE
    return None, None


def test1():
    #findIntersection(linkedlist1, linkedlist2):
    
    #intersectionNode = Node('intersection')

    #LL1 = LinkedList()
    #LL2 = LinkedList() 
    x, y = findIntersection(LL1, LL2)
    # count result = 61

    print(x, y)

#test1()

def test2():
    #worst case
    # LL3, LL4 
    result = findIntersection(LL4, LL5)
    print(result)
    #count = 240

#test2()

def test3():
    #scenario: End node is the intersection
    LLend1 = LinkedList()
    LLend2 = LinkedList() 
    endNode = Node("end")
    for num in range(19):
        LLend1.push(num)
        LLend2.push(num)
        print(num)
    LLend1.pushNode(endNode)
    LLend2.pushNode(endNode)
    result = findIntersection(LLend1, LLend2)
    #count = 435 
    # length of both lists = 19
    # This is the worst case, and the worst case of checking for the end node, does not stop with the check.
    
    print(result)

test3()
