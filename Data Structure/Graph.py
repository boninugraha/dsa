class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            if v1 in self.adj_list[v2] and v2 in self.adj_list[v1]:
                self.adj_list[v2].remove(v1)
                self.adj_list[v1].remove(v2)
                return True
            
        return False
    
    def remove_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            return False
        connections = self.adj_list[vertex]
        
        for i in range(len(connections)):
            self.adj_list[connections[i]].remove(vertex)
        del self.adj_list[vertex]
        return True

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, self.adj_list[vertex])


gr = Graph()
gr.add_vertex('A')
gr.add_vertex('B')
gr.add_vertex('C')
gr.add_edge('A', "B")
gr.add_edge('A', "C")
# gr.remove_edge('A', 'B')
gr.remove_vertex('A')
gr.print_graph()