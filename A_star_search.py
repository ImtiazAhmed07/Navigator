import csv
import math
import heapq

# Load the datasets
def load_cities(file_path):
    cities = {}
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        print(f"Cities CSV headers: {headers}")  # Debugging line
        for row in reader:
            cities[row['City']] = (float(row['Latitude']), float(row['Longitude']))
    return cities

def load_distances(file_path):
    distances = {}
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        print(f"Distances CSV headers: {headers}")  # Debugging line
        for row in reader:
            if row['City1'] not in distances:
                distances[row['City1']] = {}
            if row['City2'] not in distances:
                distances[row['City2']] = {}
            distances[row['City1']][row['City2']] = float(row['Distance'])
            distances[row['City2']][row['City1']] = float(row['Distance'])
    return distances

# Heuristic function: Euclidean distance
def heuristic(city1, city2, cities):
    lat1, lon1 = cities[city1]
    lat2, lon2 = cities[city2]
    return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)

# A* Algorithm
def a_star_search(start, goal, cities, distances):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, goal, cities), 0, start, []))
    closed_list = set()

    while open_list:
        _, cost, current_city, path = heapq.heappop(open_list)

        if current_city in closed_list:
            continue

        path = path + [current_city]

        if current_city == goal:
            return path, cost

        closed_list.add(current_city)

        for neighbor, distance in distances[current_city].items():
            if neighbor not in closed_list:
                new_cost = cost + distance
                heapq.heappush(open_list, (new_cost + heuristic(neighbor, goal, cities), new_cost, neighbor, path))

    return None, float('inf')

# File paths
cities_file_path = r'C:\Users\Imtiaz Ahmed\OneDrive\Desktop\Astar Search\Pakistn_cities.csv'
distances_file_path = r'C:\Users\Imtiaz Ahmed\OneDrive\Desktop\Astar Search\Pakistan_distances.csv'

# Load data
cities = load_cities(cities_file_path)
distances = load_distances(distances_file_path)

# Example usage
start_city = 'Islamabad'
goal_city = 'Karachi'
path, cost = a_star_search(start_city, goal_city, cities, distances)

print(f"Path from {start_city} to {goal_city}: {path}")
print(f"Total cost: {cost}")