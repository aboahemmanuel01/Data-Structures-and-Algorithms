'''
Problem Definition:

In an encryption system where ASCII lower case letters represent numbers in the pattern a=1, b=2, c=3... and so on, 
this code finds out all the encrption that are possible for a given input number.

For example:
number = 123
codes_possible = ["aw", "abc", "lc"]


Assumption: Input number will never contain any 0s

'''

def all_codes(number):
    """
    :param: number - input integer
    Return - list() of all codes possible for this number
    """
    # Base case
    if number == 0:
        return [""]
    
    # calculation for two right-most digits e.g. if number = 1123, this calculation is meant for 23
    remainder = number % 100
    output_100 = list()
    
    if remainder <= 26 and number > 9: # there are 26 letters of the alphabet
        output_100 = all_codes(number // 100)
        
        alphabet = get_alphabet(remainder)
        for idx, num in enumerate(output_100):
            output_100[idx] = num + alphabet
            
            
    # calculation for right-most digit e.g. if number = 1123, this calculation is meant for 3
    remainder = number%10
    
    # get all codes for the remaining number
    output_10 = all_codes(number//10)
    
    alphabet = get_alphabet(remainder)
    for idx, num in enumerate(output_10): 
        output_10[idx] = num + alphabet
        
    output = list()
    output.extend(output_100)
    output.extend(output_10)
    
    
    return output
    
    
def get_alphabet(number):
    '''
    The alphabet has 26 letters and char(int) returns the ASCII character of a number
    But ASCII for lower case "a" = 97 which is equivalent to 1 for the encryption.
    Example: chr(65) = "A" and chr(1 + 96) = "a"
    '''
        
    return chr(number + 96)
  
  
  
  
# Test cases
def test_function(test_case):
    number = test_case[0]
    solution = test_case[1]
    
    output = all_codes(num)
    
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")
        
        
# Case 1
number = 123
solution = ['abc', 'aw', 'lc']
test_case = [number, solution]
test_function(test_case)
