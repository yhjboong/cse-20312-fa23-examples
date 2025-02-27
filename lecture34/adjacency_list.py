#!/usr/bin/env python3

''' adjacency_list.py

Represent graph as adjaceny list.
'''

from collections import defaultdict

import sys

# Types

AdjacencyList = dict[int, list[int]]

# Functions

def read_graph(stream) -> AdjacencyList:
    # Read number of vertices (n) and number of edges (m)
    try:
        n, m = map(int, stream.readline().split())
    except ValueError:
        return {}

    # Initialize empty adjacency list
    graph = defaultdict(list)

    # Read each edge and update adjacency list
    for _ in range(m):
        source, target = map(int, stream.readline().split())

        # Update both directions since graph is undirected
        graph[source].append(target)
        graph[target].append(source)

    return graph

# Main Execution

def main(stream=sys.stdin) -> None:
    graph = read_graph(stream)

    for vertex, neighbors in sorted(graph.items()):
        print(f'{vertex}: {sorted(neighbors)}')

if __name__ == '__main__':
    main()
