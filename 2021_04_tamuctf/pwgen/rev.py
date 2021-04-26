from z3 import *

s = Solver()

seeds = [BitVec('seed'+str(i), 31) for i in range(0,9)]
prev_pass = 'ElxFr9)F'
prev_pass_value = [BitVecVal(ord(prev_pass[i]) - 0x21, 31) for i in range(0,8)]

for i in range(1,9):
    s.add(seeds[i] == (seeds[i-1] * 1103515245) + 12345)
for i in range(len(prev_pass)):
    s.add(((seeds[i+1] >> 16) & 0x7fff) % 0x5e == prev_pass_value[i])

if s.check() == sat:
    m = s.model()
    answer = m[seeds[0]]
    print("Seed :",answer)
else:
    print("Not satisfiable")
