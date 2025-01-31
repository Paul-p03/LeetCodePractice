class Solution:
    def longestSubarray(self, nums):
        left = 0
        max_length = 0
        zero_count = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
        
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Calculate window length and updates max_length
            max_length = max(max_length, right - left)
        
        
        if max_length == len(nums):
            return max_length - 1
        
        return max_length

nums1 = [1,1,0,1]
nums2 = [0,1,1,1,0,1,1,0,1]
nums3 = [1,1,1]

solution = Solution()
print(solution.longestSubarray(nums1))  
print(solution.longestSubarray(nums2))  
print(solution.longestSubarray(nums3))  
