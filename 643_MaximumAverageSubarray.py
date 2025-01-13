class Solution(object):
    def findMaxAverage(self, nums, k):
    
        current_sum = sum(nums[:k])
        max_avg = current_sum / k
        
        
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_avg = max(max_avg, current_sum / k)
        
        return max_avg
        
if __name__ == "__main__":
    solution = Solution()
    testCount = [1, 12, -5, -6, 50, 3]
    print(solution.findMaxAverage(testCount, 4))
