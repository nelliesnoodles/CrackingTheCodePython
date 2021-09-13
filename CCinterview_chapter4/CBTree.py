
# Python complete binary tree
"""
A complete binary tree is one that is filled from left to right.  
Unlike a binary search tree, the nodes values do not come into play as to their placement.
A heap is just a complete binary tree.
A min-heap has the minimum value stored in the root. 
A max-heap has the maximum value stored in the root. 
For a min heap and a max heap, the parent node of children branches must also be the max/min
of all the values below it. 
Holy crap that seems like a whole lot of reaaranging on each new node. 
What the tree will need:

Add(push) node
Insert node 
Swap node
Place node
Parent node swap, child node swap?

For each node that goes in, it must go in from left => right
For this binary tree we won't be doing min/max 
That can be done after the initial tree code is figured out. 
"""


#####  NODE ######

class CBNode(object):
    def __init__(self, data, ID):
        self.data = data
        self.left = None
        self.right = None 
        self.parent = None 
        self.ID = ID
        
    def __repr__(self):
        """
        This is a special function in python that returns the string 
        representation of an object.  Defining this will allow us to 
        print the node in testing and other senarios with the object data 
        we wish to see. If the data is complex, it would be better to exclude the data being printed 
        in testing and observation, unless you'd like to specifically see the data too. 
        """
        left = 'None'
        right = 'None'
        data = 'None'
        ID = self.ID
        if self.left != None:
            left = self.left.data
        if self.right != None:
            right = self.right.data
        if self.data != None:
            data = self.data
        rep = f"[{left}, {data} : {ID}, {right}]"
        return rep

def testCBNode():
    newnode = CBNode('first') 
    leftnode = CBNode('left')
    rightnode = CBNode('right') 

    newnode.left = leftnode 
    newnode.right = rightnode
    leftnode.parent = newnode 
    rightnode.parent = newnode 

    print(newnode)


