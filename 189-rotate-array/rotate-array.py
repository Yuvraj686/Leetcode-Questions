class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Brute force 
        # n = 0
        # temp = 0
        # while n < k:
        #     temp = nums[len(nums)-1]
        #     for i in range(len(nums)-2,-1,-1):
        #         nums[i+1] = nums[i]
        #     nums[0] = temp

        #     n += 1

        n = len(nums)
        k %= n

        count = 0
        start = 0

        while count < n:
            current = start
            prev = nums[start]

            while True:
                nxt = (current + k) % n
                nums[nxt], prev = prev, nums[nxt]
                current = nxt
                count += 1

                if current == start:
                    break

            start += 1       