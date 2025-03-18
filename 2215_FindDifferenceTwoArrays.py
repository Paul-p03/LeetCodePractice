class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        result1 = []
        result2 = []

        for num in nums1:
            if num not in nums2 and num not in result1:
                result1.append(num)
        for num in nums2:
            if num not in nums1 and num not in result2:
                result2.append(num)

        return [result1, result2]

solution = Solution()
num1 = [1, 2, 3]
num2 = [2, 4, 6]
solution = solution.findDifference(num1, num2)
print(solution)
        