# Graphsp

## Project description
This project implements algorithms associated with ` Graph Data Structure `.

The following is the list of algorithm this library implements:

- Breadth First Search
- Depth First Search
- Dijkstra (Single Source Shortest Path)
- Floyd Warshall (All Pairs Shortest Path)

## Installation
` pip install graphsp `

## Usage
` from graphsp import Graph `

Initializing graph object
```
graph = graphsp.Graph(n, graph_type)
```
n = Total number of nodes
graph_type = directed / undirected [in string]


Initializing & Populating the graph
```
graph = graphsp.Graph(5, "undirected")

graph.bulk_link([(0, 4, 5), (0, 1, 1), (1, 4, 3),
                 (1, 3, 1), (1, 2, 15), (2, 3, 2), (3, 4, 3)])
```

Using different algorithms
```
fw = FloydWarshall(n, graph)
print(fw.floyd_warshall())

dfs = DFS(n, graph)
print(dfs.dfs(start_node))

bfs = BFS(n, graph)
print(bfs.bfs(start_node))

dj = Dijkstra(n, graph)
print(dj.dijkstra(start_node))
```
n = Total number of nodes
start_node = Number on the desired starting node
graph = Object of Graph class

## Github repository
` https://github.com/jainam2385/graphsp `


## License
© 2022 Jainam Shah
This repository is licensed under the MIT license. See LICENSE for details.
