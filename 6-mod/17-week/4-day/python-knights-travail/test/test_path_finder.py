import unittest
import path_finder
import tree


class TestKnightPathFinderInitialize(unittest.TestCase):
    def setUp(self):
        self.knight_path_finder_pos_0_0 = path_finder.KnightPathFinder((0, 0))
        self.knight_path_finder_pos_3_3 = path_finder.KnightPathFinder((3, 3))

    def test_root_attribute_exists(self):
        attribute_name = "_root"
        has_attribute = hasattr(
            self.knight_path_finder_pos_0_0, attribute_name
        )
        self.assertTrue(
            has_attribute,
            msg=f"KnightPathFinder class has no {attribute_name} attribute."
        )

    def test_considered_positions_attribute_exists(self):
        attribute_name = "_considered_positions"
        has_attribute = hasattr(
            self.knight_path_finder_pos_0_0, attribute_name
        )
        self.assertTrue(
            has_attribute,
            msg=f"KnightPathFinder class has no {attribute_name} attribute."
        )

    def test_root_should_be_node(self):
        self.assertIsInstance(self.knight_path_finder_pos_0_0._root, tree.Node)

    def test_should_set_root_position(self):
        self.assertEqual(self.knight_path_finder_pos_0_0._root.value, (0, 0))
        self.assertEqual(self.knight_path_finder_pos_3_3._root.value, (3, 3))

    def test_considered_positions_should_be_set(self):
        self.assertIsInstance(
            self.knight_path_finder_pos_0_0._considered_positions, set
        )

    def test_considered_positions_contains_root_pos(self):
        self.assertIn(
            self.knight_path_finder_pos_0_0._root.value,
            self.knight_path_finder_pos_0_0._considered_positions
        )
        self.assertIn(
            self.knight_path_finder_pos_3_3._root.value,
            self.knight_path_finder_pos_3_3._considered_positions
        )


class TestGetValidMoves(unittest.TestCase):
    def setUp(self):
        self.knight_path_finder = path_finder.KnightPathFinder((0, 0))

    def test_get_valid_moves_exists(self):
        attribute_name = "get_valid_moves"
        has_attribute = hasattr(
            self.knight_path_finder, attribute_name
        )
        self.assertTrue(
            has_attribute,
            msg=f"KnightPathFinder class has no {attribute_name} attribute."
        )

    def test_get_valid_moves_returns_list(self):
        pos = (0, 0)
        self.assertIsInstance(
            self.knight_path_finder.get_valid_moves((0, 0)), list
        )

    def test_get_valid_moves_gets_valid_moves(self):
        moves1 = self.knight_path_finder.get_valid_moves((0, 0))
        expected1 = [(1, 2), (2, 1)]
        moves2 = self.knight_path_finder.get_valid_moves((3, 3))
        expected2 = [
            (1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 2), (5, 4)
        ]
        moves3 = self.knight_path_finder.get_valid_moves((7, 7))
        expected3 = [(5, 6), (6, 5)]
        moves4 = self.knight_path_finder.get_valid_moves((20, 20))
        expected4 = []
        self.assertCountEqual(moves1, expected1)
        self.assertCountEqual(moves2, expected2)
        self.assertCountEqual(moves3, expected3)
        self.assertCountEqual(moves4, expected4)


class TestNewMovePositions(unittest.TestCase):
    def setUp(self):
        self.knight_path_finder1 = path_finder.KnightPathFinder((0, 0))
        self.knight_path_finder2 = path_finder.KnightPathFinder((3, 3))

    def test_new_move_positions_exists(self):
        attribute_name = "new_move_positions"
        has_attribute = hasattr(
            self.knight_path_finder1, attribute_name
        )
        self.assertTrue(
            has_attribute,
            msg=f"KnightPathFinder class has no {attribute_name} attribute."
        )

    def test_new_move_positions_returns_set(self):
        self.assertIsInstance(
            self.knight_path_finder1.new_move_positions((0, 0)), set
        )

    def test_new_move_positions_returns_correct_positions(self):
        test1 = self.knight_path_finder1.new_move_positions((1, 2))
        expected1 = {(2, 4), (0, 4), (3, 1), (2, 0), (3, 3)}
        test2 = self.knight_path_finder2.new_move_positions((1, 2))
        expected2 = {(2, 4), (0, 4), (0, 0), (3, 1), (2, 0)}
        self.assertEqual(test1, expected1)
        self.assertEqual(test2, expected2)

    def test_new_move_positions_correctly_mutates_considered_positions(self):
        self.assertEqual(
            self.knight_path_finder1._considered_positions, {(0, 0), }
        )
        self.assertEqual(
            self.knight_path_finder2._considered_positions, {(3, 3), }
        )
        self.knight_path_finder1.new_move_positions((2, 1))
        self.knight_path_finder2.new_move_positions((2, 1))
        self.assertEqual(
            self.knight_path_finder1._considered_positions,
            {(0, 2), (4, 0), (3, 3), (0, 0), (1, 3), (4, 2)}
        )
        self.assertEqual(
            self.knight_path_finder2._considered_positions,
            {(0, 2), (3, 3), (4, 0), (0, 0), (1, 3), (4, 2)}
        )


