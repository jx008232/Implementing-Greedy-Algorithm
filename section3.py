"""
     0   NaN   NaN     8    19     8     8
    14     0    11   NaN   NaN   NaN     1
   NaN    11     0   NaN    14    26    39
     8   NaN   NaN     0   NaN    24     2
   NaN    10   NaN   NaN     0    40     8
     8   NaN    26   NaN   NaN     0    18
     8     1    39     2     8    18     0
"""

import heapq


def prim_mst(graph):
    mst = []
    visited = set()
    pq = [(0, 'A')]

    while pq:
        (weight, node) = heapq.heappop(pq)
        if node not in visited:
            visited.add(node)
            mst.append((node, weight))
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (weight, neighbor))

    return mst


graph = {
    'A': [('D', 8), ('E', 19), ('F', 8), ('G', 8)],
    'B': [('A', 14), ('C', 11), ('G', 1)],
    'C': [('B', 11), ('E', 14), ('F', 26), ('G', 39)],
    'D': [('A', 8), ('F', 24), ('G', 2)],
    'E': [('B', 10), ('F', 40), ('G', 8)],
    'F': [('A', 8), ('C', 26), ('G', 18)],
    'G': [('A', 8), ('B', 1), ('C', 39), ('D', 2), ('E', 8), ('F', 18)]
}

mst = prim_mst(graph)

for edge in mst:
    print(edge)

total_weight = sum(weight for n, weight in mst)
print("Total weight of the MST:", total_weight)
