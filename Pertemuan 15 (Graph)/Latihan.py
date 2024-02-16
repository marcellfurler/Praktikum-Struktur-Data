class Graph():
    def __init__(self):
        self._data={}

    def addVertex(self, key):
        if key not in self._data:
            self._data[key]=set()

    def vertex(self):
        for key, value in self._data.items():
            print(key, end=" ")

    def addEdge(self, x, y):
        if x in self._data and y in self._data:
            self._data[x].add(y)
            self._data[y].add(x)


    def edge(self):
        listEdge=set()
        for key, value in self._data.items():
            for item in self._data[key]:
                if key+item not in listEdge and item+key not in listEdge:
                    listEdge.add(key+item)
        for item in listEdge:
            print(item, end=" ")
        print()

    def findPath(self, x, y):
        visited=[]
        self.dfs(x,y,visited)

    def dfs(self, node, x, y, visited):
        visited.append(node)
        if node==y:
            print(visited)
        else:
            for item in self._data[node]:
                if item not in visited:
                    self.dfs(item, y, visited)

    def findPathdfs(self, v1, v2):
        vNow=v1
        path:list=[v1]
        visited=[v1]
        while len(path)>0:
            if vNow==v2:
                break

            neighbors=self.data[vNow]
            isPathAdded=False
            for neighboren in neighbors:
                if neighboren not in visited:
                    vNow=neighboren
                    path.append(vNow)
                    visited.append(vNow)
                    isPathAdded=True
                    break
            if not isPathAdded:
                path.pop()
                if len(path)>0:
                    vNow=path[-1]
        return path
    


graph=Graph()
graph.addVertex("A")
graph.addVertex("B")
graph.addVertex("C")
graph.addVertex("D")
graph.addEdge("A", "B")
graph.addEdge("A", "C")
graph.addEdge("A", "D")
graph.addEdge("B", "D")
graph.addEdge("C", "D")
graph.vertex()
graph.edge()