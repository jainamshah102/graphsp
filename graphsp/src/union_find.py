class UnionFind:
    def __init__(self, n):
        self.__n = n
        self.__parent = [node for node in range(self.__n)]

    def find(self, node):
        if (self.__parent[node] == node):
            return node
        self.__parent[node] = self.find(self.__parent[node])
        return self.__parent[node]

    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if (parent1 != parent2):
            self.__parent[parent1] = parent2
            return True

        return False
