# Solution
## Read input as specified in the question.
## Print output as specified in the question.


def staircase(n):
    if n <= 0:
        return 1
    
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    
    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)

def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = staircase(n)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

n = 3
solution = 4
test_case = [n, solution]
test_function(test_case)

n = 4
solution = 7
test_case = [n, solution]
test_function(test_case)

n = 7
solution = 44
test_case = [n, solution]
test_function(test_case)
