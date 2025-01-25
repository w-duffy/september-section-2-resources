# Tree Traversal Challenge

# In this practice, you will use classes to implement a binary search tree and
# perform pre-order, in-order, and post-order traversal of the tree.

# Implement a class Node with a constructor method that defines the following
# instance properties:

# The lefthand child of the node, initialized to None
# The right-hand child of the node, initialized to None
# The value of the node, initialized to the value passed into the constructor

# Implement the following methods:

# 1. insert() that takes in the root node and a new node and places the new node
#    in the correct location in the binary search tree
# 2. preOrderTraversal() that traverses the tree and prints the value of each
#    node in pre-order succession
# 3. inOrderTraversal() that traverses the tree and prints the value of each
#    node in in-order succession
# 4. postOrderTraversal() that traverses the tree and prints the value of each
#    node in post-order succession

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
# Insert Node
#!!START
    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value
#!!END
# Preorder traversal
# Root -> Left -> Right
#!!START
    def preOrderTraversal(self, root):
        result = []
        if root:
            result.append(root.value)
            result = result + self.preOrderTraversal(root.left)
            result = result + self.preOrderTraversal(root.right)
        return result
#!!END
# Inorder traversal
# Left -> Root -> Right
#!!START
    def inOrderTraversal(self, root):
        result = []
        if root:
            result = self.inOrderTraversal(root.left)
            result.append(root.value)
            result = result + self.inOrderTraversal(root.right)
        return result
#!!END
# Postorder traversal
#  Left -> Right -> Root
#!!START
    def postOrderTraversal(self, root):
        result = []
        if root:
            result = self.postOrderTraversal(root.left)
            result = result + self.postOrderTraversal(root.right)
            result.append(root.value)
        return result
#!!END


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

print(root.preOrderTraversal(root))  # [27, 14, 10, 19, 35, 31, 42]
print(root.inOrderTraversal(root))   # [10, 14, 19, 27, 31, 35, 42]
print(root.postOrderTraversal(root)) # [10, 19, 14, 31, 42, 35, 27]
