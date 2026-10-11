class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        initial = strs[0]
        
        for str in strs[1:]:
            i = 0
            while not str.startswith(initial):    
                initial = initial[:-1]
        
        return initial
            