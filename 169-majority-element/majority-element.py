class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # freq = {}
        # result = 0
        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1


        # for num, count in freq.items():
        #     if count > len(nums)/2:
        #         result = num 
        #         return result
                
        
        nums.sort()
        count = 0
        for i in range(0,len(nums)):
            
            if nums[i] == nums[i-1]:
                count += 1
                if count > len(nums)/2:
                    return nums[i]

            else:
                count = 1