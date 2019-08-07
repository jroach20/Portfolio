#This problem was asked by Microsoft.
#Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer 
#and each internal node is one of '+', '−', '∗', or '/'.
#Given the root to such a tree, write a function to evaluate it.
#For example, given the following tree:
#    *
#   / \
#  +    +
# / \  / \
#3  2  4  5
#You should return 45, as it is (3 + 2) * (4 + 5).


class node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    
    def evaluateExpressionTree(self,root): 
  
        # empty tree 
        if root is None: 
            return 0
      
        if root.left is None and root.right is None: 
            return int(root.data) 
      
        # evaluate left tree 
        left_sum = self.evaluateExpressionTree(root.left) 
      
        # evaluate right tree 
        right_sum = self.evaluateExpressionTree(root.right) 
      
        # check which operation to apply 
        if root.data == '+': 
            return left_sum + right_sum 
          
        elif root.data == '-': 
            return left_sum - right_sum 
          
        elif root.data == '*': 
            return left_sum * right_sum 
          
        else: 
            return left_sum / right_sum 
            

tree = node("*")

tree.left = node("+")
tree.right = node("+")

tree.left.left = node(3)
tree.left.right = node(2)

tree.right.left = node(4)
tree.right.right = node(5)


print (tree.evaluateExpressionTree(tree))
