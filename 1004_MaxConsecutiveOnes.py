class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        p1 = 0
        count = 0
        max_seq = 0

        for p2 in range(len(nums)):
            if nums[p2] == 0:
                count += 1

            while count > k:
                if nums[p1] == 0:
                    count -= 1
                p1 += 1
            max_seq = max(max_seq, p2 - p1 + 1)
        return max_seq
    
if __name__ == "__main__":
    solution = Solution()
    test = solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)
    print(test)