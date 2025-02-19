class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = []
        stack = []

        lenght = len(pattern)

        for i in range(lenght + 1):
            stack.append(i + 1)

            if i == lenght or pattern[i] == 'I':
                while stack:
                    result.append(str(stack.pop()))

        return ''.join(result)


# Test cases
print(Solution().smallestNumber("IIIDIDDD"))  
print(Solution().smallestNumber("DDD"))  