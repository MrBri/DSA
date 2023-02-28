"""
Solution of;
Project: Problems vs Algorithms
Problem 3: Rearrange Array Digits
"""


# mergesort function
def merge_sort(list):

    if len(list) <= 1:
        return list

    mid = len(list) // 2
    l = list[:mid]
    r = list[mid:]

    l = merge_sort(l)
    r = merge_sort(r)

    return merge(l, r)


def merge(l, r):

    merged = []
    l_index = 0
    r_index = 0

    while l_index < len(l) and r_index < len(r):
        if l[l_index] > r[r_index]:
            merged.append(r[r_index])
            r_index += 1
        else:
            merged.append(l[l_index])
            l_index += 1

    merged += l[l_index:]
    merged += r[r_index:]

    return merged


def rearrange_array(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    input_list = merge_sort(input_list)
    print("sort: ", input_list)

    i = len(input_list) - 1

    out_1 = ""
    out_2 = ""

    while i >= 0:

        if i % 2 == 0:
            out_1 += str(input_list[i])

        else:
            out_2 += str(input_list[i])

        i -= 1

    if out_1 > out_2:

        return list(map(int, [out_1, out_2]))

    return list(map(int, [out_2, out_1]))


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
