# -*- coding: utf-8 -*-
"""
Write a program to merge two binary trees. Each node in the new tree 
should hold a value equal to the sum of the values of the corresponding nodes of the input trees. 
If only one input tree has a node in a given position, the corresponding
node in the new tree should match that input node.

"""

class node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
class tree:
    def __init__(self):
        self.root = None
        
    def __str__(self):
        current = self.root
        
    def insert(self, item):
        newNode = node(item)
        current = self.root
        parent = self.root
        
        if self.root == None:
            self.root = newNode
        else:
            while current != None:
                parent = current
                if item < current.data:
                    current = current.left
                else:
                    current = current.right

            if item < parent.data:
                parent.left = newNode
            else:
                parent.right = newNode
    
    def makeList(self, aNode):
        nodes = []
        if aNode == None:
            pass
        
        if aNode != None:
            nodes = self.makeList(aNode.left)
            nodes.append(aNode.data)
            nodes += self.makeList(aNode.right)
        return nodes
    
    def treeLength(self,tree1,tree2):
        
        tree1Len = len(self.makeList(tree1))
        tree2Len = len(self.makeList(tree2))
        bigTree = 0
        
        if tree1Len > tree2Len:
            bigTree = tree1Len
            
        else:
            bigTree = tree2Len
        
        return bigTree
    
    def mergeTrees(self,tree1,tree2):
        treeLength = self.treeLength(tree1,tree2)
        tree1 = self.makeList(tree1)
        tree2 = self.makeList(tree2)
        newTree = self

        for i in range(treeLength):
             try:
                 newTree.insert (tree1[i]+tree2[i])
                 
             except IndexError:
                if len(tree1) == treeLength:
                    newTree.insert (tree1[i])
                    
                else:
                    newTree.insert (tree2[i])
                    
        newTree = self.makeList(newTree.root)
    
        return newTree
        
t = tree()
u = tree()

for i in [10,5,15,11,15]:
    t.insert(i)
    
for i in [1,2,3,4,5]:
    u.insert(i)

print (t.makeList(t.root))
print (u.makeList(u.root))

print (tree().mergeTrees(t.root,u.root))