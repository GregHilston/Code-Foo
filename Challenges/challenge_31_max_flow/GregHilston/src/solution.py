# Definition for a binary tree node.
class GraphNode:
    def __init__(self, name: str):
        self.name: str = name
        self.children: [(GraphNode, int)] = []

class MaxFlow:
    def __init__(self, source: GraphNode):
        self.source = source

    def max_flow(self) -> int:
        return -1