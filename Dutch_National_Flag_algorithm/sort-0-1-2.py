def sort_012(arr):
    # initialize pointers
    low = 0
    high = len(arr) - 1
    mid = 0
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    
    return arr

arr = [2, 1, 0, 2, 1, 0, 1, 2, 0]
sorted_arr = sort_012(arr)
print(sorted_arr)  # Output: [0, 0, 0, 1, 1, 1, 2, 2, 2]

