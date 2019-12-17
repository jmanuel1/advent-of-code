from operator import add, mul
programString = input()
program = list(map(int, programString.split(',')))

for ip in range(0, len(program), 4):
    if program[ip] == 99:
        print(program)
        break
    op = None
    if program[ip] == 1:
        op = add
    elif program[ip] == 2:
        op = mul
    if op is None:
        continue
    program[program[ip + 3]] = op(program[program[ip + 1]], program[program[ip + 2]])
