from typing import Tuple


def add(point1, point2):
    return point1[0] + point2[0], point1[1] + point2[1]


def mul(number, point):
    return number * point[0], number * point[1]


def horizontal(line):
    return line[0][1] == line[1][1]


def all_points_in_line(line):
    # assume endpoints are in order
    assert line[0] <= line[1]
    incr = (1, 0) if horizontal(line) else (0, 1)
    point = line[0]
    while point <= line[1]:
        yield point
        point = add(point, incr)


def manhattan_from_origin(point):
    return abs(point[0]) + abs(point[1])


def closest_to_center_in_line(line: Tuple[Tuple[int, int], Tuple[int, int]]) -> Tuple[int, int]:
    return min(all_points_in_line(line), key=manhattan_from_origin)


def intersect(line1, line2):
    # sort endpoints
    line1 = tuple(sorted(line1))
    line2 = tuple(sorted(line2))
    if horizontal(line1):
        if horizontal(line2):
            line1, line2 = sorted((line1, line2))
            if line2[1][0] >= line1[1][0] >= line2[0][0] and line1[0][1] == line2[0][1]:
                return closest_to_center_in_line((line2[0], line1[1]))
        elif line1[0][0] <= line2[0][0] <= line1[1][0] and line2[0][1] <= line1[0][1] <= line2[1][1]:
            return line2[0][0], line1[0][1]
    elif horizontal(line2):
        return intersect(line2, line1)
    else:
        line1, line2 = sorted((line1, line2))
        if line2[1][1] >= line1[1][1] >= line2[0][1] and line1[0][0] == line2[0][0]:
            return closest_to_center_in_line((line2[0], line1[1]))
    # no intersection
    return False


def all_adjacent_pairs(path):
    for i in range(0, len(path) - 1):
        yield path[i], path[i + 1]


path1 = [(0, 0)]
pathDesc1 = input().split(',')
for part in pathDesc1:
    direction, distance = part[0], int(part[1:])
    difference = {'R': (1, 0), 'D': (0, -1), 'L': (-1, 0),
                  'U': (0, 1)}[direction]
    path1.append(add(path1[-1], mul(distance, difference)))

path2 = [(0, 0)]
pathDesc2 = input().split(',')
for part in pathDesc2:
    direction, distance = part[0], int(part[1:])
    difference = {'R': (1, 0), 'D': (0, -1), 'L': (-1, 0),
                  'U': (0, 1)}[direction]
    path2.append(add(path2[-1], mul(distance, difference)))

intersections = []
for line1 in all_adjacent_pairs(path1):
    for line2 in all_adjacent_pairs(path2):
        intersection = intersect(line1, line2)
        if intersection and intersection != (0, 0):
            intersections.append(intersection)
print(manhattan_from_origin(min(intersections, key=manhattan_from_origin)))
