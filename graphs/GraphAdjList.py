class Graph:
  def __init__(self):
    self.adjList = {}

  def add_vertex(self, vertex):
    if vertex not in self.adjList:
      self.adjList[vertex] = []

  def add_edge(self, vertex, edge):
    self.add_vertex(vertex)
    self.add_vertex(edge)

    self.adjList[vertex].append(edge)
    self.adjList[edge].append(vertex)

  def printGraph(self):
    for vertex in self.adjList:
      print(vertex, " -> ", self.adjList[vertex], end="\n")



g = Graph()
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(1,4)
g.add_edge(4,3)
g.add_edge(2,4)
g.add_edge(4,5)
g.add_edge(5,3)

g.printGraph()


