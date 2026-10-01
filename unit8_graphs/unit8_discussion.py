"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    if start not in graph:
        return []

    visited = {start}

    queue = deque([start])
    order = []

    while queue:

        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)

                queue.append(neighbor)

def print_graph(graph):

    for node, neighbors in graph.items():
        print(f"  {node:<6} -> {', '.join(neighbors) if neighbors else '(no connections)'}")

def add_edge(graph,a,b):

    graph.setdefualt(a, [])
    graph.setdefualt(b, [])
    if b not in graph[a]:
        graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    graph = {
        "Alice": ["Bob", "Carol"],
        "Bob":   ["Alice", "Dave", "Eve"],
        "Carol": ["Alice", "Eve"],
        "Dave":  ["Bob", "Frank"],
        "Eve":   ["Bob", "Carol", "Frank"],
        "Frank": ["Dave", "Eve"],
    }
    print("\n=== GRAPH STRUCTURE ===")
    print_graph(graph)

    # ===============================
    # BFS TRAVERSAL
    # ===============================
    start = "Alice"
    print("\n=== BFS TRAVERSAL ===")
    print(f"Starting at: {start}")
    print(f"Visit order: {' -> '.join(bfs(graph, start))}")
    # Explanation of the levels from Alice:
    #   Level 0: Alice
    #   Level 1: Bob, Carol      (Alice's direct friends)
    #   Level 2: Dave, Eve       (friends of Bob/Carol)
    #   Level 3: Frank           (friend of Dave/Eve)
    # BFS finishes each level before moving on to the next one.
    print("Levels: Alice | Bob, Carol | Dave, Eve | Frank")

    # Add a new node and edges, then traverse again.
    print("\n--- After adding Grace (friends with Carol and Frank) ---")
    add_edge(graph, "Grace", "Carol")
    add_edge(graph, "Grace", "Frank")
    print_graph(graph)
    print(f"Visit order: {' -> '.join(bfs(graph, start))}")
    # Grace is 2 steps from Alice (via Carol), so she now appears in
    # level 2 alongside Dave and Eve, before Frank at level 3.

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASE TESTS ===")

    # 1. Starting from a different node
    print("\n1) Different start node (Frank):")
    print(f"   {' -> '.join(bfs(graph, 'Frank'))}")
    print("   The order changes because 'distance' is measured from Frank now.")

    # 2. Disconnected graph
    disconnected = {
        "A": ["B"],
        "B": ["A"],
        "C": ["D"],
        "D": ["C"],
    }
    print("\n2) Disconnected graph (A-B and C-D are separate groups):")
    print(f"   BFS from A: {bfs(disconnected, 'A')}")
    print("   Only A and B are reached. BFS can only follow existing edges,")
    print("   so C and D are never visited.")

    # 3. Missing start node
    print("\n3) Start node not in graph ('Zed'):")
    print(f"   {bfs(graph, 'Zed')}")
    print("   Returns an empty list instead of raising a KeyError.")

    # 4. Single-node graph
    print("\n4) Graph with a single node:")
    print(f"   {bfs({'Solo': []}, 'Solo')}")
    print("   Only the start node is visited since it has no neighbors.")

    # 5. Empty graph
    print("\n5) Empty graph:")
    print(f"   {bfs({}, 'Alice')}")
    print("   No nodes exist, so the result is an empty list.")


if __name__ == "__main__":
    main()
