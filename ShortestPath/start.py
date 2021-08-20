from SandD import SnD
from graph import Graph
from itertools import permutations
import sys
from lines import PlotLine

class Start:
    def start(self):
        source = SnD.source
        destination = SnD.destination
        alldots = SnD.alldots

        # WITH PERMUTATION FUNCTION
        # print(ShortestPath.travellingsalesman(source, destination, alldots, Graph.g))

        # WITH RECURSIONS (BEST)
        a = list(alldots)

        V = len(alldots)
        s = alldots.index(source)
        d = alldots.index(destination)
        SnD.s = s
        SnD.d = d
        vertex = []
        for i in range(V):
            # if i != s and i != d:
            vertex.append(i)


        obj = ShortestPath(vertex, Graph.g, s, d)
        ShortestPath.travellingsalesman(vertex, 0, len(vertex)-1)
        SnD.sPath = ShortestPath.allpaths[ShortestPath.min_path]
        SnD.minDis = ShortestPath.min_path
        # SnD.sPath = range(len(SnD.alldots))
        PlotLine.plotLine()


class ShortestPath:

    def __init__(self, vertex, graph, s, d):
        ShortestPath.vertex = vertex
        ShortestPath.min_path = sys.maxsize
        ShortestPath.graph = graph
        ShortestPath.s = s
        ShortestPath.d = d
        ShortestPath.allpaths = {}
    def travellingsalesman(vertex, l, r):
        

        if l==r:
            if vertex[0] == ShortestPath.s and vertex[-1] == ShortestPath.d:
                current_pathweight = 0
                k = ShortestPath.s
                for j in vertex:
                    current_pathweight += ShortestPath.graph[k][j]
                    k = j
                current_pathweight += ShortestPath.graph[k][ShortestPath.s]
        
                ShortestPath.allpaths[current_pathweight] = list(vertex)
                ShortestPath.min_path = min(ShortestPath.min_path, current_pathweight)
        else:
            for i in range(l,r+1):
                vertex[l], vertex[i] = vertex[i], vertex[l]
                ShortestPath.travellingsalesman(vertex, l+1, r)
                vertex[l], vertex[i] = vertex[i], vertex[l] 


















    # def travellingsalesman(source, destination, alldots, graph):
    #     V = len(alldots)
    #     s = alldots.index(source)
    #     d = alldots.index(destination)
    #     print(s)
    #     vertex = []
    #     for i in range(V):
    #         if i != s and i != d:
    #             vertex.append(i)
    
    #     min_path = sys.maxsize
    #     next_permutation=permutations(vertex)
    #     allpaths = {}
    #     print(vertex)
    #     for i in next_permutation:            
    #         current_pathweight = 0
    #         k = s
    #         for j in i:
    #             current_pathweight += graph[k][j]
    #             k = j
    #         current_pathweight += graph[k][s]
    
    #         allpaths[current_pathweight] = list(i)
    #         min_path = min(min_path, current_pathweight)
            
    #     # IT'S THE BEST PATH
    #     print(allpaths[min_path])
    #     return min_path