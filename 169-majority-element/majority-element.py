class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Solution 1
        # freq = {}
        # result = 0
        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1


        # for num, count in freq.items():
        #     if count > len(nums)/2:
        #         result = num 
        #         return result
                
        # Solution 2
        # nums.sort()
        # count = 0
        # for i in range(0,len(nums)):
            
        #     if nums[i] == nums[i-1]:
        #         count += 1
        #         if count > len(nums)/2:
        #             return nums[i]

        #     else:
        #         count = 1

        # Solution 3 most optimal ans with space complexity of O(1)
        count, res = 0,0

        for n in nums:
            if count == 0:
                res = n

            if n == res:
                count += 1
            else:
                count -= 1
        return res