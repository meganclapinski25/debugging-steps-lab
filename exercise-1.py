"""
Exercise 1
"""

# PART 1: Gather Information
#Traceback (most recent call last):
#   File "/Users/meganclapinski/Documents/GitHub/debugging-steps-lab/SPD-2.3-Debugging-Steps-Lab-main 2/exercise-1.py", line 31, in <module>
#     answer = find_largest_diff([5, 3, 1, 2, 6, 4])
#   File "/Users/meganclapinski/Documents/GitHub/debugging-steps-lab/SPD-2.3-Debugging-Steps-Lab-main 2/exercise-1.py", line 23, in find_largest_diff
#     diff = abs(list_of_nums[i] - list_of_nums[i+1])
#                                  ~~~~~~~~~~~~^^^^^
# IndexError: list index out of range

# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
## - Expecgted output is 4 , not actual output because of the error 
# - What error message (if any) is there?
## - IndexError: list index out of range 
# - What line number is causing the error?
## - Line 31 (before typing)
# - What can you deduce about the cause of the error?
## - If I were to equal the last index of the list, i+1 would not be able to return anything because it has gone past the amount of indexis in the list
## - 


# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!

## - My assumptions are the the loop compares each pair of consective numbers (0,1) (1,2) 
## - the enginneer thought using in range would be significant enough to make sure there were no errors


def find_largest_diff(list_of_nums):
    """Find the largest difference between *consecutive* numbers in a list."""
    largest_diff = 0
    for i in range(len(list_of_nums)):
        diff = abs(list_of_nums[i] - list_of_nums[i+1]) 
        if diff > largest_diff:
            largest_diff = diff

    return largest_diff

if __name__ == '__main__':
    print('### Problem 1 ###')
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])

    # This should print 4, as the largest diff between consecutive numbers is between 2 and 6
    print(answer)