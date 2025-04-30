from collections import deque
def add_edge(graph,u,v):
    graph.setdefault(u,[]).append(v)
    graph.setdefault(v,[]).append(u)

def dfs(graph,node,visited):
    if node not in visited:
        print(node,end='')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph,neighbour,visited)

def bfs(graph,node):
    queue=deque([node])
    visited=set()
    while queue:
        node=queue.popleft()
        if node not in visited:
            print(node,end=' ')
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)



graph={}
num_edges=int(input("enter the no.of edges"))

print("enter the edge's start and end vertex")

for _ in range(num_edges):
    u,v=input().split()
    add_edge(graph,u,v)

visited=set()
start_node=input("enter the start node")

print("dfs traversal from start vertex ",start_node)


dfs(graph,start_node,visited)

print("bfs traversal from start vertex ",start_node)


bfs(graph,start_node)