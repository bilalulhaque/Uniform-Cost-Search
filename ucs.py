#Uniform Cost Search

import copy

graph = {
    'A': {'O': 146, 'S':140, 'C':494},
    'O': {'A': 146, 'S': 151},
    'C': {'A':494, 'P':138, 'R': 146},
    'S': {'A':140, 'O':151, 'F':99, 'R':80},
    'R': {'S':80, 'C':146, 'P':97},
    'P': {'R': 97, 'C':138, 'B':101},
    'F': {'B':211, 'S':99},
    'B': {'F': 211, 'P':101}
}



def ucs(start,final):
    path=[]
    priorityQueue = [[[start], 0]]
    visited = []
    while priorityQueue!=[]:
        path.append(priorityQueue.pop(0))
        node=path[-1][0][-1]
        visited.append(node)
        if node == final:
            finalPath = copy.deepcopy(path[-1])
            print("final", finalPath)
            return "Found"
        for neighbor,cost in graph[node].items():
            if neighbor not in visited:
                newpath=copy.deepcopy(path[-1])
                newpath[0].append(neighbor)
                newpath[1]+=cost
                priorityQueue.append(newpath)
                # print("Priority Queue", priorityQueue)

        priorityQueue.sort(key=lambda x:x[1])
        # print("Visited", visited)

ucs('A','B')


