class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """


        p1 = 0
        p2 = len(height) - 1
        max_area = 0
        
        while p1 < p2:
            area = min(height[p1], height[p2]) * (p2 - p1)

            max_area = max(max_area, area)

            if p1 > p2:
                p2 -= 1

            else:
                p1 += 1
        return max_area
    
if __name__ == "__main__":
    solution = Solution()
    max_area = solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(f'Bounds with largest area: {max_area}')