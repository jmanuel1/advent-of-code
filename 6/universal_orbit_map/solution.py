import sys
from collections import defaultdict


# unique
def all_paths(graph, root):
    if not graph[root]:
        return
    for child in graph[root]:
        yield root, child
        bs = set()
        for a, b in all_paths(graph, child):
            yield a, b
            if b not in bs:
                yield root, b
                bs.add(b)


def count_paths(graph, root):
    count = 0
    for __ in all_paths(graph, root):
        count += 1
    return count


graph = defaultdict(lambda: [])
for line in sys.stdin:
    body, satellite = line.strip().split(')')
    graph[body].append(satellite)
print(graph)
print(count_paths(graph, 'COM'))
