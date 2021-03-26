# This is an alternative solution to the add one problem in the directory.

# ### Problem Statement
# You are given a non-negative number in the form of list elements. For example, the number `123` would be provided as `arr = [1, 2, 3]`. Add one to the number and return the output in the form of a new list. 
# 
# **Example 1:**
# * `input = [1, 2, 3]`
# * `output = [1, 2, 4]`
# 
# 
# **Example 2:**
# * `input = [1, 2, 9]`
# * `output = [1, 3, 0]`
# 
# **Example 3:**
# * `input = [9, 9, 9]`
# * `output = [1, 0, 0, 0]`

'''
Logic:
First I converted the input array of integers into a list of string 
For example: arr = [1, 2, 3] is converted into string = ['1', '2', '3']
Afterwards, the i used the join method to remove the "," between the string
The string was converted into an intger and 1 was added, i.e. 123 + 1 = 124
Finally, the total value was converted into a array.

'''


def add_one(arr):
    '''
    This function adds  one to the array (number)
    and return the output in the form of a new list
    '''
    
    string_arr = [str(i) for i in arr]
    string_arr = "".join(string_arr)
    
    str_to_int = int(string_arr) + 1
    int_to_str = str(str_to_int)
    
    new_list = [int(x) for x in int_to_str]
    
    
    return new_list
  
  
