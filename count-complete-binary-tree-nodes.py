# Time:  O(h * logn) = O((logn)^2)
# Space: O(1)

# Given a complete binary tree, count the number of nodes.
#
# In a complete binary tree every level, except possibly the last,
# is completely filled, and all nodes in the last level are as far
# left as possible. It can have between 1 and 2h nodes inclusive at
# the last level h.
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if root is None:
            return 0
        
        node, level = root, 0
        while node.left is not None:
            node = node.left
            level += 1
        
        # Binary search.
        left, right = 2 ** level, 2 ** (level + 1)
        while left < right:
            mid = left + (right - left) / 2
            if not self.exist(root, mid):
                right = mid
            else:
                left = mid + 1
                
        return left - 1
    
    # Check if the nth node exist.
    def exist(self, root, n):
        k = 1
        while k <= n:
            k <<= 1
        k >>= 2
        
        node = root
        while k > 0:
            if (n & k) == 0:
                node = node.left
            else:
                node = node.right
            k >>= 1
        return node is not None
********************************************************************
# Time:  O(n)
# Space: O(1)
# 
# Given a binary tree, determine if it is a valid binary search tree (BST).
# 
# Assume a BST is defined as follows:
# 
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Morris Traversal Solution
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def isValidBST(self, root):
        prev, cur = None, root
        while cur:
            if cur.left is None:
                if prev and prev.val >= cur.val:
                    return False
                prev = cur
                cur = cur.right
            else:
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right
            
                if node.right is None:
                    node.right = cur
                    cur = cur.left
                else:
                    if prev and prev.val >= cur.val:
                        return False
                    node.right = None
                    prev = cur
                    cur = cur.right
                
        return True

*************************************************************
# Time:  O(n)
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def isValidBST(self, root):
        return self.isValidBSTRecu(root, float("-inf"), float("inf"))

    def isValidBSTRecu(self, root, low, high):
        if root is None:
            return True
        return low < root.val and root.val < high \
            and self.isValidBSTRecu(root.left, low, root.val) \
                and self.isValidBSTRecu(root.right, root.val, high)

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    s = Solution().isValidBST(root)
    print("Binary tree right side view BFS traversal is -")
    print(s)
