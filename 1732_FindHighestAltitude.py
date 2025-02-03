class Solution(object):
    def largestAltitude(self, gain):
        inp = len(gain)
        max_inp = 0
        alt = 0

        for i in range(inp):   #Finds highest sequential summation point
            alt += gain[i]
            max_inp = max(alt, max_inp)

        return max_inp 

solution = Solution()
array_input = solution.largestAltitude([-5,1,5,0,-7])
print(f'Highest Altitude reached during road trip: {array_input}')