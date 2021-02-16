import sys

total = 0
for line in sys.stdin:
    if line:
        mass = int(line)
        fuel = mass//3 - 2
        total += fuel

print(total)
