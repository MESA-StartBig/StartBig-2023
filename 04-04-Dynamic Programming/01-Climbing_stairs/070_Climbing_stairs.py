class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0: 1, 1: 1}

        def recursiveClimbStairs(stairs_left):
        
            if stairs_left in memo:
                return memo[stairs_left]
            
            if stairs_left < 0:
                return 0
            
            memo[stairs_left] = recursiveClimbStairs(stairs_left-1) + recursiveClimbStairs(stairs_left-2) 
            return memo[stairs_left]

        res = recursiveClimbStairs(n)
        return res
    