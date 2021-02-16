def all_adjacent_pairs(path):
    for i in range(0, len(path) - 1):
        yield path[i], path[i + 1]


def adjacent_digits_check(pair, passwordStr):
    index, (a, b) = pair
    if a != b:
        return False
    # print('here', pair, passwordStr)
    if index > 0 and passwordStr[index - 1] == a:
        return False
    if index < len(passwordStr) - 2 and passwordStr[index + 2] == a:
        return False
    return True


def adjacent_digits(password):
    return any(map(lambda x: adjacent_digits_check(x, str(password)), enumerate(all_adjacent_pairs(str(password)))))


def increasing(password):
    return all(map(lambda x: x[0] <= x[1], all_adjacent_pairs(str(password))))


minimum, maximum = map(int, input().split('-'))

count = 0
for password in range(minimum, maximum + 1):
    if adjacent_digits(password) and increasing(password):
        count += 1
print(count)