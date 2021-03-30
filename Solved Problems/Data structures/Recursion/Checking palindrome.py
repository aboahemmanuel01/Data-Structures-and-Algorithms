'''
A palindrome is a word that is the reverse of itself—that is, it is the same word when read forwards and backwards.
For example:
"madam" is a palindrome
'''
def is_palindrome(input):
    """
    Return True if input is palindrome, False otherwise.

    Args:
       input(str): input to be checked if it is palindrome
    """
    # Termination / Base condition
    if len(input) <= 1:
        return True
    else:
        first_char = input[0]
        last_char = input[-1]

        # sub_input is input with first and last char removed
        sub_input = input[1:-1]

        # recursive call, if first and last char are identical, else return False
        return (first_char == last_char) and is_palindrome(sub_input)

print ("Pass" if  (is_palindrome("")) else "Fail")
print ("Pass" if  (is_palindrome("a")) else "Fail")
print ("Pass" if  (is_palindrome("madam")) else "Fail")
print ("Pass" if  (is_palindrome("abba")) else "Fail")
print ("Pass" if not (is_palindrome("Udacity")) else "Fail")



'''

# AN ALTERNATIVE SOLUTION TO THE PROBLEM ###


def recurse_input(input):
    
    if len(input) == 0:
        return ""
    
    else:
        first = input[0]
        the_rest = slice(1, None)
        sliced = input[the_rest]
    
        palindrome = recurse_input(sliced)
        
        answer = palindrome + first
            
        return answer


def is_palindrome(input):

    """
    Return True if input is palindrome, False otherwise.
    
    Args:
       input(str): input to be checked if it is palindrome
    """
    
    word = input 
    if input is None:
        return True
    
    else:
        
        return recurse_input(input) == word
    
    
'''
