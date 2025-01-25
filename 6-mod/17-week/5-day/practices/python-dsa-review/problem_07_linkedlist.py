# Linked List Iterator

# In this practice, you will be overriding built-in magic methods to iterate
# over a linked list. You will see a very simple Node & LinkedList class in
# the file.

# Implement another class called LinkedListIterator that uses the magic
# methods __init__, __iter__, and __next__ to allow for iteration over an
# instance of the LinkedList class with a for loop:

# 1. __init__ should initialize an instance property that keeps track of the
#    current node.
# 2. __iter__ must return an iterator object, in other words an object that
#    implements __next__.
# 3. __next__ should return the value of the current node and then move the
#    current node to the next node in the linked list. If the current node is
#    None, raise the built-in StopIteration exception to stop iterating.

# We are iterating over the LinkedList class itself, so this class will also
# need a __iter__ method that returns an iterator object. Do not modify the
# Node class.

#!!START
class LinkedListIterator:
    def __init__(self, head):
        self._current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self._current:
            raise StopIteration
        else:
            value = self._current._value
            self._current = self._current._next
            return value
#!!END

class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0
#!!START SILENT
    def __iter__(self):
        return LinkedListIterator(self._head)
#!!END
    def add(self, value):
        new_node = Node(value)

        if self._head is None:
            self._head = new_node
        else:
            self._tail._next = new_node

        self._tail = new_node
        self._length += 1
        return self

    def __len__(self):
        return self._length


linked_list = LinkedList()
linked_list.add('node 1')
linked_list.add('node 2')
linked_list.add('node 3')
linked_list.add('node 4')
linked_list.add('node 5')


# -----------------------DO NOT MODIFY BELOW THIS LINE------------------------ #
def result(linked_list):
    lst = []
    for i in linked_list:
        lst.append(f"Current node: {i}")
    return lst
