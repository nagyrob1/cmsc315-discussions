"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""

def linear_search(lst, target):
    """
    Implement a linear search algorithm.

    Linear search checks each item from beginning to end.
    Since we may have to check every item in the list,
    the time complexity is O(n).
    """
    for i in range(len(lst)):
        # Check if the current item is the target
        if lst[i] == target:
            return i

    # Target was not found
    return -1


def binary_search(lst, target):
    """
    Implement a binary search algorithm.

    The list must already be sorted.

    Binary search repeatedly cuts the search area in half.
    Because the search space is divided by 2 each time,
    the time complexity is O(log n).
    """

    # Set the starting and ending positions
    left = 0
    right = len(lst) - 1

    while left <= right:
        # Find the middle position
        middle = (left + right) // 2

        # If the middle value is the target, return its index
        if lst[middle] == target:
            return middle

        # If the target is greater than the middle value,
        # ignore the left half of the list.
        elif lst[middle] < target:
            left = middle + 1

        # If the target is smaller than the middle value,
        # ignore the right half of the list.
        else:
            right = middle - 1

    # Target was not found
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # SMALL DATASET
    # ===============================

    print("\n=== SMALL DATASET TEST ===")

    # Create a small sorted dataset
    small_list = [1, 3, 5, 7, 9, 11, 13, 15]

    print("Dataset:", small_list)

    # Search for a value that exists
    target = 7

    linear_result = linear_search(small_list, target)
    binary_result = binary_search(small_list, target)

    print("\nSearching for:", target)
    print("Linear search index:", linear_result)
    print("Binary search index:", binary_result)

    # Search for a value that does not exist
    target = 10

    linear_result = linear_search(small_list, target)
    binary_result = binary_search(small_list, target)

    print("\nSearching for:", target)
    print("Linear search index:", linear_result)
    print("Binary search index:", binary_result)

    # -1 means that the value was not found.


    # ===============================
    # LARGE DATASET
    # ===============================

    print("\n=== LARGE DATASET TEST ===")

    # Create a sorted dataset containing 1,000,000 numbers
    large_list = list(range(1, 1000001))

    print("Dataset contains", len(large_list), "values.")

    # Search for a value near the end of the list.
    # This is a good example because linear search
    # will have to check many values.
    target = 999999

    linear_result = linear_search(large_list, target)
    binary_result = binary_search(large_list, target)

    print("\nSearching for:", target)
    print("Linear search index:", linear_result)
    print("Binary search index:", binary_result)

    # Linear search has O(n) time complexity, so it may
    # need to check almost every item.
    #
    # Binary search has O(log n) time complexity because
    # it cuts the search area in half during every iteration.
    #
    # Therefore, binary search becomes much more efficient
    # as the dataset gets larger.


    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: Empty list
    empty_list = []

    print("\n1. Empty list:")
    print("Linear search:", linear_search(empty_list, 5))
    print("Binary search:", binary_search(empty_list, 5))

    # Both return -1 because there is nothing to search.


    # Edge case 2: Single-element list
    single_list = [10]

    print("\n2. Single-element list:")

    # Search for the value that exists
    print("Searching for 10:")
    print("Linear search:", linear_search(single_list, 10))
    print("Binary search:", binary_search(single_list, 10))

    # Search for a value that does not exist
    print("Searching for 5:")
    print("Linear search:", linear_search(single_list, 5))
    print("Binary search:", binary_search(single_list, 5))

    # The searches return 0 when the value is found
    # because the first and only element has index 0.
    # They return -1 when the value is not found.


if __name__ == "__main__":
    main()
