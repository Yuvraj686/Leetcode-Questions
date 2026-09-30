class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left = []
        product = 1

        for i in range(len(nums)):
            if i == 0:
                left.append(1)
            else:
                product = product * nums[i-1]
                left.append(product)
        right = []
        product = 1
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                right.append(1)
            else:
                product = product * nums[i+1]
                right.append(product)

        right.reverse()
        
        ans = []
        for i in range(len(nums)):
            k = right[i]*left[i]
            ans.append(k)

        return ans
