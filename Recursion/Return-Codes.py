def get_alphabet(number):
    """
    Helper function to convert a number to its corresponding alphabet
    """
    return chr(number + 96)

def all_codes(number):
    if number == 0:
        return [""]
    
    # Split the number into 2 digits and calculate the alphabet codes for each part
    two_digit_number = number % 100
    alphabet_codes_100 = []
    if two_digit_number <= 26 and number > 9:
        alphabet_codes_100 = all_codes(number // 100)
        alphabet = get_alphabet(two_digit_number)
        for i, code in enumerate(alphabet_codes_100):
            alphabet_codes_100[i] = code + alphabet
        print(f"Alphabet codes for two digits: {alphabet_codes_100}")
    
    one_digit_number = number % 10
    alphabet_codes_10 = all_codes(number // 10)
    alphabet = get_alphabet(one_digit_number)
    for i, code in enumerate(alphabet_codes_10):
        alphabet_codes_10[i] = code + alphabet
    print(f"Alphabet codes for one digit: {alphabet_codes_10}")
        
    # Combine the alphabet codes for both parts
    alphabet_codes = alphabet_codes_100 + alphabet_codes_10
    print(f"Combined alphabet codes: {alphabet_codes}")
    return alphabet_codes

def test_function(test_case):
    number = test_case[0]
    solution = test_case[1]
    
    output = all_codes(number)
    
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
