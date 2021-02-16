import sys
from collections import defaultdict


def first_equal(i, j):
    last_item = None
    for i_item, j_item in zip(i, j):
        if i_item != j_item:
            return last_item
        last_item = i_item


def parents(tree, node):
    current = node
    while tree[current]:
        current = tree[current]
        yield current


def nearest_common_ancestor(tree, a, b):
    return first_equal(reversed(tuple(parents(tree, a))), reversed(tuple(parents(tree, b))))


def distance(tree, node, ancestor):
    dist = 0
    while node != ancestor:
        dist += 1
        node = tree[node]
    return dist


# graph links nodes to parents
graph = defaultdict(lambda: None)
for line in sys.stdin:
    body, satellite = line.strip().split(')')
    graph[satellite] = body
print(graph)
ancestor = nearest_common_ancestor(graph, 'YOU', 'SAN')
print(distance(graph, 'YOU', ancestor) + distance(graph, 'SAN', ancestor) - 2)
