class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        # Convert dictionary to a set for O(1) lookups
        word_set = set(dictionary)
        n = len(s)
        
        # dp[i] will hold the minimum number of extra characters in s[:i]
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # Start with the worst case, all characters up to i are extra
            dp[i] = dp[i - 1] + 1
            
            # Check all possible words ending at position i
            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])  # Update to the best option
            
        return dp[n]

# Example usage
solution = Solution()
s = "leetscode"
dictionary = ["leet", "code", "leetcode"]
result = solution.minExtraChar(s, dictionary)
print(result)  # Output: 1 (the character 's' is extra)
