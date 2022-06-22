class Graph:
    def __init__(self, n, graph_type="undirected"):
        self.__n = n
        self.__graph_type = graph_type
        self.__graph = {node: [] for node in range(n)}

    def __str__(self):
        display = ""
        for node in range(self.__n):
            display += str(node) + "\n"

            for neighbour, dist in self.__graph[node]:
                display += "node: " + \
                    str(neighbour) + ", distance: " + str(dist) + "\n"

            display += "\n"
        return display

    def __cycle_detection(self, node, parent, visited, stack):
        visited[node] = True
        stack[node] = True

        for neighbour, dist in self.get_neighbours(node):
            if (self.__graph_type == "directed" and stack[neighbour]):
                return True

            if (visited[neighbour] == False and self.__cycle_detection(neighbour, node, visited, stack)):
                if (self.__graph_type == "undirected" and parent != neighbour):
                    return True
                elif(self.__graph_type == "directed"):
                    return True

        stack[node] = False

        return False

    def link(self, source, dest, weight=1):
        # Linking edges in the graph based on the type of the graph
        if (self.__graph_type == "directed"):
            self.__graph[source].append((dest, weight))

        if (self.__graph_type == "undirected"):
            self.__graph[source].append((dest, weight))
            self.__graph[dest].append((source, weight))

    def bulk_link(self, edges):
        # Adding multiple edges in the graph
        for source, dest, weight in edges:
            self.link(source, dest, weight)

    def unlink(self, source, dest):
        # Removing the link between nodes in the graph
        if (self.__graph_type in ("directed", "undirected")):
            for idx, node, weight in enumerate(self.__graph[source]):
                if (node == dest):
                    self.__graph[source].pop(idx)
                    break

        if (self.__graph_type == "undirected"):
            for idx, node, weight in enumerate(self.__graph[dest]):
                if (node == source):
                    self.__graph[dest].pop(idx)
                    break

    def bulk_unlink(self, edges):
        # Removing multiple edges in the graph
        for source, dest in edges:
            self.unlink(source, dest)

    def get_neighbours(self, node):
        # Returns all the neighbours of given node
        return self.__graph[node]

    def get_graph_type(self):
        # Returns graph type -> directed / undirected
        return self.__graph_type

    def detect_cycle(self):
        visited = [False for _ in range(self.__n)]
        stack = [False for _ in range(self.__n)]

        for node in range(self.__n):
            if (visited[node]):
                continue

            if (self.__cycle_detection(node, None, visited, stack)):
                return True
        return False

    def get_edges(self):
        edges = []
        for node in range(self.__n):
            for neighbour, dist in self.get_neighbours(node):
                edges.append([node, neighbour, dist])

        return edges

    def reversed_graph(self):
        r_graph = Graph(self.__n, "directed")
        edges = self.get_edges()

        for node, neighbour, dist in edges:
            r_graph.link(neighbour, node, dist)

        return r_graph
