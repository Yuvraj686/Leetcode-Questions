class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProd = 1
        ans = []
        for i in range(len(nums)):
            ans.append(leftProd)
            leftProd = leftProd * nums[i]
            
        rightProd = 1

        for i in range(len(nums)-1,-1,-1):
            ans[i] = ans[i]*rightProd
            rightProd = rightProd*nums[i]

        
        return ans