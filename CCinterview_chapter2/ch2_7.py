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

LL1.printList()
print('-' * 10)
LL2.printList()
#worst case is no intersection

LL4 = LinkedList()
LL5 = LinkedList() 

for char4 in 'notintersecting':    
    LL4.push(char4)
    LL5.push(char4)


def findIntersection(linkedlist1, linkedlist2):
    node1 = linkedlist1.begin 
    node2 = linkedlist2.begin
    node2temp = linkedlist2.begin
    count = 0
    while node1 and node2temp:
       
        if node1 == node2:
            print("*\n",count, "\n*")
            return node1, node2 
        if node1.next == node2:
            print("*\n",count, "\n*")
            return node1.next, node2 
        if node2.next == node1:
            print("*\n",count, "\n*")
            return node2.next, node1
        while node2:
            #print('node1:', node1)
            #print('node2:', node2)
            #print("*********************************")
           
            if node1 == node2:
                print("*\n",count, "\n*")
                return node1, node2
            if node1.next == node2:
                print("*\n",count, "\n*")
                return node1.next, node2
            if node2.next == node1:
                print("*\n",count, "\n*")
                return node1, node2.next
            node2 = node2.next
            count += 1

        node1 = node1.next 
        node2 = node2temp
        count += 1
    print("*\n",count, "\n*")   
    return None, None


def test1():
    #findIntersection(linkedlist1, linkedlist2):
    
    #intersectionNode = Node('intersection')

    #LL1 = LinkedList()
    #LL2 = LinkedList() 
    x, y = findIntersection(LL1, LL2)
    # count result = 61
    print(x, '\n', y)

#test1()

def test2():
    #worst case
    # LL3, LL4 
    result = findIntersection(LL4, LL5)
    print(result)
    #count = 240

#test2()
