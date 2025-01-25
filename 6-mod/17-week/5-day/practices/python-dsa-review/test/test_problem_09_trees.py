import unittest

class TestTreeTraversal(unittest.TestCase):
    def test_results_for_pre_order_traversals(self):
        from problem_09_trees import Node
        root = Node(27)
        root.insert(14)
        root.insert(35)
        root.insert(10)
        root.insert(19)
        root.insert(31)
        root.insert(42)
        self.assertEqual(root.preOrderTraversal(root), [27, 14, 10, 19, 35, 31, 42])

    def test_results_for_in_order_traversal(self):
        from problem_09_trees import Node
        root = Node(38)
        root.insert(19)
        root.insert(90)
        root.insert(74)
        root.insert(-2)
        root.insert(0)
        root.insert(-85)
        self.assertEqual(root.inOrderTraversal(root), [-85, -2, 0, 19, 38, 74, 90])

    def test_results_for_post_order_traversal(self):
        from problem_09_trees import Node
        root = Node(64)
        root.insert(-90)
        root.insert(-21)
        root.insert(5)
        root.insert(73)
        root.insert(-8)
        root.insert(15)
        root.insert(2)
        self.assertEqual(root.postOrderTraversal(root), [2, -8, 15, 5, -21, -90, 73, 64])
