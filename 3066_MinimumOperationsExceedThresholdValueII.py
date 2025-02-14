class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
    
        operations = 0
    
        while len(nums) > 1 and nums[0] < k:
            x = nums.pop(0)  
            y = nums.pop(0)  
        
            new_value = min(x, y) * 2 + max(x, y)
            nums.append(new_value)
            nums.sort()
            operations += 1

        if nums[0] >= k:
            return operations
    
        return -1

solution = Solution()
nums = [2, 11, 10, 1, 3]
k = 10
print(solution.minOperations(nums, k)) 