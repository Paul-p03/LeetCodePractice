class Solution(object):
    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False

        first = second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
        
if __name__ == "__main__":
    solution = Solution()
    result1 = solution.increasingTriplet([1, 2, 3, 4, 5])
    result2 = solution.increasingTriplet([5, 4, 3, 2, 1])
    print(result1)
    print(result2)