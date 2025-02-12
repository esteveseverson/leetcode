from typing import List

def maximum_sum(nums: List[int]) -> int:
    number_sum = {}
    asw = -1
    
    for num in nums:

        sum_pair = sum(int(digit) for digit in str(num))

        if sum_pair in number_sum:
            number_sum[sum_pair].append(num)
        else:
            number_sum[sum_pair] = [num]

    for key in number_sum:
        if len(number_sum[key]) > 1:
            number_sum[key].sort(reverse=True)
            asw = max(asw, number_sum[key][0] + number_sum[key][1])
    
    return asw

nums = [27, 43, 36, 13, 7, 18]
print(maximum_sum(nums))  # Output: 54

nums = [10, 12, 19, 14]
print(maximum_sum(nums))  # Output: -1