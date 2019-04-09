import unittest
from solution import TreeNode
from solution import EarliestAncestor

class EarliestAncestorTests(unittest.TestCase):
    def setUp(self):
        root = TreeNode(3)
        left = TreeNode(4)
        right = TreeNode(5)
        left_left = TreeNode(1)
        left_right = TreeNode(2)

        root.left = left
        root.right = right
        root.left.left = left_left
        root.left.right = left_right

        t_root = TreeNode(4)
        t_left = TreeNode(1)
        t_right = TreeNode(2)

        t_root.left = t_left
        t_root.right = t_right

        self.sut = EarliestAncestor(root)

    def test_immediate_parent(self):
        self.assertEqual(4, self.sut.common_ancestor(1, 2))

    def test_root(self):
        self.assertEqual(3, self.sut.common_ancestor(1, 4))

    def test_none(self):
        self.assertEqual(None, self.sut.common_ancestor(1, 3))

if __name__ == '__main__':
    unittest.main()