class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = {}
        seen2 = {}

        for s in s:
            seen1[s] = seen1.get(s,0) + 1

        for t in t:
            seen2[t] = seen2.get(t,0) + 1

        if seen1 == seen2:
            return True
        return False