class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        nums.sort()
        p1 = 0
        p2 = len(nums) - 1
        count = 0

        while p1 < p2:
            sum = nums[p1] + nums[p2]
            if sum == k:
                count += 1
                nums.pop(p2)
                nums.pop(p1)
                
                p1 = 0
                p2 = len(nums) - 1
            elif sum < k:
                p1 += 1

            else:
                p2 -= 1
        return count
    
if __name__ == "__main__":
    solution = Solution()
    x = solution.maxOperations([1,2,3,4], 5)
    print(f'The max number of K-sum pairs are: {x}')