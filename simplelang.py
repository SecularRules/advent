# copying to test ruff - check runs and gives additional feedback.
# format also runs

import string


def run(program):
    # would be better to have less functions and no global variables.
    global printlist
    printlist = []
    global location
    location = {}  # save location name and index
    global vars
    vars = {char: 0 for char in string.ascii_uppercase}  # initialise vars
    global i
    i = 0
    build_dic(program)  # gotta find locations first

    eval_program(program, i)
    return printlist


def build_dic(program):
    k = 0
    for j in program:
        j = j.split(" ")
        location[j[0][:-1]] = k
        k += 1

def eval_program(program, i):
    if len(program) == 0:
        return
    while True:
        line = program[i]
        line = line.split(" ")
        match line[0]:
            case "PRINT":
                PRINT(line[1])
            case "MOV":
                MOV(line[1], line[2])
            case "ADD":
                ADD(line[1], line[2])
            case "SUB":
                SUB(line[1], line[2])
            case "MUL":
                MUL(line[1], line[2])
            case "JUMP":
                i = location[line[1]] - 1  # doubt if should be function but needs pogram
            case "IF":
                if IF(line[1], line[2], line[3]):
                    i = location[line[5]] - 1
            case "END":
                return  # printlist
            case _:  # catch all for the locations
                location[line[0][:-1]] = i
        i += 1
        if i >= len(program):
            return

def PRINT(a):
    if a in vars:
        printlist.append(vars[a])
    else:
        printlist.append(int(a))

def MOV(a, b):
    if b in vars:
        vars[a] = vars[b]
    else:
        vars[a] = int(b)

def ADD(a, b):
    if b in vars:
        vars[a] += vars[b]
    else:
        vars[a] += int(b)

def SUB(a, b):
    if b in vars:
        vars[a] -= vars[b]
    else:
        vars[a] -= int(b)

def MUL(a, b):
    if b in vars:
        vars[a] *= vars[b]
    else:
        vars[a] *= int(b)

def IF(val1, op, val2):
    if val1 in vars:
        val1 = vars[val1]
    if val2 in vars:
        val2 = vars[val2]

    match op:
        case "==":
            return int(val1) == int(val2)
        case ">=":
            return int(val1) >= int(val2)
        case "<=":
            return int(val1) <= int(val2)
        case "<":
            return int(val1) < int(val2)
        case ">":
            return int(val1) > int(val2)
        case "!=":
            return int(val1) != int(val2)


if __name__ == "__main__":
    program1 = []
    program1.append("MOV A 1")
    program1.append("MOV B 999")
    program1.append("start:")
    program1.append("ADD A 1")
    program1.append("SUB B 1")
    program1.append("ADD C 1")
    program1.append("IF A == B JUMP end")
    program1.append("JUMP start")
    program1.append("end:")
    program1.append("PRINT C")

    result = run(program1)
    print(result)