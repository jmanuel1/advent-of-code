def all_adjacent_pairs(path):
    for i in range(0, len(path) - 1):
        yield path[i], path[i + 1]


def adjacent_digits(password):
    return any(map(lambda x: x[0] == x[1], all_adjacent_pairs(str(password))))


def increasing(password):
    return all(map(lambda x: x[0] <= x[1], all_adjacent_pairs(str(password))))


minimum, maximum = map(int, input().split('-'))

count = 0
for password in range(minimum, maximum + 1):
    if adjacent_digits(password) and increasing(password):
        count += 1
print(count)