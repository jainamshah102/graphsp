from collections import deque
import heapq

from graph import Graph
from union_find import UnionFind


class DFS:
    def __init__(self, n, graph):
        self.__n = n
        self.__graph = graph

    def dfs(self, start_node):
        visited = [False for _ in range(self.__n)]

        return self.__dfs_helper(start_node, visited)

    def __dfs_helper(self, node, visited):
        if (visited[node]):
            return []

        visited[node] = True
        result = [node]

        for neighbour, dist in self.__graph.get_neighbours(node):
            result += self.__dfs_helper(neighbour, visited)

        return result


class BFS:
    def __init__(self, n, graph):
        self.__n = n
        self.__graph = graph

    def bfs(self, start_node):
        visited = [False for _ in range(self.__n)]

        queue = deque([start_node])
        visited[start_node] = True

        result = []

        while queue:
            node = queue.popleft()

            result.append(node)

            for neighbour, distance in self.__graph.get_neighbours(node):
                if (visited[neighbour]):
                    continue

                visited[neighbour] = True
                queue.append(neighbour)

        return result


class Dijkstra:
    def __init__(self, n,  graph):
        self.__n = n
        self.__graph = graph

    def dijkstra(self, source):
        priority_queue = [(0, source)]
        distance = {node: float('inf') for node in range(self.__n)}
        distance[source] = 0

        while priority_queue:
            dist, node = heapq.heappop(priority_queue)

            for neighbour, weight in self.__graph.get_neighbours(node):
                if (distance[neighbour] > dist + weight):
                    distance[neighbour] = dist + weight
                    heapq.heappush(
                        priority_queue, (distance[neighbour], neighbour))

        return distance


class BellmanFord:
    def __init__(self, n, graph):
        self.__n = n
        self.__graph = graph

    def bellman_ford(self, source):
        distance = {node: float('inf') for node in range(self.__n)}
        edges = self.__graph.get_edges()

        distance[source] = 0

        for _ in range(self.__n - 1):
            for node, neighbour, weight in edges:
                if (distance[node] != float('inf') and distance[node] + weight < distance[neighbour]):
                    distance[neighbour] = distance[node] + weight

        for node, neighbour, weight in edges:
            if (distance[node] != float('inf') and distance[node] + weight < distance[neighbour]):
                return -1

        return distance


class FloydWarshall:
    def __init__(self, n, graph):
        self.__matrix = [[float('inf') for _ in range(n)] for _ in range(n)]
        self.__n = n
        for node in range(n):
            for neighbour, dist in graph.get_neighbours(node):
                self.__matrix[node][neighbour] = dist

    def floyd_warshall(self):
        matrix = [[self.__matrix[i][j]
                   for i in range(self.__n)] for j in range(self.__n)]

        for k in range(self.__n):
            for i in range(self.__n):
                for j in range(self.__n):
                    if (i == j):
                        continue
                    matrix[i][j] = min(
                        matrix[i][j], matrix[i][k] + matrix[k][j])

        return matrix


class TopoSorting:
    def __init__(self, n, graph):
        self.__n = n
        self.__graph = graph

    def topo_sorting(self):
        result = []
        in_edge = [0 for _ in range(self.__n)]

        for node in range(self.__n):
            for neighbour, dist in self.__graph.get_neighbours(node):
                in_edge[neighbour] += 1

        queue = deque([])

        for node in range(self.__n):
            if (in_edge[node] == 0):
                queue.append(node)

        while queue:
            node = queue.popleft()

            result.append(node)

            for neighbour, dist in self.__graph.get_neighbours(node):
                in_edge[neighbour] -= 1

                if (in_edge[neighbour] == 0):
                    result.append(neighbour)

        return result


class Prim:
    def __init__(self, n, graph):
        self.__n = n
        self.__graph = graph

    def prim(self):
        parent = [i for i in range(self.__n)]
        visited = set()

        total = 0
        parent[0] = -1
        priority_queue = [(0, 0, -1)]

        while priority_queue:
            cost, node, pr = heapq.heappop(priority_queue)

            if (node in visited):
                continue

            total += cost
            parent[pr] = node
            visited.add(node)

            for neighbour, dist in self.__graph.get_neighbours(node):
                if (neighbour in visited):
                    continue

                heapq.heappush(priority_queue, (dist, neighbour, node))

        return total, parent


class Kruskal:
    def __init__(self, n, graph):
        self.__n = n
        self.__graph = graph

    def kruskal(self):
        total = 0

        edges = self.__graph.get_edges()
        edges.sort(key=lambda x: x[2])
        uf = UnionFind(self.__n)

        for source, dest, weight in edges:
            if (uf.union(source, dest)):
                total += weight

        return total


class Kosaraju:
    def __init__(self, n, graph):
        self.__n = n
        self.__graph = graph

    def kosaraju(self):
        dfs = DFS(self.__n, self.__graph)

        if (len(dfs.dfs(0)) != self.__n):
            return False

        dfs = DFS(self.__n, self.__graph.reversed_graph())

        if (len(dfs.dfs(0)) != self.__n):
            return False

        return True
