"""
Exercise 3
"""

# PART 1: Gather Information
# Traceback (most recent call last):
#   File "/Users/meganclapinski/Documents/GitHub/debugging-steps-lab/SPD-2.3-Debugging-Steps-Lab-main 2/exercise-3.py", line 34, in <module>
#     answer = insertion_sort([5, 2, 3, 1, 6])
#   File "/Users/meganclapinski/Documents/GitHub/debugging-steps-lab/SPD-2.3-Debugging-Steps-Lab-main 2/exercise-3.py", line 26, in insertion_sort
#     while key < arr[j] :
#                 ~~~^^^
# IndexError: list index out of range 
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?

# - What error message (if any) is there?
## - list index out of range 
# - What line number is causing the error?
## - line 32
# - What can you deduce about the cause of the error?
## - The error happens because the loop never stops when j moves past the first index (1). 

# PART 2: State Assumptions
# -- The author wanted j to stop once it reached the start of the list 
# -- The author thought maybe that negative indexes would led to it stopping instead of continuiing to go backwards 
# -- Thought that checking if j in array is more than the value of the key that it would be enough to prevent errors. 
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.

def insertion_sort(arr):
    """Performs an Insertion Sort on the array arr."""
    for i in range(1, len(arr)):
        key = arr[i] 

        j = i-1
        while key < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    print('### Problem 3 ###')
    answer = insertion_sort([5, 2, 3, 1, 6])
    print(answer)

