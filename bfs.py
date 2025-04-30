from collections import deque

def add_edge(graph,u,v):
    graph.setdefault(u,[]).append(v)
    graph.setdefault(v,[]).append(u)

def bfs(graph,start_node):
    visited=set()
    queue=deque([start_node])

    while queue:
        node=queue.popleft()
        if node not in visited:
            print(node,end=' ')
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)


graph={}

num_edges=int(input("enter no. of edges"))
print("enter the edge start and end vertex")
for _ in range(num_edges):
    u,v=input().split()
    add_edge(graph,u,v)
start_node=input("enter the start node")

bfs(graph,start_node)