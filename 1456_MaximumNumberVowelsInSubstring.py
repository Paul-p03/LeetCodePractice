class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = set('aeiou')
        string = len(s)
        max_vowel = 0
        current_vowel = 0

        for i in range(k):
            if s[i] in vowels:
                current_vowel += 1
        max_vowel = current_vowel # swaps the max value to allow current vowel to be tracked in second loop

        for i in range(k, string):
            if s[i - k] in vowels: #Sliding window leaves a letter, decrements from list if a vowel
                current_vowel -= 1
            if s[i] in vowels: #Sliding window adds new letter and increments current if a vowel
                current_vowel += 1
            max_vowel = max(max_vowel, current_vowel)
        return max_vowel

if __name__ == "__main__":
    solution = Solution()
    substring = solution.maxVowels("abciiidef", 3)
    print(f'Vowels: {substring}')