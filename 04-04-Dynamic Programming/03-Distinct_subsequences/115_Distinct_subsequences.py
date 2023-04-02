class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        # memoization
        memo = {}

        # recursive function with memoization
        def dp(i, j):

            # if we reach the end of the string t
            # -> we found a match
            if j == len(t):
                return 1

            # if we reach the end of the string s
            # -> we did not find a match
            if i == len(s):
                return 0

            # check if the result for the given (i, j) indices has already been computed
            if (i, j) in memo:
              return memo[(i, j)]

            # if the characters at indices i and j match
            if s[i] == t[j]:
                # we can include the character and move to the next character in both strings: dp(i+1, j+1)
                # or we can decide not to include the character:  dp(i+1, j)
                memo[(i, j)] = dp(i+1, j+1) + dp(i+1, j)
            else:
                # we skip the character in s and move to the next character in t
                memo[(i, j)] = dp(i+1, j)

            # return the result of the subproblem for the given (i, j) indices
            return memo[(i, j)]

        return dp(0, 0)
