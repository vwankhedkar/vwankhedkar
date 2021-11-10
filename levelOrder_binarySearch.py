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
***********************************************************************************
                 2
            8        9
          1  3     4   5
Should return following list:

[2,8,9,1,3,4,5]

def tree_by_levels(node):
    # create a return list, and a queue to loop
    p, q = [], [node]
    # loop
    while q:
        # take the first item from the queue
        v = q.pop(0)
        # if it is not empty
        if v is not None:
            # add it's value to the return list
            p.append(v.value)
            # add the left and right nodes to the queue
            q += [v.left,v.right]
    # return the final list, otherwise return [] is empty
    return p if not node is None else []
       
    from collections import deque


def tree_by_levels(node):
    if not node:
        return []
    res, queue = [], deque([node,])
    while queue:
        n = queue.popleft()
        res.append(n.value)
        if n.left is not None:
            queue.append(n.left)
        if n.right is not None:
            queue.append(n.right)
    return res

def tree_by_levels(node):
    r = []
    nodes = [node]
    while nodes:
        r += [n.value for n in nodes if n]
        nodes = [e for n in [(n.left, n.right) for n in nodes if n] for e in n if e]
        
    return r
