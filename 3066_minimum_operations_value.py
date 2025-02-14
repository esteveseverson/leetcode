import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Create a min-heap from the list
        heapq.heapify(nums)
        asw = 0

        while nums[0] < k:
            if len(nums) < 2:
                return -1

            # Pop the two smallest elements from the heap
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            # Create a new element and push it back to the heap
            new_element = (x * 2) + y
            heapq.heappush(nums, new_element)

            asw += 1
        
        return asw
