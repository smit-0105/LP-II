   



def add_edge(graph,u,v,weight):
    graph.setdefault(u,[]).append((v,weight))
    graph.setdefault(v,[]).append((u,weight))

def prims_algo(graph,sv):
    visited=set([sv])
    mst=[]
    total_cost=0

    while len(visited)<len(graph):
        min_edge=None
        min_weight=float('inf')

        for u in visited:
            for v , weight in graph[u]:
                if v not in visited and weight<min_weight:
                    min_weight=weight
                    min_edge=(u,v)

        if min_edge:
            u,v=min_edge
            visited.add(v)
            mst.append((u,v,min_weight))
            total_cost+=min_weight


        for u,v, weight in mst:
            print(f"{u}-{v}:{weight}")

        print("total cost",{total_cost})

graph={}
no=int(input("enter the no of edges"))

for _ in range(no):
    u,v,weight=input().split()
    weight=int(weight)
    add_edge(graph,u,v,weight)

sv=input("enter sv")

prims_algo(graph,sv)
