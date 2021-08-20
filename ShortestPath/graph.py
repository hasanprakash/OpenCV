class Graph:
    g = []
    def createGraph(self, alldots):
        for i in alldots:
            g1 = []
            for j in alldots:
                if i != j:
                    dis = ((j[0] - i[0])**2 + (j[1] - i[1])**2)
                    g1.append(dis)
                else:
                    g1.append(0)
            Graph.g.append(g1)
        
        # for i in self.g:
        #     for j in i:
        #         print(j, end=" ")
        #     print()