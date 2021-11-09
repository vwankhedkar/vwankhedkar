# Time:  O(n)
# Space: O(1)
#
# You are climbing a stair case. It takes n steps to reach to the top.
# 
# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?

class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        return min(self.minCost(n-1, cost), self.minCost(n-2, cost))

    def minCost(self, i, cost):
        if (i < 0):
            return 0
        if (i == 0 or i == 1):
            return cost[i]
        return cost[i] + min(self.minCost(i - 1, cost), self.minCost(i - 2, cost))


if __name__ == "__main__":
    result = Solution().minCostClimbingStairs([10, 15, 30])
    print(result)
*****************************************************************************
class Solution:
    """
    :type n: int
    :rtype: int
    """
    def climbStairs(self, n):
        prev, current = 0, 1
        for i in xrange(n):
            prev, current = current, prev + current, 
        return current

    # Time:  O(2^n)
    # Space: O(n)
    def climbStairs1(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

if __name__ == "__main__":
    result = Solution().climbStairs(2)
    print result
