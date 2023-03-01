def rearrange_array(input_list):
    if len(input_list) < 2:
        return [-1, -1]
    # sort the array in descending order using merge sort
    nums = merge_sort_descending(input_list)
    
    # construct the two numbers by taking alternating digits
    num1, num2 = 0, 0
    for i in range(len(nums)):
        if i % 2 == 0:
            num1 = num1 * 10 + nums[i]
        else:
            num2 = num2 * 10 + nums[i]
    
    return [num1, num2]


def merge_sort_descending(nums):
    # base case
    if len(nums) <= 1:
        return nums
    
    # split the array into two halves
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    
    # sort the left and right halves recursively
    left = merge_sort_descending(left)
    right = merge_sort_descending(right)
    
    # merge the sorted left and right halves
    return merge_descending(left, right)


def merge_descending(left, right):
    result = []
    i = 0
    j = 0
    
    # merge the left and right arrays in descending order
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # append any remaining elements from the left or right array
    result += left[i:]
    result += right[j:]
    
    return result

# test_case[0] is the list that we want to test
# test_case[1] is the result that we expect
def test_function(test_case):
    output = rearrange_array(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])

test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

test_function([[0, 1], [1, 0]])

test_function([[0, 8, 5], [80, 5]])

test_function([[], [-1, -1]])

test_function([[0], [-1, -1]])

test_function([[0, 0], [0, 0]])

test_function([[1, 1, 1, 3, 5, 6], [631, 511]])
