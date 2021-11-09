# Time:  O(n)
# Space: O(n)
#
# Given a binary tree, return the level order traversal of its nodes' values. 
# (ie, from left to right, level by level).
#
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#    3
#   / \
#  9  20
#    /  \
#   15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#
# Definition for a  binary tree node

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        queue, current = [], [root]

        while current:
            next_level, vals = [], []
            for root in current:
                vals.append(root.val)
                if root.left:
                    next_level.append(root.left)
                if root.right:
                    next_level.append(root.right)
            current = next_level
            queue.append(vals)
        return queue

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    s = Solution().levelOrder(root)
    print("Level Order Traversal of binary tree is -")
    print(s)
