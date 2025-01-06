class Solution(object):
    def reverseWords(self, s):
        swapOrder = s.split()  # Split the string into a list of words
        reverseList = swapOrder[::-1]  # Reverse the list
        return ' '.join(reverseList)  # Join the reversed list into a string

if __name__ == "__main__":
    solution = Solution()
    print("Give me liberty, or give me death!")
    print(solution.reverseWords("Give me liberty, or give me death!"))
    