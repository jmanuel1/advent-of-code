from operator import add, mul
programString = input()
program = list(map(int, programString.split(',')))

for x in range(0, 100):
    for y in range(0, 100):
        memory = program[:]
        memory[1:3] = x, y

# Traceback (most recent call last):
#   File ".\solution2.py", line 42, in <module>
#     program[program[ip + 3]] = op(program[program[ip + 1]], program[program[ip + 2]])
# TypeError: list indices must be integers or slices, not Symbol
# class Symbol:
#
#     def __init__(self, name):
#         self._value = name
#
#     def __add__(self, other):
#         return type(self)({'add': [self, other]})
#
#     def __mul__(self, other):
#         return type(self)({'mul': [self, other]})
#
#     def __str__(self):
#         if isinstance(self._value, str):
#             return self._value
#         op, children = '', []
#         if 'add' in self._value:
#             op, children = '+', self._value['add']
#         elif 'mul' in self._value:
#             op, children = '*', self._value['mul']
#         return str(children[0]) + op + str(children[1])

#
# # Treat memory[1] and memory[2] as symbols
# memory[1] = Symbol('x')
# memory[2] = Symbol('y')

        for ip in range(0, len(memory), 4):
            if memory[ip] == 99 and memory[0] == 19690720:
                print(x, y, memory)
                break
            op = None
            if memory[ip] == 1:
                op = add
            elif memory[ip] == 2:
                op = mul
            if op is None:
                continue
            memory[memory[ip + 3]] = op(memory[memory[ip + 1]], memory[memory[ip + 2]])
