class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i,num in enumerate(nums):
            k  = target - num

            if k in seen:
                return [seen[k],i]
            else:
                seen[num] = i

        for s in seen:
            left = target - s
            if left in seen:
                return [seen[s],seen[left]]