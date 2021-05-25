class Solution:
    def solve(self, nums):
        n = len(nums)
        nums.sort()
        num1 = num2 = 0
        sum1 = nums[0]*nums[1]
        sum2 = nums[n-1]*nums[n-2]
        if sum1 > sum2:
            return sum1
        else:
            return sum2