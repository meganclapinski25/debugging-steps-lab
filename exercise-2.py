"""
Exercise 2
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
## - Expected output would be False and True. THe acutal output was False and False 
# - What error message (if any) is there?
## - No Error Message 
# - What line number is causing the error?
## - Line 28  
# - What can you deduce about the cause of the error?
## - since the return statement is inside the for loop, it will really wont loop through all test cases. 
## If the first 3 numbers are not increasing by 1, it will assume the loop / list is done. 

# PART 2: State Assumptions
# The author thought the for loop would check every group of 3 elements in the list. 
# Thought the else statement would only be called at the end of list
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!

def contains_3_consecutive(list_of_nums):
    """Return True if the list contains 3 consecutive numbers each increasing by 1."""
    for i in range(len(list_of_nums) - 2):
        if (list_of_nums[i+1] == list_of_nums[i] + 1 and
            list_of_nums[i+2] == list_of_nums[i] + 2):
            return True
        else:
            return False

    return False

if __name__ == '__main__':
    print('### Problem 2 ###')
    answer1 = contains_3_consecutive([1, 2, 4])
    print(answer1) # should print False

    answer2 = contains_3_consecutive([4, 1, 2, 3])
    print(answer2) # should print True