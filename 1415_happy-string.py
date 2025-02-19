class Solution:
    
    def generate_happy_string(self, n, current_str, result, prev_char):
        if len(current_str) == n:
            result.append(current_str)
            return

        for char in ['a', 'b', 'c']:
            if char != prev_char:
                self.generate_happy_string(n, current_str + char, result, char)

    def getHappyString(self, n: int, k: int) -> str:
        result = []
        self.generate_happy_string(n, '', result, '')

        if len(result) < k:
            return ''
        
        return result[k - 1]
    
print(Solution().getHappyString(1, 3)) # c
print(Solution().getHappyString(1, 4)) # ''
print(Solution().getHappyString(3, 9)) # cab
print(Solution().getHappyString(4, 16))
print(Solution().getHappyString(5, 25))