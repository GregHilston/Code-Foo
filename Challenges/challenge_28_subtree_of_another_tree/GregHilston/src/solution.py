# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SubTreeOfAnotherTree:
    def trees_match(self, s: TreeNode, t: TreeNode) -> bool:
        print("\tRECURSED!")

        # We've run out of s and t. We haven't had a problem, so return true
        if s == None and t == None:
            print("\ts == None and t == None returning True")
            return True

        # We ran out of s but have more in t to match
        if s == None and t != None:
            print("\ts == None and t != None t.val {t.val} returning False")
            return False

        # We more things in s we could match but ran out of things in t to match
        if s != None and t == None:
            print("\ts != None s.val {s.val} and t == None returning False")
            return False

        # Neither are none, so we check value
        if s.val != t.val:
            print(f"\ts.val {s.val} != t.val {t.val} returning False")
            return False
        else:
            # continuing olnly if the values match, otherwise we return false above
            print(f"\ts != none s.val {s.val} and t != none t.val {t.val} SHOULD RECURSE LEFT AND RIGHT")

        return self.trees_match(s.left, t.left) and self.trees_match(s.right, t.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s == None:
            print("s == None")
        else:
            print(f"s.val = {s.val}")

        # if we found a match
        if self.trees_match(s, t):
            return True

        # if we ran out of s to check
        if s == None:
            return False

        # recurse down left s with t and right s with t
        if self.isSubtree(s.left, t) or self.isSubtree(s.right, t):
            return True

        # we found no matches, so this isn't a match
        return False