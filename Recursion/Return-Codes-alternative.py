def get_alphabet(number):
    """
    Helper function to convert a number to its corresponding alphabet
    """
    return chr(number + 96)

"""
def all_codes(number):
    def get_alphabet(num):
        return chr(num + 96)
    
    if number == 0:
        return [""]
    
    codes = []
    if number >= 10 and number <= 26:
        codes = all_codes(number // 100)
        for i, code in enumerate(codes):
            codes[i] = code + get_alphabet(number % 100)
    else:
        codes = all_codes(number // 10)
        for i, code in enumerate(codes):
            codes[i] = code + get_alphabet(number % 10)
            
    return codes
"""

def all_codes(number):
    if number == 0:
        return [""]
    
    output = []
    # calculation for two right-most digits e.g. if number = 1123, this calculation is meant for 23
    if number > 9 and number % 100 <= 26:
        output_100 = all_codes(number // 100)
        alphabet = get_alphabet(number % 100)
        
        for _, element in enumerate(output_100):
            output.append(element + alphabet)

    output_10 = all_codes(number // 10)
    alphabet = get_alphabet(number % 10)
    
    for _, element in enumerate(output_10):
        output.append(element + alphabet)
        
    return output

def test_function(test_case):
    number = test_case[0]
    solution = test_case[1]
    
    output = all_codes(number)
    print('OUTPUT:', output)
    
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")

number = 123
solution = ['abc', 'aw', 'lc']
test_case = [number, solution]
test_function(test_case)

number = 1145
solution =  ['aade', 'ane', 'kde']
test_case = [number, solution]
test_function(test_case)