class CBTree(object):

    """ key: 
    Special Cases
    1) We are inserting at root (Tree is empty)
    2) We are at the last right child of a level (current level is full)
    3) We are inserting a left child
    4) We are inserting a right child
           

                                                     [root]   
                                               /       |      \    
                                        /              |             \
                                 /                     |                   \
                          [L]                          |                      [R]  
                        /       \                      |                    /     \
                      /            \                   |                   /         \
                    /                \                 |                  /             \
                 [P]                  [P]              |                [P]               [P]
             [P]    [P]           [P]     [P]          |           [P]      [P]       [P]     [P]    
            /   \   /   \         /   \   /   \        |          /   \    /  \      /  \    /   \
          [C]   [C][C]  [C]     [C]   [C][C]  [C]                [C]  [C][C]  [C]  [C]  [C][C]   [C]

    INFO:
    Whenever we insert, we check the last inserted node that is stored.  If the last child that was inserted was a left, 
    we now move to the right in parent to place a child.  If the last child that was inserted was a right, We go up a level and move to the right
    then look for the next Parent in the level that has an empty left child. The Parents are one level above, and linked through their parents.
    This is a lot of movement when placing a child in the tree. A short process for small trees, a long process for big trees. 


    Optimization????
    When we go up the tree, we should never have to go more than one level up, unless the level is full. 
    We know the level is full when the branch level node count has hit N*2, N being the last levels count or When no empty Right branches can be found 

    Otherwise, we'd travel all the way through the tree to discover if there are no right children available.  By keeping count, we know if the level
    is full, and when to start a new level going from root => left most child and starting over. 
    This will only happen at the end insertion, but on trees of sizes like 128, we will save a traversal that would touch each node to find out that
    all node 'right' branches are full.   Is this optimization Worth it?

    When a currentID becomes the same as levelBreak, we will start the next node on a new level. 
    """
    def __init__(self):
        self.root = CBNode('ROOTNODE', 0)
        self.lastInsert = self.root
        self.currentID = 0
        self.N = 2  # + 1 if root starts at 1
        self.levelBreak = False

        
       



    def add(self, data):
        """
        Add nodes in such a way that all values are added from left to right.
        The first problem is to tackle, where the new node should be added.  
        If the tree is filling from left to right,  we should only need to go in a zig zag like pattern looking for the next 
        empty parent.  Each level has 2X more nodes than the previous, no more, no less.        
        """

        # Root is preset.   First nodes to be set are the LEFT and RIGHT branch
        new_id = self.currentID + 1
        newnode = CBNode(data, new_id)
        self.currentID += 1
        if self.root.left == None:          
            newnode.parent = self.root
            self.root.left = newnode   
            # print("setting left primary")
            
        elif self.root.right == None:           
            newnode.parent = self.root
            self.root.right = newnode
            # print("setting right primary")
           
           
           
        else:
            # check if self.levelBreak is true
          
            if self.levelBreak:
                # print("\n -----------levelBreak------------- \n")
                # go to left most child in the tree and start new level.
                # tree is updated in this function no need to repeat self.updateTree()
                self.newLevel(newnode)
                
            # check if lastinserted was a left or right child of parent
            else:
               # print(f"No level break, adding node {data}")
               # print(self.lastInsert)
               # print(self.lastInsert.parent)
                parent = self.lastInsert.parent


                ###  Looking for right child  ###
                if parent.left == self.lastInsert:
                    # we find next empty right child in current level,
                    # this should be the Current Parents right child
                    # if the currentID is equal to the level break, after the node is set, 
                    # update level break. 
                    
                    
                    if parent.right == None:
                        parent.right = newnode
                        newnode.parent = parent
                        self.lastInsert = newnode
                    else:
                        message = "ERROR: The right pointer of the parent had a child. This should not happen."
                        print(message)
                        print("see  ###  Looking for right child  ### clause in add()")
                
                ###  Looking for left child ###
                elif parent.right == self.lastInsert:
                    # We go to each parent checking if it is the left branch of the grandparent. We keep track of 
                    # how many levels we have accended with X  
                    # When it is the left child, we go to the grandparents right, then decend X levels left
                    GP = parent.parent
                    X = 2
                    notFound = True
                    startnode = None
                    #print("*" * 5)
                    #print("finding new left child")
                    while notFound:
                        #print("GP=", GP)
                        #print("parent=", parent)
                        if GP.left == parent:
                            notFound = False
                            startnode = GP.right
                            break
                        else:
                            X += 1
                            parent = GP
                            GP = GP.parent
                    #print(startnode)
                    if startnode != None:
                        #print("placing new left child")
                        while X != 0:

                           
                            if startnode.left == None:
                                #print("newnode being placed left")
                                startnode.left = newnode
                                newnode.parent = startnode
                                #print("newnode parent set to:", startnode)
                                break
                            else:
                                startnode = startnode.left
                                #print("Moving left")
                                X -= 1 
                    #print("----startnode:", startnode)
                    #print("*" * 5)
                  

                    
                else:
                    message = "the lastInsert does not have a parent reference that matches itself in the left or right pointers"
                    print(message)
                    print("see  ###  Looking for right child  ### clause in add()")

        self.updateTree(newnode)


    
    def updateTree(self, newnode):
        self.lastInsert = newnode
        currentID = newnode.ID
        if currentID == self.N:
            # print(currentID, self.N)
            self.levelBreak = True

            
    def updateLevelBreak(self):
        # update the level break point
        self.N = self.N * 2 + 2
        self.levelBreak = False
       


    def newLevel(self, newnode):
        # go to the left most child and start a new level
        # reset self.newLevel to false
      
        start = self.root
        while start != None:
            next = start.left
            if next == None:
                start.left = newnode
                newnode.parent = start
                # print(self.currentID)
               

                break
            start = start.left

        self.updateTree(newnode)      
        self.updateLevelBreak()
     
    def dump(self):
        root = self.root
        message = "root"
        depth = 0
        alist = [[]]
        self.dumphelper(root, message, alist, depth)
        depth = 0
        for item in alist:
            print("------  Depth: ", depth)
            print(item)
            print("\n")
            depth += 1

    def dumphelper(self, branch, message, alist, depth):
        # this is messy looking
        alist[depth].append(branch)
        depth += 1
        if branch.left == None and branch.right == None:
            return alist

        else:
            if branch.left != None or branch.right != None:
                alist.append([])
            
            if branch.left != None:            
                left = branch.left
                message = "branch left"
                self.dumphelper(left, message, alist, depth)
            if branch.right != None:
                message = "branch right"
                right = branch.right            
                self.dumphelper(right, message, alist, depth)


    

        


def Treetest1():
    Tree = CBTree()
    for i in range(20, 50):
        Tree.add(i)
    
    # Dump is appending more lists than necessary, I'm sure I did the recursion wrong, just FYI, there will be extra empty lists when you dump the tree.
    #Tree.dump()

#Treetest1()



