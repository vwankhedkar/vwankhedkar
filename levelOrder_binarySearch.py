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
***************************************************************
DFS - right side reversal 
# Time:  O(n)
# Space: O(h)
#
# Given a binary tree, imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.
#
# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# You should return [1, 3, 4].
#

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def rightSideView(self, root):
        result = []
        self.rightSideViewDFS(root, 1, result)
        return result

    def rightSideViewDFS(self, node, depth, result):
        if not node:
            return
        if depth > len(result):
            result.append(node.val)
        self.rightSideViewDFS(node.right, depth+1, result)
        self.rightSideViewDFS(node.left, depth+1, result)

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    s = Solution().rightSideView(root)
    print("Binary tree right side view traversal is -")
    print(s)
    
  **********************************************************
BFS 
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def rightSideView(self, root):
        if root is None:
            return []

        result, current = [], [root]
        while current:
            next_level = []
            for i, node in enumerate(current):
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                if i == len(current) - 1:
                    result.append(node.val)
            current = next_level
        return result

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    s = Solution().rightSideView(root)
    print("Binary tree right side view BFS traversal is -")
    print(s)
