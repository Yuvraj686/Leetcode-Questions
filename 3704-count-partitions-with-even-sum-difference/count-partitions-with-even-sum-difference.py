class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0
        left = nums[0]
        right = 0
        for i in range(1,len(nums)):
            right += nums[i]

        for i in range(1,len(nums)):
            if (left - right) % 2 == 0:
                count +=1
            left += nums[i]
            right -= nums[i]
        return count