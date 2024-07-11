class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    # def insert(self, val):
    #     newNode = Node(val)
    #     #Enter you code here.
    #     if (self.root is None):
    #         self.root = newNode
    #         return self
    #     if (self.root.info <= newNode.info):
    #         if (self.root.right is None):
    #             self.root.right = newNode
    #             return self
    #         else:
    #             return tree.insert(self.root.right, newNode.info)
    #     if (self.root.info >= newNode.info):
    #         if (self.root.left is None):
    #             self.root.left = newNode
    #             return self
    #         else:
    #             return tree.insert(self.root.right, newNode.info)

    def insert(self, val):
        newNode = Node(val)
        if (self.root is None):
            self.root = newNode
            return self
        cur = self.root
        while (1):
            if (newNode.info >= cur.info):
                if (cur.right is None):
                    cur.right = newNode
                    return self
                else:
                    cur = cur.right
                    continue
            if (newNode.info <= cur.info):
                if (cur.left is None):
                    cur.left = newNode
                    return self
                else:
                    cur = cur.left
                    continue
            

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)