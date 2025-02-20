from typing import List

class Solution:
    
    def generate_binary(self, n, current_binary, result):
        if len(current_binary) == n:
            result.append(current_binary)
            return

        for binary in ['0', '1']:
            self.generate_binary(n, current_binary + binary, result)

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        lenght = len(nums[0])
        binary_list = []

        self.generate_binary(lenght, '', binary_list)

        for binary in binary_list:
            if binary not in nums:
                return binary

        return ''
    
print(Solution().findDifferentBinaryString(["01","10"]))
print(Solution().findDifferentBinaryString(["00","01"]))
print(Solution().findDifferentBinaryString(["111","011","001"]))