class TestBuildMoveTree(unittest.TestCase):

    def setUp(self):
        self.knight_path_finder1 = path_finder.KnightPathFinder((0, 0))
        self.knight_path_finder2 = path_finder.KnightPathFinder((3, 3))

    def test_build_move_tree_exists(self):
        attribute_name = "build_move_tree"
        has_attribute = hasattr(
            self.knight_path_finder1, attribute_name
        )
        self.assertTrue(
            has_attribute,
            msg=f"KnightPathFinder class has no {attribute_name} attribute."
        )

    def test_root_has_correct_children(self):
        self.knight_path_finder1.build_move_tree()
        self.knight_path_finder2.build_move_tree()
        children1 = [
            node.value for node in self.knight_path_finder1._root.children
        ]
        expected1 = [(1, 2), (2, 1)]

        children2 = [
            node.value for node in self.knight_path_finder2._root.children
        ]
        expected2 = [
            (1, 2), (2, 1), (5, 4), (1, 4), (4, 5), (2, 5), (4, 1), (5, 2)
        ]

        self.assertCountEqual(children1, expected1)
        self.assertCountEqual(children2, expected2)


class TestFindPath(unittest.TestCase):
    def setUp(self):
        self.knight_path_finder1 = path_finder.KnightPathFinder((0, 0))
        self.knight_path_finder1.build_move_tree()
        self.knight_path_finder2 = path_finder.KnightPathFinder((3, 3))
        self.knight_path_finder2.build_move_tree()

    def test_find_path_returns_correct_paths_starting_at_0_0(self):
        path1_result = self.knight_path_finder1.find_path((2, 1))
        path1_expected = [(0, 0), (2, 1)]
        path2_result = self.knight_path_finder1.find_path((3, 3))
        path2_expected = [(0, 0), (1, 2), (3, 3)]
        path3_result = self.knight_path_finder1.find_path((6, 2))
        path3_expected = [(0, 0), (1, 2), (2, 4), (4, 3), (6, 2)]
        path4_result = self.knight_path_finder1.find_path((7, 6))
        path4_expected = [(0, 0), (1, 2), (2, 4), (4, 3), (5, 5), (7, 6)]
        self.assertEqual(len(path1_result), len(path1_expected))
        self.assertEqual(len(path2_result), len(path2_expected))
        self.assertEqual(len(path3_result), len(path3_expected))
        self.assertEqual(len(path4_result), len(path4_expected))
        self.assertTrue(
            first_and_last_el_are_same(path1_result, path1_expected),
            msg="Incorrect path"
        )
        self.assertTrue(
            first_and_last_el_are_same(path2_result, path2_expected),
            msg="Incorrect path"
        )
        self.assertTrue(
            first_and_last_el_are_same(path3_result, path3_expected),
            msg="Incorrect path"
        )
        self.assertTrue(
            first_and_last_el_are_same(path4_result, path4_expected),
            msg="Incorrect path"
        )

    def test_find_path_returns_correct_paths_starting_at_3_3(self):
        path1_result = self.knight_path_finder2.find_path((2, 1))
        path1_expected = [(3, 3), (2, 1)]
        path2_result = self.knight_path_finder2.find_path((3, 3))
        path2_expected = [(3, 3)]
        path3_result = self.knight_path_finder2.find_path((6, 2))
        path3_expected = [(3, 3), (5, 4), (6, 2)]
        path4_result = self.knight_path_finder2.find_path((7, 6))
        path4_expected = [(3, 3), (4, 5), (6, 4), (7, 6)]
        self.assertEqual(len(path1_result), len(path1_expected))
        self.assertEqual(len(path2_result), len(path2_expected))
        self.assertEqual(len(path3_result), len(path3_expected))
        self.assertEqual(len(path4_result), len(path4_expected))
        self.assertTrue(
            first_and_last_el_are_same(path1_result, path1_expected),
            msg="Incorrect path"
        )
        self.assertTrue(
            first_and_last_el_are_same(path2_result, path2_expected),
            msg="Incorrect path"
        )
        self.assertTrue(
            first_and_last_el_are_same(path3_result, path3_expected),
            msg="Incorrect path"
        )
        self.assertTrue(
            first_and_last_el_are_same(path4_result, path4_expected),
            msg="Incorrect path"
        )


def first_and_last_el_are_same(list1, list2):
    try:
        result = list1[0] == list2[0] and list1[-1] == list2[-1]
        return result
    except IndexError:
        return False
