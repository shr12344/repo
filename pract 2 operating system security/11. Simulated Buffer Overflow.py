#11. Simulated Buffer Overflow

def safe_array_write(array, index, value):
    if index < len(array):
        array[index] = value
        return " Value written"
    else:
        return " Buffer Overflow Attempt!"
    
    
arr = [0] * 5
print(safe_array_write(arr, 2, 10))
print(safe_array_write(arr, 8, 10))
