class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hash = {}
        
        for num in nums:
            if num in hash:
                hash[num] += 1
            
            else:
                hash[num] = 1

        for h in hash:
            if hash[h] > len(nums)/2:
                return h