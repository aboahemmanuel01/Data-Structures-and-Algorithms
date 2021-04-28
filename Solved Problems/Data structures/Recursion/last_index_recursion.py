'''
Problem Definition

Given an array arr and a target element target, this code finds the last index of occurence of target in arr using recursion. 
If target is not present in arr, it returns -1.

For example:
For arr = [1, 2, 5, 5, 1, 2, 5, 4] and target = 5, output = 6
For arr = [1, 2, 5, 5, 1, 2, 5, 4] and target = 7, output = -1

'''

def last_index(arr, target):
    """
    :param: arr - input array
    :param: target - integer element
    return: int - last index of target in arr
    """
    return last_index_recusion(arr, target, len(arr)-1)

def last_index_recusion(arr, target, index):
    # base case
    if index < 0:
        return -1
    
    # check to see if target has been found
    if arr[index] == target:
        return index
    
    # else make a recursive call to the rest of the array
    return last_index_recusion(arr, target, index-1)

  
# Test cases
def test_function(test_case):
    arr = test_case[0]
    target = test_case[1]
    solution = test_case[2]
    output = last_index(arr, target)
    if output == solution:
        print("Pass")
    else:
        print("FAIL: Expected", solution, ", but you've got:", output)

# case 1
arr = [1, 2, 5, 5, 4]
target = 5
solution = 3

test_case = [arr, target, solution]
test_function(test_case)        
 
