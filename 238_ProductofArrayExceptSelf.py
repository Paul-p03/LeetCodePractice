class Solution(object):
    def productExceptSelf(self, nums):
        length = len(nums)
        ans = [1] * length #initializes array to 1's

        prefix = 1
        for i in range(length):
            ans[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(length-1, -1, -1):
            ans[i] *= suffix  #Combining both prefix and suffix together
            suffix *= nums[i]

        return ans
        
if __name__ == "__main__":
    solution = Solution()
    result = solution.productExceptSelf([1, 2, 3, 4])
    print("Input: 1, 2, 3, 4")
    print("Output: ", result)

