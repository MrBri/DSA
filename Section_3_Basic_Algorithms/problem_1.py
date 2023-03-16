def sqrt(n: int) -> int:
    if n < 0:
        raise ValueError("Square root not defined for negative numbers.")
    
    left, right = 0, n

    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid

        if mid_squared == n:
            return mid
        elif mid_squared < n:
            left = mid + 1
        else:
            right = mid - 1

    return left - 1

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (5 == sqrt(25)) else "Fail")
print ("Pass" if  (1 == sqrt(2)) else "Fail")
print(sqrt(-5)) # should throw an a error
