from operator import add, mul


def get_param_modes(integer):
    names = ['position', 'immediate']
    param_modes = integer // 100
    while True:
        yield names[param_modes % 10]
        param_modes = param_modes // 10


def read(memory, address, mode):
    if mode == 'position':
        return memory[memory[address]]
    return memory[address]


programString = input()
program = list(map(int, programString.split(',')))

ip = 0
while ip < len(program):
    opcode, param_modes = program[ip] % 100, get_param_modes(program[ip])
    if opcode == 99:
        print(program)
        break
    op = None
    if opcode == 1:
        op = add
    elif opcode == 2:
        op = mul
    if op is None:
        if opcode == 3:
            # store input, assume position mode
            program[program[ip + 1]] = int(input())
            ip += 2
        elif opcode == 4:
            # output
            mode = next(param_modes)
            if mode == 'position':
                print(program[program[ip + 1]])
            else:
                print(program[ip + 1])
            ip += 2
        elif opcode == 5:
            # jump if true
            mode1, mode2 = next(param_modes), next(param_modes)
            if read(program, ip + 1, mode1):
                ip = read(program, ip + 2, mode2)
            else:
                ip += 3
        elif opcode == 6:
            # jump if false
            mode1, mode2 = next(param_modes), next(param_modes)
            if not read(program, ip + 1, mode1):
                ip = read(program, ip + 2, mode2)
            else:
                ip += 3
        elif opcode == 7:
            # less than, assume third parameter is in position mode
            mode1, mode2 = next(param_modes), next(param_modes)
            if read(program, ip + 1, mode1) < read(program, ip + 2, mode2):
                program[program[ip + 3]] = 1
            else:
                program[program[ip + 3]] = 0
            ip += 4
        elif opcode == 8:
            # equals, assume third parameter is in position mode
            mode1, mode2 = next(param_modes), next(param_modes)
            if read(program, ip + 1, mode1) == read(program, ip + 2, mode2):
                program[program[ip + 3]] = 1
            else:
                program[program[ip + 3]] = 0
            ip += 4
    else:
        # assume parameter 3 is in position mode
        mode1, mode2 = next(param_modes), next(param_modes)
        param1, param2 = None, None
        if mode1 == 'position':
            param1 = program[program[ip + 1]]
        else:
            param1 = program[ip + 1]
        if mode2 == 'position':
            param2 = program[program[ip + 2]]
        else:
            param2 = program[ip + 2]
        program[program[ip + 3]] = op(param1, param2)
        ip += 4
