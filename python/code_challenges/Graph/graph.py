class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):

        v = Vertex(value)
        self._adjacency_list[v] = []
        return v

    def add_edge(self, start_vertex, end_vertex, weight=1):

        if start_vertex not in self._adjacency_list:
            raise KeyError("Start isnt looking to well")
        if end_vertex not in self._adjacency_list:
            raise KeyError("End Not in sight")

        edge = Edge(end_vertex, weight)
        adjacencies = self._adjacency_list[start_vertex]
        adjacencies.append(edge)

    def get_nodes(self):

        if self._adjacency_list == {}:
            return None
        else:
            nodes = [*self._adjacency_list]
            print(nodes)

            for i in range(len(nodes)):
                nodes[i] = nodes[i].value

            return nodes

    def get_neighbor(self, node):

        nodes = [*self._adjacency_list]
        print(nodes)

        for i in range(len(nodes)):
            if nodes[i].value == node:
                adjacencies = self._adjacency_list[nodes[i]]
                print(adjacencies)

                adjacencies_with_weight = [
                    adjacencies[i].vertex.value,
                    adjacencies[i].weight,
                ]

                return adjacencies_with_weight
            else:
                raise KeyError("Null")

class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight


if __name__ == "__main__":
    graph = Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    c = graph.add_node("c")
    d = graph.add_node("d")
    e = graph.add_node("e")
    f = graph.add_node("f")
    g = graph.add_node("g")
    h = graph.add_node("h")
    graph.add_edge(a, b)
    graph.add_edge(a, c)
    graph.add_edge(b, d)
    graph.add_edge(c, d)
    graph.add_edge(a, e)
    graph.add_edge(e, f)
    graph.add_edge(e, g)
    graph.add_edge(f, h)
    print(graph.get_neighbors(a))
 
