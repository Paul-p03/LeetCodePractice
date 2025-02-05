class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        w1 = len(s1)
        w2 = len(s2)

        if w1 != w2:
            return False
        
        elif w1 == w2:
            sort1 = ''.join(sorted(s1))
            sort2 = ''.join(sorted(s2))
            if sort1 == sort2:
                
                return True
            else:
                return False