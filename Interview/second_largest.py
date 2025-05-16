def second_larget_number(arr):
    if len(arr) < 2:
        return None
    
    unique_numbers = set(arr)
    if len(unique_numbers) < 2:
        return None
    unique_numbers.remove(max(unique_numbers))
    return max(unique_numbers)

# Test cases        
print(second_larget_number([1, 2, 3, 4, 5]))  # Output: 4
print(second_larget_number([5, 5, 5, 5]))     # Output: None