import itertools
import math

def calculate_distance(points):
    """Вычисляет общее расстояние пути"""
    total_distance = 0
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        total_distance += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return total_distance

def solve_tsp(points):
    """Решает задачу коммивояжёра полным перебором"""
    if len(points) < 2:
        return points, 0
    
    # Генерируем все возможные перестановки точек
    permutations = list(itertools.permutations(points))
    
    best_path = None
    best_distance = float('inf')
    
    for path in permutations:
        distance = calculate_distance(path)
        if distance < best_distance:
            best_distance = distance
            best_path = path
    
    return list(best_path), best_distance

if __name__ == "__main__":
    # Пример использования
    points = [(0, 0), (1, 2), (3, 1), (2, 3)]
    best_path, distance = solve_tsp(points)
    
    print("Лучший путь:", best_path)
    print("Расстояние:", distance)