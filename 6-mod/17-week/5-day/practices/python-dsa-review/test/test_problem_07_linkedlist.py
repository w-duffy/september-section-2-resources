import unittest

class TestLinkedList(unittest.TestCase):
    def test_for_expected_results(self):
        from problem_07_linkedlist import Node, LinkedList, result
        linked_list = LinkedList()
        linked_list.add('node 1')
        linked_list.add('node 2')
        linked_list.add('node 3')
        linked_list.add('node 4')
        linked_list.add('node 5')
        expected = ['Current node: node 1',
                    'Current node: node 2',
                    'Current node: node 3',
                    'Current node: node 4',
                    'Current node: node 5']
        self.assertEqual((result(linked_list)), expected)

    def test_for_test_results(self):
        from problem_07_linkedlist import Node, LinkedList, result
        linked_list = LinkedList()
        linked_list.add('node 0')
        linked_list.add('node -2')
        linked_list.add('node -8')
        linked_list.add('node 3')
        linked_list.add('node None')
        expected = ['Current node: node 0',
                    'Current node: node -2',
                    'Current node: node -8',
                    'Current node: node 3',
                    'Current node: node None']
        self.assertEqual((result(linked_list)), expected)
