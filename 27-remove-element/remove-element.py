class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        temp = 0
        while i <= j:
            if nums[i] == val:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j -= 1
            else:
                i += 1
            
        return j+ 1