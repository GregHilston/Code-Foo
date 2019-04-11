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
        source.children.append((one, 16))
        source.children.append((two, 13))

        one.children.append((two, 10))
        one.children.append((three, 12))

        two.children.append((one, 4))
        two.children.append((four, 14))

        three.children.append((two, 9))
        three.children.append((sink, 20))

        four.children.append((three, 7))
        four.children.append((sink, 4))

        self.sut = MaxFlow(source)

    def test_max_flow(self):
        self.assertEqual(4, self.sut.max_flow())

if __name__ == '__main__':
    unittest.main()