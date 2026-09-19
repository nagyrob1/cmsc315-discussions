"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""
from unittest import result


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    age_diction= {}
    # 2. Add at least 5 key-value pairs.
    age_diction["bob"] = 96
    age_diction["sam"] = 23
    age_diction["sally"] = 40
    age_diction["bill"] = 62
    age_diction["paul"] = 18
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    #Python uses a hash funtion to turn every key into a number
    # 4. Display the contents of the dictionary.
    print("this is my dictionary: ",age_diction)

    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    print("bobs age: ", {age_diction['bob']})
    print("pauls age: ", {age_diction['paul']})
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.
    # Python hashes the key a second time and jumps straight to the location of the key
    # It confirms that the key matches the value rather than going through the dictionary again
    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    print("before bobs age gets updated: ", {age_diction['bob']})
    age_diction["bob"] = 59
    print("after bobs age gets updated: ", {age_diction['bob']})
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.
    # Python finds the existing key value, then teh slot and replaces the old key with the new
    # No duplicate is created because the keys need to be unique

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    print("before bobs key is deleted: " , age_diction)
    del age_diction["bob"]
    print("After bobs key is deleted: ", age_diction)
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.
    # Python hashes the key, finds the slot, and removes the entry

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.
    # Looking up a missing key
    print("trying to find a missing key: ", {age_diction["zach"]})
    # we get a key error for this lookup example
    result = age_diction.get("zach")
    print(result)
    #we get "none here" for this lookup example

    print("Deleting a missing key safely")
    deleted = age_diction.pop("zach", "not found")
    print(" removed key: ", deleted)
    print(age_diction)


    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")



if __name__ == "__main__":
    main()