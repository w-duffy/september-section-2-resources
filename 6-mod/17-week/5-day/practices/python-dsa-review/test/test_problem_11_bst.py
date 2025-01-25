import unittest

class TestTreeSearch(unittest.TestCase):
    def test_search_to_return_true(self):
        from problem_11_bst import TreeNode, is_BST
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        self.assertEqual(is_BST(root), True)

    def test_search_to_return_false(self):
        from problem_11_bst import TreeNode, is_BST
        root = TreeNode(5)
        root.left = TreeNode(6)
        root.right = TreeNode(7)
        self.assertEqual(is_BST(root), False)

    def test_search_test(self):
        from problem_11_bst import TreeNode, is_BST
        root = TreeNode(10)
        root.left = TreeNode(6)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(9)
        root.right = TreeNode(15)
        root.right.right = TreeNode(20)
        root.right.left = TreeNode(13)
        self.assertEqual(is_BST(root), True)

    def test_search_test_left(self):
        from problem_11_bst import TreeNode, is_BST
        root = TreeNode(10)
        root.left = TreeNode(8)
        root.left.left = TreeNode(6)
        root.left.left.left = TreeNode(4)
        self.assertEqual(is_BST(root), True)

    def test_search_test_right(self):
        from problem_11_bst import TreeNode, is_BST
        root = TreeNode(10)
        root.right = TreeNode(8)
        root.right.right = TreeNode(6)
        root.right.right.right = TreeNode(100)
        self.assertEqual(is_BST(root), False)

    def test_search_test_root(self):
        from problem_11_bst import TreeNode, is_BST
        root = TreeNode(0)
        self.assertEqual(is_BST(root), True)

    def test_search_test_none(self):
        from problem_11_bst import TreeNode, is_BST
        root = TreeNode(0)
        root.right = TreeNode(0)
        root.left = TreeNode(0)
        self.assertEqual(is_BST(root), False)
