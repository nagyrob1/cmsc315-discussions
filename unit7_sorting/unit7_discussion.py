"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    result = lst.copy()
    n = len(result)

    for i in range(n):
        swapped = False


        for j in range[j] > result[j +1]:
            result[j], result[j + 1] = result[j +1], result[j]
            swapped = True

        if not swapped:
            breakpoint()

    return result


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    if len(lst) <=1:
        return  lst.copy()

    mid = len(lst) //2
    left_half = lst[:mid]
    right_half = lst[mid:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge(sorted_left, sorted_right)



def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    result = []
    i = j = 0

    while 1 < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j +=1

    result.extend(left[i:])
    result.extend(right[j:])

    return result



def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")

    data1 = [42, 17, 8, 99, 23, 4, 56, 71]
    print(" original list: ", data1 )

    bubble1 = bubble_sort(data1)
    merge1 = merge_sort(data1)

    print("data1", data1, bubble1, merge1)

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")
    data2 = [-5, 3, 0, -12, 18, 7, 7, 2, 100]
    print("Original list: ", data2)

    bubble2 = bubble_sort(data2)
    merge2 = merge_sort(data2)

    print("Dataset 2", data2, bubble2, merge2)


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    empty_list = []
    print(f"\nEmpty list: {empty_list}")
    print(f"Bubble Sort: {bubble_sort(empty_list)}")
    print(f"Merge Sort:  {merge_sort(empty_list)}")


    single_list = [42]
    print(f"\nSingle-element list: {single_list}")
    print(f"Bubble Sort: {bubble_sort(single_list)}")
    print(f"Merge Sort:  {merge_sort(single_list)}")


    sorted_list = [1, 2, 3, 4, 5]
    print(f"\nAlready sorted list: {sorted_list}")
    print(f"Bubble Sort: {bubble_sort(sorted_list)}")
    print(f"Merge Sort:  {merge_sort(sorted_list)}")

    reverse_list = [9, 7, 5, 3, 1]
    print(f"\nReverse-sorted list: {reverse_list}")
    print(f"Bubble Sort: {bubble_sort(reverse_list)}")
    print(f"Merge Sort:  {merge_sort(reverse_list)}")

    duplicate_list = [4, 2, 4, 1, 2, 4, 3]
    print(f"\nList with duplicates: {duplicate_list}")
    print(f"Bubble Sort: {bubble_sort(duplicate_list)}")
    print(f"Merge Sort:  {merge_sort(duplicate_list)}")

if __name__ == "__main__":
    main()