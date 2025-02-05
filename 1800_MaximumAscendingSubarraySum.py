class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_arr = len(nums)
        total_sub = max_amount = nums[0]

        for i in range(1, max_arr):
            if nums[i] > nums[i-1]: #if the order is ascending, sum the next value
                total_sub += nums[i]
            else:
                total_sub = nums[i] # start new summing sequence
            max_amount = max(total_sub, max_amount)

        return max_amount

solution = Solution()
test1 = solution.maxAscendingSum([10,20,30,5,10,50])
print(f"Largest ascending sum: {test1}")