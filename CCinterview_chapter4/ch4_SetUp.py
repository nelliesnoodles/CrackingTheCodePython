# chapter 4 Set up
from random import randint

class BinaryNode(object):
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
        self.rootnode = False
        # Not sure if this will be needed but just in case
        self.visited = False

    def __repr__(self):
        data = self.data
        left = 'None'
        right = 'None'
        if self.left != None:
            left = self.left.data
        if self.right != None:
            right = self.right.data
        rep = f"[{left}, {data}, {right}]"
        return rep

class BST(object):
    def __init__(self):
        self.root = BinaryNode() 
        self.root.rootnode = True 

    def push(self, data):
        newnode = BinaryNode()
        newnode.data = data 
        ROOT = self.root 
        if ROOT.data == None:
            self.root = newnode 
            newnode.rootnode = True 
        else:
            if data <= ROOT.data:
                node = ROOT.left
                if node == None:
                    self.root.left = newnode
                else:
                    while node:
                        current = node.data
                        if current == data:
                            # do nothing. Break?
                            break
                        if current <= data:
                            if node.left == None:
                                node.left = newnode
                                break
                            else:
                                node = node.left
                        elif current >= data:
                            if node.right == None:
                                node.right = newnode
                                break
                            else:
                                node = node.right
                        else:
                            print("breaking while loop Left branch placement.")
                            break
            else:
                node = ROOT.right
                if node == None:
                    self.root.right = newnode
                else:
                    while node:
                        current = node.data
                        if current == data:
                            break
                        if current < data:
                            if node.left == None:
                                node.left = newnode
                                break
                            else:
                                node = node.left
                        elif current > data:
                            if node.right == None:
                                node.right = newnode
                                break
                            else:
                                node = node.right
                        else:
                            print("breaking while loop Left branch placement.")
                            break

    def recurs_dump(self, branch):
        
        if branch.left == None and branch.right == None:
            print("END BRANCH")
        else:
            print("branch:", branch)
            if branch.left != None:
                print("left:", branch.left)
                self.recurs_dump(branch.left)
            if branch.right != None:
                print("right:", branch.right)
                self.recurs_dump(branch.right)

    def dump(self):
        ROOT = self.root
        print(ROOT)
        if ROOT.left != None:
            print("LEFT BRANCH")
            self.recurs_dump(ROOT.left)
        if ROOT.right != None:
            print("RIGHT BRANCH")
            self.recurs_dump(ROOT.right)
        print("--END DUMP--")


def testPush():
    BT = BST()
    for i in range(18):
        x = randint(1, 20)
        BT.push(x)
    BT.dump()

#testPush()
    