# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class EarliestAncestor:
    def __init__(self, root: TreeNode):
        self.root = root

    def depth_first_search(self, needle: int, haystack: int, path: [int]):
        # if haystack:
            # print(f"Looking for {needle} and at haystack {haystack.val} and path {path}")
        if haystack == None or haystack.val == needle:
            return path

        path.append(haystack.val)

        left_search = self.depth_first_search(needle, haystack.left, path)
        if left_search:
            return left_search

        right_search = self.depth_first_search(needle, haystack.right, path)
        if right_search:
            return right_search

    def last_common(self, list_one: [int], list_two: [int]):
        last_match = None

        for i, j in zip(list_one, list_two):
            if i == j:
                last_match = i

        return last_match

    def common_ancestor(self, id_one: int, id_two: int):
        id_one_path = self.depth_first_search(id_one, self.root, [])
        id_two_path = self.depth_first_search(id_two, self.root, [])

        # print(f"id_one_path {id_one_path}")
        # print(f"id_two_path {id_two_path}")

        return self.last_common(id_one_path, id_two_path)