import r2pipe

r = r2pipe.open('./chall')
r.cmd("aaa")

# Find the name of all walk functions
# afl~walk => list all functions, followed by a grep search for "walk"
functions = r.cmd("afl~walk | sed 's/.*sym.walk/sym.walk/'").split("\n")
functions.remove("")

call_info = {}

# For each walk function find out which other walk functions are called from it
# pds => prints summary (calls, jumps, ...)
for function in functions:
    callees = r.cmd("pds @ "+function+"; ~call~[2] | grep -v get_input").split("\n")
    callees.remove("")
    call_info[function] = callees

# Find a path from walk_start to walk_end using depth first search
# This will populate the path (in reverse order) in path array
path = []
def dfs(current_function):
    if current_function == 'sym.walk_end':
        return True
    for func in call_info[current_function]:
        if dfs(func):
            path.append(func)
            return True
    return False
dfs('sym.walk_start')

current_function = path[0]
path.remove(path[0])
path.append('sym.walk_start')

# For each function in the path, find out what value of if condition or case statement is used
# pdg => print disassembly using ghidra
solution = []
for function in path:
    disass = (r.cmd("pdg @ " + function + " | grep " + current_function + " -B1")).split("\n")[0]
    if disass.strip().find('if') == -1:
        # Case statement
        solution.append(chr(int(disass.strip().split("0x")[1].split(":")[0], 16)))
    else:
        # If statement
        solution.append(disass.strip().split("'")[1])
    current_function = function

solution.reverse()
soln_file = open("solution", "w")
for char in solution:
    soln_file.write(char)
