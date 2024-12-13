"""
     0   NaN   NaN     8    19     8     8
    14     0    11   NaN   NaN   NaN     1
   NaN    11     0   NaN    14    26    39
     8   NaN   NaN     0   NaN    24     2
   NaN    10   NaN   NaN     0    40     8
     8   NaN    26   NaN   NaN     0    18
     8     1    39     2     8    18     0
"""

graph_d = {
    'A': [('D', 8), ('E', 19), ('F', 8), ('G', 8)],
    'B': [('A', 14), ('C', 11), ('G', 1)],
    'C': [('B', 11), ('E', 14), ('F', 26), ('G', 39)],
    'D': [('A', 8), ('F', 24), ('G', 2)],
    'E': [('B', 10), ('F', 40), ('G', 8)],
    'F': [('A', 8), ('C', 26), ('G', 18)],
    'G': [('A', 8), ('B', 1), ('C', 39), ('D', 2), ('E', 8), ('F', 18)]
}


def calculate_travel_times(graph_d):
    graph_t = {}
    for node, neighbors in graph_d.items():
        graph_t[node] = []
        for neighbor, distance in neighbors:
            if distance < 5:
                speed = 5
            elif distance < 10:
                speed = 10
            else:
                speed = 30
            time = distance / speed
            graph_t[node].append((neighbor, time))
    return graph_t


graph_t = calculate_travel_times(graph_d)
print(graph_t)

import heapq


def dijkstra(graph_t, source):
    distances = {node: float('infinity') for node in graph_t}
    distances[source] = 0
    pq = [(0, source)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph_t[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


source_node = input("please select the source node that you want: ").upper()
shortest_distances = dijkstra(graph_t, source_node)
print(shortest_distances)


