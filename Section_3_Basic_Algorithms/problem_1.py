def sqrt(n: int) -> int:
    print("n:", n)
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number")
    if n < 2:
        return n
    
    # start with a rough estimate of the square root
    x = n // 2
    print("x:", x)
    
    # loop until the estimate stops changing
    while True:
        y = (x + n // x) // 2
        print("y:", y)
        if y >= x:
            return x
        x = y

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (5 == sqrt(25)) else "Fail")
print ("Pass" if  (1 == sqrt(2)) else "Fail")
print(sqrt(-5)) # should throw an a error
