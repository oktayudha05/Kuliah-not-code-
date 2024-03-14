import heapq

def dijkstra(graph, start, end):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    previous = {node: None for node in graph}
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_node == end:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = previous[current_node]
            return distances[end], list(reversed(path))
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))
    
    return float('infinity'), []

# Contoh penggunaan dengan grafik sederhana
graph = {
    'A': {'B': 4, 'E': 9, 'F': 13},
    'B': {'F': 15, 'C': 5},
    'C': {'D': 7, 'F': 12},
    'D': {'F': 7, 'G': 8},
    'E': {'F': 10, 'H': 7},
    'F': {'H': 9, 'K': 20, 'J': 13},
    'G': {'J': 15, 'F': 3},
    'H': {'K': 18, 'I': 8},
    'I': {'K': 13,},
    'J': {'K': 13},
    'K': {},
}

start_node = input("Masukkan titik awal: ")
end_node = input("Masukkan titik tujuan: ")

shortest_distance, shortest_path = dijkstra(graph, start_node, end_node)

if shortest_distance != float('infinity'):
    print(f"Jarak terpendek dari {start_node} ke {end_node} adalah {shortest_distance}")
    print(f"Titik yang dilalui: {' -> '.join(shortest_path)}")
else:
    print(f"Tidak ada jalur dari {start_node} ke {end_node}")
