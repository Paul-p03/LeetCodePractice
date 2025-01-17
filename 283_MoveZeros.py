class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nonZeroIndex = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nonZeroIndex] = nums[i]

                nonZeroIndex += 1

        for i in range(nonZeroIndex, len(nums)):
            nums[i] = 0
    
                

if __name__ == "__main__":
    solution = Solution()
    testCount = [0,1,0,3,5]
    solution.moveZeroes(testCount)
    print(f'Final array solutions: {testCount}')