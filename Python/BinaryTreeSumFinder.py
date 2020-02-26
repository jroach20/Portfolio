#This problem was asked by Google.
#Given the root of a binary search tree, and a target K, 
#return two nodes in the tree whose sum equals K.
#For example, given the following tree and K of 20
#    10
#   /   \
# 5      15
#       /  \
#     11    15
#Return the nodes 5 and 15

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
    
    def kFinder(k, para):
        a = tree()
        nodes = a.makeList(para)
        result = None
        
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                
                if (i == j):
                    continue
                
                c = nodes[i] + nodes [j]
                
                if (c == k):
                    first = j
                    second = i
                    result = nodes[first],"+",nodes[second],"=",k
                    result = " ".join(map(str,result))
                    break
        
        if (result == None):
            result = "k isn't there"
        
        return result

t = tree()

for i in [10,5,15,11,15]:
    t.insert(i)

print (t.makeList(t.root))

print (tree.kFinder(20,t.root))
