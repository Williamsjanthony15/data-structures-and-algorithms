
class Graph:
    def add_node(self, value):
        self._adjacency_list[v] = []
        return v

    def add_edge(self, start_vertex, end_vertex, weight=1):

        if self._adjacency_list == {}:
            return None
        else:
            nodes = [*self._adjacency_list]
            print(nodes)

            for i in range(len(nodes)):
                nodes[i] = nodes[i].value

            return nodes

    def get_neighbors(self, node):

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

    def size(self):

        return len(self._adjacency_list)


class Vertex:
    def __init__(self, value):
        self.value = value
class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight
 
