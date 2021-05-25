class Solution:
    def solve(self, nums):
        products =[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if i != j:
                    products.append(nums[i]*nums[j])
        return max(products)