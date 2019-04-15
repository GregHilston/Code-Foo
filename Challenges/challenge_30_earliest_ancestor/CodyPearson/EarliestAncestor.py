class Node:
  parent = None
  value = None

  def __init__(self, value):
    self.value = value


def buildExampleTree():
  tree = {'1': Node('1'), '2': Node('2'), '3': Node('3'), '4': Node('4'), '5': Node('5')}

  tree['1'].parent = tree['4']
  tree['2'].parent = tree['4']
  tree['4'].parent = tree['3']
  tree['5'].parent = tree['3']

  return tree

def findParents(node):
  parents = []
  while True:
    node = node.parent
    if isinstance(node, Node):
      parents.append(node)
    else:
      break

  return parents

def findAncestor(tree, keyA, keyB):
  parentsA = set(findParents(tree[keyA]))
  parentsB = set(findParents(tree[keyB]))

  commonParents = list(parentsA.intersection(parentsB))
  
  if len(commonParents) > 0:
    return commonParents.pop().value
  else:
    return -1


def test():
  tree = buildExampleTree()
  ancestor = findAncestor(tree, '1', '2')
  print(ancestor)

test()