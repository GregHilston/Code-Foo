import unittest
from solution import GraphNode
from solution import MaxFlow

class MaxFlowTests(unittest.TestCase):
    def setUp(self):
        # Create all our nodes
        source = GraphNode("source")
        one = GraphNode("1")
        two = GraphNode("2")
        three = GraphNode("3")
        four = GraphNode("4")
        sink = GraphNode("sink")

        # source edges
        source.add_edge(one, 16)
        source.add_edge(two, 13)

        one.add_edge(two, 10)
        one.add_edge(three, 12)

        two.add_edge(one, 4)
        two.add_edge(four, 14)

        three.add_edge(two, 9)
        three.add_edge(sink, 20)

        four.add_edge(three, 7)
        four.add_edge(sink, 4)

        self.sut = MaxFlow(source)

    def test_max_flow(self):
        self.assertEqual(4, self.sut.max_flow())

if __name__ == '__main__':
    unittest.main()