class Graph:
  def __init__(self, vertex):
    self.mat = [[0]*vertex for x in range(vertex)]
    self.size = vertex

  def add_edge(self, source, destination, weight):
    if (0 <= source < self.size and 0<= destination < self.size):
      self.mat[source][destination] = weight
      self.mat[destination][source] = weight
    else:
      print("Invalid edge")

  def print(self):
    for row in self.mat:
      print(' '.join(map(str, row)))     


G = Graph(5)

G.add_edge(0, 2, 5)
G.add_edge(0, 1, 6)
G.add_edge(1, 3, 7)
G.add_edge(2, 3, 8)
G.add_edge(2, 4, 9)
G.add_edge(3, 4, 10)

G.print()