class Solution(object):
    def findMaxAverage(self, nums, k):
        currentTotal = sum(nums[:k])
        maxAvg = currentTotal
        
        for j in range(k, len(nums)):
            currentTotal += nums[j] - nums[j-k]
            maxAvg = max(maxAvg, currentTotal)

        return maxAvg / float(k)
        
        
if __name__ == "__main__":
    solution = Solution()
    testCount = [43, 11, -19, -6, 22, 34, 14, 17, -2, 58]
    print(solution.findMaxAverage(testCount, 4))
