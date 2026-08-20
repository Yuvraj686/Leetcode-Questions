class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = {}
        curr = 0
        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1
                
            curr = max(curr,right - left + 1)
            seen[s[right]] = right
            
        return curr
        


