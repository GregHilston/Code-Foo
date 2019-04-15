

class GraphNode:
    class GraphEdge:
        def __init__(self, source: "GraphNode", destination: "GraphNode", max: int):
            self.source = source
            self.destination = destination
            self.max = max
            self.current = 0

    def __init__(self, name: str):
        self.name: str = name
        self.edges: [GraphNode.GraphEdge] = []

    def add_edge(self, destination: "GraphNode", max: int):
        self.edges.append(GraphNode.GraphEdge(self, destination, max))


class MaxFlow:
    def __init__(self, source: GraphNode):
        self.source = source

    def max_flow(self) -> int:
        flow = {}

        return -1