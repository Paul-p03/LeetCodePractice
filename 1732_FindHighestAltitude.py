class Solution(object):
    def largestAltitude(self, gain):
        inp = len(gain)
        max_inp = 0
        alt = 0

        for i in range(inp):
            alt += gain[i]
            max_inp = max(alt, max_inp)

        return max_inp 
