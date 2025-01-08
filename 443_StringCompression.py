class Solution(object):
    def compress(self, chars):
        duplicates = []
        count = 1
        

        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                duplicates.append(chars[i-1])
                if count > 1:
                    duplicates.append(str(count))
                count = 1
            
        if len(chars) > 0:
            duplicates.append(chars[-1])
            if count > 1:
                duplicates.append(str(count))

        return duplicates

if __name__ == "__main__":
    solution = Solution()
    char = ["a","a","b","b", "b","c","c"]
    result = solution.compress(char)
    print(result)
