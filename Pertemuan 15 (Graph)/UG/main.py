
class Graph:
    def __init__(self):
        self.data = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.data:
            self.data[vertex] = []
    def get_vertex(self):
        for key in self.data.keys():
            print(key, end = " ")
        print()
    def add_edge(self, x, y):
        if x in self.data and y in self.data:
            self.data[x].append(y)
            self.data[y].append(x)
    
    def get_edges(self):
        list_edges = set()
        for vertex, neighbors in self.data.items():
            for neighbor in neighbors:
                if neighbor+vertex not in list_edges and vertex+neighbor not in list_edges:
                    list_edges.add(vertex+neighbor)
        return list(list_edges)

    def find_path_dfs(self, v1, v2):
        stack : list = [v1]
        visited : list = [v1] 
        path : list = [v1]

        while len(stack) > 0:
            popped = stack.pop()
            neighbors = self.data[popped]
            unvisited = 0
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.append(neighbor)
                    path.append(neighbor)
                    stack.append(neighbor)
                    unvisited += 1
                    break         

            if unvisited == 0:
                if path[-1] == v2:
                    break

                if len(path) <= 1:
                    return

                path.pop()
                stack.append(path[-1])
            
        return path

    def is_path_possible(self, path : list):


        for i in range(len(path) - 1):
            data=self.data
            awal = path[i]
            akhir=path[i + 1]
            if awal not in data or akhir not in data[awal]:
                return False
            
        if len(path) < 2:
            return False
        
        return True
    
            
        


def main () :
    
    g : Graph = Graph()
    for i in range(1, 11):
        g.add_vertex("v"+str(i))
    
    g.add_edge("v1", "v2")
    g.add_edge("v1", "v3")
    g.add_edge("v2", "v4")
    g.add_edge("v2", "v5")
    g.add_edge("v3", "v5")
    g.add_edge("v4", "v6")
    g.add_edge("v4", "v7")
    g.add_edge("v5", "v7")
    g.add_edge("v7", "v8")
    g.add_edge("v7", "v9")
    g.add_edge("v9", "v10")
    g.add_edge("v8", "v9")

    print(g.is_path_possible(["v1", "v2", "v4","v6"]))
    print(g.is_path_possible(["v7", "v8", "v10"]))
    print(g.is_path_possible(["v1", "v2", "v3"]))
    print(g.is_path_possible(["v8", "v7", "v9", "v10"]))
    print(g.is_path_possible(["v2", "v7"]))
    print(g.is_path_possible(["v2", "v5", "v7", "v9", "v10"]))
if __name__ == "__main__":
    main()