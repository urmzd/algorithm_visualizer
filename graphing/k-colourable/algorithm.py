from typing import OrderedDict


def getGraph(filename: str):
    file = open(filename, "r");
    graph = {}

    for line in file:
        vertex, edges = line.strip().split(":")
        edges = [e.strip() for e in edges.split(",")]
        graph[vertex] = edges

    return graph;

'''
   visted: {[edge: string]: keyof colors} 
'''
graph = getGraph("")

### TEST
def countCapeBretonIsland(root: str, n: int, assigned_colors = {}, remaining_colors: int = 3, seperators = tuple()):
    if n == 0:
        return 1;

    if root in seperators or root in assigned_colors:
        return 0;

    if (remaining_colors):
        return 

print(countCapeBretonIsland("Cape Breton", 3))

