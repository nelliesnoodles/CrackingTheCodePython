#chapter 2 Setup
# In Java and C, the next would be 'Null' instead of None
# Single link (STACK)
# Reference Link:
 # https://www.andrew.cmu.edu/course/15-121/lectures/Stacks%20and%20Queues/Stacks%20and%20Queues.html
class Node(object):
    def __init__(self, data):
        self.next = None
        self.data = data

    def __repr__(self):
        data = self.data #<=  Changed  data = self.data or None was setting 0 as None.
        # reference Link: https://stackoverflow.com/questions/8747740/assignment-with-or-in-python
       
        data = str(data)
        # Removed ' or None'  to account for data that is the zero integer
        if self.next != None:
            next = self.next and self.next.data
        else:
            next = 'None'
        dataString = f"[ data: {data}, next: {next} ]"
        return dataString


class LinkedList(object):

     def __init__(self):
         self.end = None
         self.begin = None
         
         
     def push(self, newdata):
         newnode = Node(newdata)
         
         #change = removed zero check. The problem was in the __repr__
       

         if self.end == None and self.begin == None:
             self.begin = newnode
         elif self.begin != None and self.end == None:
             self.begin.next = newnode 
             self.end = newnode
         else:
             self.end.next = newnode 
             self.end = newnode

     #  ***   Optional push method    **** #
     #This method will make the self.begin and self.end point to the same node when the first item is added.
     #Every node after that is attached to the self.end.next, and then replaces the self.end address with the new nodes address
     #I don't particularly like this method, but it seems to be the typical creation method for this exercise. 
     #I believe they do it this way as to avoid null pointer issuses, which is a serious issue in languages like C.
     def append(self, newdata):
           
        newnode = Node(newdata)

        if self.begin is None:
            self.begin = newnode
        else:
            self.end.next = newnode

        self.end = newnode
    #    **   END OPTIONAL   **    #
            

        
    
     def printList(self):
        if self.begin == None:
            print("This list is empty, or self.begin IS NONE")
        else:
            node = self.begin
            #print("begin node:", node)
            #print("begin node next:", self.begin.next)
            while node:
                print(node)
                node = node.next



     def delete(self, value):

        node = self.begin
        if node == None:
            return None 
        else:
            #print(node.data, value)
            temp = self.begin
            node = self.begin.next

            if node == None and temp.data != value:
               
                return 
           

            while node:
              
                if node.data == value:
                   
                   
                    if node.next != None:
                        temp.next = node.next 
                    if node.next == None: 
                        temp.next = None
                    break
                
                temp = node 
                node = node.next
                

               
                
                



def test1():
    stack = LinkedList()
    for i in range(0, 25):
        stack.append(i)
    stack.printList()


#test1()

def test2():
    stack = LinkedList()
    for i in range(0, 25):
        stack.push(i)
    deletions = [2, 5, 8, 10, 11, 24]
    for num in deletions:
        
        stack.delete(num)

    stack.printList()

#test2()

def zerobugtest():
    #fixed.  When assigning the __repr__
    stack = LinkedList()
    for i in range(0, 5):
        stack.append(0)
    stack.printList()


#zerobugtest()