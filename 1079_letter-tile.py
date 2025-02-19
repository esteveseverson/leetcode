from collections import Counter

def numTilePossibilities(tiles: str) -> int:
    # Function to count the number of sequences using backtracking
    def backtrack(current_sequence, frequency_map):
        # If current_sequence is not empty, count it as a valid sequence
        if current_sequence:
            result[0] += 1
        
        # Try every character in frequency_map
        for char in frequency_map:
            if frequency_map[char] > 0:
                # Choose this character and decrement its count
                frequency_map[char] -= 1
                # Recurse to explore further possibilities
                backtrack(current_sequence + char, frequency_map)
                # Backtrack, restore the character's count
                frequency_map[char] += 1
    
    # Step 1: Create a frequency map of the tiles
    frequency_map = Counter(tiles)
    
    # Step 2: Initialize result to count valid sequences
    result = [0]
    
    # Step 3: Start backtracking with an empty current sequence
    backtrack("", frequency_map)
    
    # Step 4: Return the result
    return result[0]

# Test cases
print(numTilePossibilities("AAB"))  # Output: 8
print(numTilePossibilities("ABCDEFGH"))  # Output: 188
print(numTilePossibilities("V"))  # Output: 1
