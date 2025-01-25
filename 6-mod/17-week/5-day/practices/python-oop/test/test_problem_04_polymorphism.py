import unittest

class TestBookDescriptions(unittest.TestCase):
    def test_function_for_expected_result(self):
        from problem_04_polymorphism import Book
        book = Book("Alice in Wonderland", "Lewis Carroll", 1865)
        self.assertEqual(book.description(), "Alice in Wonderland is written by Lewis Carroll and was published in 1865.")

    def test_function_for_expected_result_nonfiction(self):
        from problem_04_polymorphism import NonfictionBook
        nonfiction = NonfictionBook("Cosmos", "Carl Sagan", 1980, "cosmic evolution and human civilization")
        self.assertEqual(nonfiction.description(), "Cosmos is written by Carl Sagan and was published in 1980. It is a nonfiction book about cosmic evolution and human civilization.")

    def test_function_for_test_results(self):
        from problem_04_polymorphism import Book, NonfictionBook
        book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
        book2 = NonfictionBook("In Love", "Amy Bloom", 2022, "a memoir of love and lost")
        self.assertEqual(book.description(), "The Great Gatsby is written by F. Scott Fitzgerald and was published in 1925.")
        self.assertEqual(book2.description(), "In Love is written by Amy Bloom and was published in 2022. It is a nonfiction book about a memoir of love and lost.")
