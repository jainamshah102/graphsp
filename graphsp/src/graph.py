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
