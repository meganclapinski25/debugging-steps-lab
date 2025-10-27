"""
Exercise 4
"""

# PART 1: Gather Information
# Traceback (most recent call last):
#   File "/Users/meganclapinski/Documents/GitHub/debugging-steps-lab/SPD-2.3-Debugging-Steps-Lab-main 2/exercise-4.py", line 40, in <module>
#     answer = binary_search([1, 2, 4, 5, 7], 7)
#   File "/Users/meganclapinski/Documents/GitHub/debugging-steps-lab/SPD-2.3-Debugging-Steps-Lab-main 2/exercise-4.py", line 36, in binary_search
#     return binary_search(arr, element, mid, high)
#   File "/Users/meganclapinski/Documents/GitHub/debugging-steps-lab/SPD-2.3-Debugging-Steps-Lab-main 2/exercise-4.py", line 36, in binary_search
#     return binary_search(arr, element, mid, high)
#   File "/Users/meganclapinski/Documents/GitHub/debugging-steps-lab/SPD-2.3-Debugging-Steps-Lab-main 2/exercise-4.py", line 36, in binary_search
#     return binary_search(arr, element, mid, high)
#   [Previous line repeated 995 more times]
#   File "/Users/meganclapinski/Documents/GitHub/debugging-steps-lab/SPD-2.3-Debugging-Steps-Lab-main 2/exercise-4.py", line 21, in binary_search
#     if high == None:
# RecursionError: maximum recursion depth exceeded in comparison

# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
## - expected output would be 4, the actual output is an Error in recursion 
# - What error message (if any) is there?
## -  RecursionError: maximum recursion depth exceeded in comparison
# - What line number is causing the error?
## - 49 and 52
# - What can you deduce about the cause of the error?
## - The call reuses "mid" over and over again, so the loop doesn't go from low, mid and mid, high. 
## - 

# PART 2: State Assumptions
#  -- The author assumed that the use of low, mid and mid, high would be the correct window in search for the elements 
#  -- 
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.

def binary_search(arr, element, low=0, high=None):
    if high == None:
        high = len(arr) - 1

    if high < low:
        return -1

    mid = (high + low) // 2

    if arr[mid] == element: 
        return mid

    elif arr[mid] > element:
        return binary_search(arr, element, low, mid)

    else: 
        return binary_search(arr, element, mid, high)


if __name__ == '__main__':
    answer = binary_search([1, 2, 4, 5, 7], 7)
    print(answer)