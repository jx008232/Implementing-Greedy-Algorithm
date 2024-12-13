"""
     0   NaN   NaN     8    19     8     
    14     0    11   NaN   NaN   NaN     
   NaN    11     0   NaN    14    26    
     8   NaN   NaN     0   NaN    24     
   NaN    10   NaN   NaN     0    40     
     8   NaN    26   NaN   NaN     0    
"""
graph = {
    'A': [('D', 8), ('E', 19), ('F', 8)],
    'B': [('A', 14), ('C', 11)],
    'C': [('B', 11), ('E', 14), ('F', 26)],
    'D': [('A', 8), ('F', 24)],
    'E': [('B', 10), ('F', 40)],
    'F': [('A', 8), ('C', 26)],
}

import heapq


def dijkstra(graph, source):
    distances = {node: float('infinity') for node in graph}
    distances[source] = 0
    pq = [(0, source)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


source_node = input("please select the source node that you want: ").upper()
shortest_distances = dijkstra(graph, source_node)
print(shortest_distances)
