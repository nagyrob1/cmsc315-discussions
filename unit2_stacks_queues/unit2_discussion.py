"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items= []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            raise IndexError("cannot pop from an empty stack.")
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if self.is_empty():
            raise IndexError("cannot peek from an empty stack.")
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            raise IndexError("cannot dequeue from an empty queue.")
        return  self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if self.is_empty():
            raise IndexError("Cannot view the from of an empty queue.")
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # STACK DEMO
    # ===============================
    print("\n=== STACK DEMO ===")

    stack = Stack()

    print("Adding 4 values to the stack...")
    for value in ["A", "B", "C", "D"]:
        stack.push(value)
        print(f"  Pushed: {value}")

    print(f"\nThe top of the stack is: {stack.peek()}")
    print("The stack follows LIFO: Last In, First Out.")

    print("\nRemoving values from the stack:")
    while not stack.is_empty():
        print(f"  Popped: {stack.pop()}")

    print(f"Is the stack empty? {stack.is_empty()}")

    # Test popping from an empty stack.
    print("\nTrying to pop from an empty stack:")
    try:
        stack.pop()
    except IndexError as error:
        print(f"  Error handled: {error}")

    # Test peeking at an empty stack.
    print("\nTrying to peek at an empty stack:")
    try:
        stack.peek()
    except IndexError as error:
        print(f"  Error handled: {error}")

    # Single-item stack edge case.
    print("\nSingle-item stack test:")
    single_stack = Stack()
    single_stack.push("Only Item")
    print(f"  Added: {single_stack.peek()}")
    removed = single_stack.pop()
    print(f"  Removed: {removed}")
    print(f"  Is the single-item stack empty? {single_stack.is_empty()}")

    # ===============================
    # QUEUE DEMO
    # ===============================
    print("\n=== QUEUE DEMO ===")

    queue = Queue()

    print("Adding 4 values to the queue...")
    for value in ["A", "B", "C", "D"]:
        queue.enqueue(value)
        print(f"  Enqueued: {value}")

    print(f"\nThe front of the queue is: {queue.front()}")
    print("The queue follows FIFO: First In, First Out.")

    print("\nRemoving values from the queue:")
    while not queue.is_empty():
        print(f"  Dequeued: {queue.dequeue()}")

    print(f"Is the queue empty? {queue.is_empty()}")

    # Test dequeuing from an empty queue.
    print("\nTrying to dequeue from an empty queue:")
    try:
        queue.dequeue()
    except IndexError as error:
        print(f"  Error handled: {error}")

    # Test viewing the front of an empty queue.
    print("\nTrying to view the front of an empty queue:")
    try:
        queue.front()
    except IndexError as error:
        print(f"  Error handled: {error}")

    # Single-item queue edge case.
    print("\nSingle-item queue test:")
    single_queue = Queue()
    single_queue.enqueue("Only Item")
    print(f"  Added: {single_queue.front()}")
    removed = single_queue.dequeue()
    print(f"  Removed: {removed}")
    print(f"  Is the single-item queue empty? {single_queue.is_empty()}")


if __name__ == "__main__":
    main()