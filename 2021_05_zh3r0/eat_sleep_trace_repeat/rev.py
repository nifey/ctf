mem_402000 = 0x41424344 # Initial seed
mem_402008 = []

# Generating the characters in memory
for i in range(2048):
    rcx = (mem_402000 & 0xffffffffffffffff)
    rdx = rcx
    rdx >>= 0xc
    rcx ^= rdx
    rdx = rcx

    rdx = (rdx << 0x19) & 0xffffffffffffffff
    rcx ^= rdx
    rdx = rcx

    rdx >>= 0x1b
    rcx ^= rdx

    rax = (0x2545f4914f6cdd1d * rcx) & 0xff
    mem_402008.append(rax)
    mem_402000 = rcx

mem_402808 = [] # Characters inputed
indices = [262 ,28 ,613 ,10 ,22 ,86 ,19 ,218 ,19 ,3 ,174 ,22 ,106 ,3 ,416 ,84 ,164 ,85 ,174 ,416 ,19 ,3 ,10 ,613 ,159 ,613 ,10 ,51 ,218 ,84 ,582 ,3 ,150 ,218 ,96 ,28 ,22 ,106 ,96 ,3 ,939 ,218 ,84 ,330 ,10 ,174 ,3 ,246 ,408 ,323 ,692 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ,260 ]

for i in indices:
    mem_402808.append(mem_402008[i-1])

for i in mem_402808:
    print (chr(i), end="")
