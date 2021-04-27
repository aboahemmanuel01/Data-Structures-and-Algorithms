'''
Problem Definition

Given an integer array, this algorithm finds and return all the subsets of the array. 
The order of subsets in the output array is not important and hence wasn't considered. 
However, the order of elements in a particular subset remains the same as in the input array.

For example:

arr = [9, 9]

output = [[],
          [9],
          [9],
          [9, 9]]
          
'''

def subsets(arr):
    """
    :param: arr - input integer array
    Return - list of lists (two dimensional array) where each list represents a subset
    """
    return return_subsets(arr, 0)


def return_subsets(arr, idx):
    
    # base case
    if idx >= len(arr):
        return [[]]
    
    # recursion      
    initial_subset = return_subsets(arr, idx+1)
    
    results = []
    # append existing subsets
    for num in initial_subset:
        results.append(num)
        print(results)
    
    for num in initial_subset:
        curr = []
        curr.append(arr[idx])
        curr.extend(num)
        results.append(curr)
        
    return results


# Test cases
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = subsets(arr)
        
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")    


arr = [9]
solution = [[], [9]]

test_case = [arr, solution]
test_function(test_case)

'''
# Other test cases
# case 2
arr = [5, 7]
solution = [[], [7], [5], [5, 7]]
test_case = [arr, solution]
test_function(test_case)

# case 3
arr = [9, 12, 15]
solution = [[], [15], [12], [12, 15], [9], [9, 15], [9, 12], [9, 12, 15]]

test_case = [arr, solution]
test_function(test_case)
