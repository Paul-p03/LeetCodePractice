class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        values = {}
        for num in arr:
            if num in values:
                values[num] += 1
            else: 
                values[num] = 1

        appear = list(values.values())

        return len(appear) == len(set(appear))

solution = Solution()
arr1 = [1, 2, 2, 1, 1, 3]
print(solution.uniqueOccurrences(arr1))
arr2 = [1, 2]
print(solution.uniqueOccurrences(arr2))
