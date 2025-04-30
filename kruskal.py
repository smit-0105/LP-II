def find(parent,node):
    while parent[node]!=node:
        node=parent[node] 
    return node
5

def union(parent,u,v):
    root_u=find(parent,u)
    root_v=find(parent,v)

    if root_u != root_v:
        parent[root_v]=root_u
        return True
    return False

def kruskal(edges):
    edges.sort(key=lambda x:x[2])
    parent={}
    min_edg=[]
    total_cost=0

    for u,v,_ in edges:
        parent[u]=u
        parent[v]=v
    
    for u,v,weight in edges:
        if union(parent,u,v):
            min_edg.append((u,v,weight))
            total_cost+=weight

    for u,v,w in min_edg:
        print(f"{u}-{v} :{weight}")

edges = []
n = int(input("Enter number of edges: "))
print("Enter edges as: node1 node2 weight")
for _ in range(n):
    u, v, w = input().split()
    w = int(w)
    edges.append((u, v, w))

kruskal(edges)



