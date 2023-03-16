def rotated_array_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # check if the left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        # check if the right half is sorted
        else:
            if nums[mid] < target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    # target not found
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

nums = [4,5,6,7,0,1,2]
target = 0
index = rotated_array_search(nums, target)
print(index)  # output: 4


nums = [3, 1, 2]
target = 0
index = rotated_array_search(nums, target)
print(index)  # output: -1

nums = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10
index = rotated_array_search(nums, target)
print(index)  # output: 0


nums = []
target = 1
index = rotated_array_search(nums, target)
print(index)  # output: -1
