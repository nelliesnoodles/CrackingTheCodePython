from ch2_SetUp import Node, LinkedList

LL = LinkedList()
values = ['apple', 'goat', 'tree', 99, 780, 'John Smith', 'Jane Doe', 'shrubbery', 'parrot', 'twine']
for item in values:
    LL.push(item)

def kthToLast(alinkedlist, n=0):
   #x(item count before k) + k(items including k, after k) = length(linkedlist)
   count = 0
   node = alinkedlist.begin
   while node:
       count += 1
       node = node.next
   
   #print(len(values))
   #print(count)
   if count == 0:
       return None
   if count < n:
       print('Index out of range!')
       return None
   index = count - n
   newcount = 0
   newnode = alinkedlist.begin
   while newnode:
       if index == newcount:
           return newnode.data 
       else:
           newcount += 1
           newnode = newnode.next
   print("ERROR: Index not found")


def test1():
    x = kthToLast(LL, 5)
    print(x)

test1()
