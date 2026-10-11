class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}

        for i in range(len(s)):
            if s[i] in seen:
                seen[s[i]][0] += 1
            
            else:
                char = s[i]
                frequency = 1
                index = i
                seen[char] = [frequency,index]


        for s in seen:
            if seen[s][0] == 1:
                return seen[s][1]

        return -1            
