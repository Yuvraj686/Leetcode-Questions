class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group = {}

        for str in strs:
            key = "".join(sorted(str))

            if key in group:
                group[key].append(str)
            else:
                group[key] = [str]
            
        return list(group.values())