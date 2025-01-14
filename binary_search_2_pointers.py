import time

"""
Author: Yair Friedenson
All rights reserved ©
This code is protected under copyright law. 
No part of this code may be copied, distributed, or used without explicit permission
from the author.
"""


def measure_execution_time(func, *args, **kwargs):
    repetitions = 1000  # Number of repetitions to average the execution time
    total_time = 0
    for _ in range(repetitions):
        start_time = time.perf_counter()  # Use perf_counter for higher precision
        func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time += (end_time - start_time)
    execution_time = total_time / repetitions
    return execution_time


def find_issue_binary_search_with_two_pointers(ls1, start=0, end=None):
    """
    Finds the first index where the list stops being in ascending order using binary search.
    Uses two mid-pointers for clarity and accuracy.
    """
    if len(ls1) < 2:
        return None

    if end is None:
        end = len(ls1) - 1

    # Base case: when start and end converge
    if start >= end:
        return None

    mid_left = (start + end) // 2
    mid_right = mid_left + 1

    # Check if the issue is at mid_left
    if mid_left < len(ls1) - 1 and ls1[mid_left] > ls1[mid_right]:
        return mid_left

    # Check if the issue is at mid_left - 1 (covers cases where the issue lies just before mid_left)
    if mid_left > 0 and ls1[mid_left - 1] > ls1[mid_left]:
        return mid_left - 1

    # If left half might contain the issue
    if start < mid_left and ls1[start] > ls1[start + 1]:
        return find_issue_binary_search_with_two_pointers(ls1, start, mid_left - 1)

    # Otherwise, search in the right half
    return find_issue_binary_search_with_two_pointers(ls1, mid_right, end)


def find_issue_with_iterations(ls1):
    """
    Wrapper function to count iterations during binary search.
    Returns the result and total iterations.
    """
    iterations = 0

    def helper(ls1, start=0, end=None):
        nonlocal iterations
        iterations += 1

        if len(ls1) < 2:
            return None

        if end is None:
            end = len(ls1) - 1

        if start >= end:
            return None

        mid_left = (start + end) // 2
        mid_right = mid_left + 1

        if mid_left < len(ls1) - 1 and ls1[mid_left] > ls1[mid_right]:
            return mid_left

        if mid_left > 0 and ls1[mid_left - 1] > ls1[mid_left]:
            return mid_left - 1

        if start < mid_left and ls1[start] > ls1[start + 1]:
            return helper(ls1, start, mid_left - 1)

        return helper(ls1, mid_right, end)

    result = helper(ls1)
    return result, iterations


def main():
    my_list2 = [1, 2, 4, 1]
    my_list3 = [1, 2, 3, 4, 5, 6, 8, 1]
    my_list4 = [1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 13, 15, 16, 18, 24, 1]
    my_list5 = [x for x in range(1, 32)] + [1]
    my_list6 = [x for x in range(1, 64)] + [1]
    my_list7 = [x for x in range(1, 128)] + [1]

    test_dict = {"my_list2": my_list2, "my_list3": my_list3, "my_list4": my_list4, "my_list5": my_list5,
                 "my_list6": my_list6, "my_list7": my_list7}

    for list_name, test_list in test_dict.items():
        execution_time = measure_execution_time(find_issue_binary_search_with_two_pointers, test_list)
        result, iterations = find_issue_with_iterations(test_list)
        print(
            f"list length {len(test_list)} (Iterations: {iterations}): Result = {result}, Average Execution Time = {execution_time:,.8f} seconds")


if __name__ == "__main__":
    main()

# list length 4 (Iterations: 2): Result = 2, Average Execution Time = 0.00000067 seconds
# list length 8 (Iterations: 3): Result = 6, Average Execution Time = 0.00000094 seconds
# list length 16 (Iterations: 4): Result = 14, Average Execution Time = 0.00000118 seconds
# list length 32 (Iterations: 5): Result = 30, Average Execution Time = 0.00000155 seconds
# list length 64 (Iterations: 6): Result = 62, Average Execution Time = 0.00000174 seconds
# list length 128 (Iterations: 7): Result = 126, Average Execution Time = 0.00000190 seconds
