import sys

total = 0
for line in sys.stdin:
    if line:
        mass = int(line)
        while True:
            fuel = mass//3 - 2
            if fuel <= 0:
                break
            total += fuel
            mass = fuel

print(total)
