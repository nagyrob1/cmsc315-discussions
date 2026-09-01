"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""
from os import remove
from tracemalloc import take_snapshot
from unittest import result


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    lst.insert(index, value)
    return lst


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    if index < 0 or index >=len(lst):
        return None

    deleted = lst.pop(index)
    return deleted


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    for i in range (len(lst)):
        if lst[i] == value:
            return i

    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    tasks = ["task 1", "task 2", "task 3"]
    print("original task created: ", tasks)
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    insert_at(tasks, 0, "new task 1")
    print("tasks after inserting the beginning: ", tasks)
    #    - the middle
    middle = len(tasks) // 2
    insert_at(tasks,  middle, "middle task")
    print(" list after splitting in half and inserting task in middle ", tasks)

    #    - the end
    insert_at(tasks, len(tasks), "task at end")
    print("list after inserting task at end ", tasks)
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    delete = delete_at(tasks, 0)
    print("list after deleting first ", tasks)
    #    - the middle
    middle = len(tasks) // 2
    delete = delete_at(tasks, middle)
    print("list after deleting middle task ", tasks)
    #    - the end
    delete_at(tasks, len(tasks) - 1)
    print("results after deleting last taskin in the list")
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # searching for a task that exist
    value = tasks[0] if tasks else "task 1"
    results = search_value(tasks, value)
    print(f"{value} found here {results}")

    # searching for a task that doesn't exist
    missing = "task 45"
    results = search_value(tasks, missing)
    print(f"search for {missing}, result is {results}")

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # delete using an invalid index
    invalid = delete_at(tasks, 999)
    print(f"value after trying to delete index 999 {invalid}")

    # inserting into an empty list
    null_tasks = []
    insert_at(null_tasks, 0, "task 1")
    print("inserting into an empty list", null_tasks)

    # deleting from an empty list
    null_tasks2 = []
    result = delete_at(null_tasks2, 0)
    print("deleting from empty list ", null_tasks2)

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")



if __name__ == "__main__":
    main()