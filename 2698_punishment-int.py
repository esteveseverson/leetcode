# Function to calculate the sum of the valid partitions of the string of digits
def check_partitions(square_str, target):
    length = len(square_str)
    result = []
    
    # Try all possible splits using backtracking
    def backtrack(start, current_sum, partition):
        if start == length:
            # If the sum of the current partition equals the target, it's a valid partition
            if current_sum == target:
                result.append(partition)
            return
        
        # Explore every possible split from the current position
        for end in range(start + 1, length + 1):
            num_str = square_str[start:end]
            num = int(num_str)  # Convert the substring to an integer
            
            # Skip leading zeros unless the number is exactly '0'
            if num_str[0] == '0' and num_str != '0':
                continue
                
            backtrack(end, current_sum + num, partition + [num])
    
    backtrack(0, 0, [])
    return len(result) > 0

# Function to check if a number i is a punishment number
def is_punishment_number(i):
    square = i * i
    square_str = str(square)
    
    # Check if we can partition the square such that the sum of the parts equals i
    return check_partitions(square_str, i)

# Function to find the punishment number sum for all integers from 1 to n
def find_punishment_number(n):
    total_sum = 0
    for i in range(1, n + 1):
        if is_punishment_number(i):
            total_sum += i * i
    return total_sum

# Test the function with examples
n1 = 10
n2 = 37
n3 = 100
n4 = 1000

print(f"Punishment number sum for n={n1}: {find_punishment_number(n1)}")
print(f"Punishment number sum for n={n2}: {find_punishment_number(n2)}")
print(f"Punishment number sum for n={n3}: {find_punishment_number(n3)}")
print(f"Punishment number sum for n={n4}: {find_punishment_number(n4)}")
