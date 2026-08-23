class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        sum = 0
        result = len(nums)+1

        for j in range(len(nums)):
            sum += nums[j]
            while sum >= target:
                curr = j - i+1
                if curr <= result:
                    result = curr
                sum -= nums[i]
                i += 1
        if result == len(nums)+1:
            return 0
        return result
            