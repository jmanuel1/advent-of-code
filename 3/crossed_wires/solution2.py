from typing import Tuple
from collections import namedtuple


class Point(namedtuple('Point', ['x', 'y', 'steps'])):

    def __add__(self, other):
        # print(type(self), type(other))
        return type(self)(self[0] + other[0], self[1] + other[1], self.steps + other.steps)

    def __mul__(self, number):
        return type(self)(number * self[0], number * self[1], self.steps * number)

    def __eq__(self, other):
        return self.x == other[0] and self.y == other[1]

    # sort functions are guaranteed to use __lt__
    def __lt__(self, other):
        return self.x < other[0] or self.x == other[0] and self.y < other[1]

    def __ne__(self, other):
        return not (self == other)

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other


def horizontal(line):
    return line[0][1] == line[1][1]


def all_points_in_line(line):
    # assume endpoints are in order
    assert line[0] <= line[1]
    step_incr = 1 if line[0].steps < line[1].steps else -1
    incr = Point(1, 0, step_incr) if horizontal(line) else Point(0, 1, step_incr)
    point = line[0]
    # print(line)
    while point <= line[1]:
        yield point
        # print(point)
        point = point + incr
    assert point.steps == line[1].steps


def steps_given_line(line, point):
    # assert line[0] <= point <= line[1]
    # stepDir = 1 if line[0].steps < line[1].steps else -1
    # if horizontal(line):
    #     return (point[0] - line[0].x) * stepDir + line[0].steps
    # return (point[0] - line[0].y) * stepDir + line[0].steps

    for point_in_line in all_points_in_line(line):
        if point_in_line == point:
            return point_in_line.steps
    assert False


def steps_given_lines(line1, line2, point):
    steps1 = steps_given_line(line1, point)
    steps2 = steps_given_line(line2, point)
    return steps1 + steps2


def intersect(line1, line2):
    if horizontal(line1) and horizontal(line2) and line1[0].y != line2[0].y:
        return
    if not horizontal(line1) and not horizontal(line2) and line1[0].x != line2[0].x:
        return
    # sort endpoints
    line1 = tuple(sorted(line1))
    line2 = tuple(sorted(line2))
    # for point1 in all_points_in_line(line1):
    #     for point2 in all_points_in_line(line2):
    #         if point1 == point2 and point1 != (0, 0):
    #             yield point1, steps_given_lines(line1, line2, point1)

    if horizontal(line1):
        if horizontal(line2):
            line1, line2 = sorted((line1, line2))
            if line1[1][0] >= line2[0][0] and line1[0][1] == line2[0][1]:
                for point in all_points_in_line((line2[0], line1[1])):
                    if point != (0, 0):
                        steps = steps_given_lines(line1, line2, point)
                        yield point, steps
        elif line1[0][0] <= line2[0][0] <= line1[1][0] and line2[0][1] <= line1[0][1] <= line2[1][1]:
            point = line2[0][0], line1[0][1]
            if point != (0, 0):
                yield point, steps_given_lines(line1, line2, point)
    elif horizontal(line2):
        return intersect(line2, line1)
    else:
        line1, line2 = sorted((line1, line2))
        if line1[1][1] >= line2[0][1] and line1[0][0] == line2[0][0]:
            for point in all_points_in_line((line2[0], line1[1])):
                if point != (0, 0):
                    steps = steps_given_lines(line1, line2, point)
                    yield point, steps


def all_adjacent_pairs(path):
    for i in range(0, len(path) - 1):
        yield path[i], path[i + 1]


def build_path(desc):
    path = [Point(0, 0, 0)]
    for part in desc:
        direction, distance = part[0], int(part[1:])
        difference = {'R': Point(1, 0, 1), 'D': Point(0, -1, 1), 'L': Point(-1, 0, 1),
                  'U': Point(0, 1, 1)}[direction]
        path.append(path[-1] + difference * distance)
    return path


pathDesc1 = input().split(',')
path1 = build_path(pathDesc1)
pathDesc2 = input().split(',')
path2 = build_path(pathDesc2)
print(path1)
print(path2)
intersections = []
for line1 in all_adjacent_pairs(path1):
    for line2 in all_adjacent_pairs(path2):
        # print(line1, line2)
        for intersection, combined_steps in intersect(line1, line2):
            # print(intersection)
            intersections.append((intersection, combined_steps))
print(min(intersections, key=lambda tup: tup[1]))
