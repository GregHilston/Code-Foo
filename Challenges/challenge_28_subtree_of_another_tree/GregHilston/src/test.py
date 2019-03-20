import unittest
from solution import TreeNode
from solution import SubTreeOfAnotherTree

class SubTreeOfAnotherTreeTests(unittest.TestCase):
    def setUp(self):
        self.sut = SubTreeOfAnotherTree()

    def test_1(self):
        # Given
        s_root = TreeNode(3)
        s_left = TreeNode(4)
        s_right = TreeNode(5)
        s_left_left = TreeNode(1)
        s_left_right = TreeNode(2)

        s_root.left = s_left
        s_root.right = s_right
        s_root.left.left = s_left_left
        s_root.left.right = s_left_right

        t_root = TreeNode(4)
        t_left = TreeNode(1)
        t_right = TreeNode(2)

        t_root.left = t_left
        t_root.right = t_right

        # When
        output = self.sut.isSubtree(s_root, t_root)

        # Then
        self.assertEqual(True, output)

if __name__ == '__main__':
    unittest.main()