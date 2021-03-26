from z3 import *

s = Solver()

vars = [BitVec('v'+str(i), 48) for i in range(0,101)]

s.add(vars[100] == 0xfd94e6e84a0a) # Target value found in binary

for i in range(0,100):
    j = 100 - i
    s.add(((vars[j-1] * 0x5deece66d) + 0xb) == vars[j])

if s.check() == sat:
    m = s.model()
    answer = m[vars[0]]
    answer = answer.as_long()
    while answer > 0:
        print(chr(answer & ((1<<8) - 1)), end='')
        answer >>= 8
    print("")
else:
    print("Not satisfiable")
