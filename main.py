import heapq

def dijkstra(graph, start):
    """
    Implements Dijkstra's algorithm to find the shortest paths from the start node.

    :param graph: Dictionary representing the graph as adjacency list
                  {node: [(neighbor, weight), ...]}
    :param start: The starting node
    :return: Dictionary of shortest distances from start to each node
    """
    # Priority queue to manage the exploration of nodes
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))  # (distance, node)

    # Dictionary to store the shortest distances
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip processing if the distance is not optimal anymore
        if current_distance > shortest_distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If a shorter path is found, update and push to the queue
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_distances


# Example Usage:
if __name__ == "__main__":
    # Graph represented as an adjacency list
    # Format: node -> [(neighbor, weight), ...]
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 6)],
        'C': [('A', 4), ('B', 2), ('D', 3)],
        'D': [('B', 6), ('C', 3)]
    }

    start_node = 'A'
    shortest_paths = dijkstra(graph, start_node)
    print(f"Shortest paths from {start_node}: {shortest_paths}")
