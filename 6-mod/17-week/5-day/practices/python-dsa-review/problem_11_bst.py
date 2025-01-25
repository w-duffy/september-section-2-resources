# Valid Binary Tree

# Create a function name is_BST to check whether a given binary tree is a valid
# binary search tree (BST) or not. If it is a binary search tree return True,
# if it is not return False.

# A binary search tree (BST) is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.

class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

#!!START
def is_BST(root):
    search = []
    prev = None

    while root or search:
        while root:
            search.append(root)
            root = root.left
        root = search.pop()
        if prev and root.value <= prev.value:
            return False
        prev = root
        root = root.right
    return True
#!!END

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
result = is_BST(root)
print(result) # True

root = TreeNode(5)
root.left = TreeNode(6)
root.right = TreeNode(7)
result = is_BST(root)
print(result) # False
