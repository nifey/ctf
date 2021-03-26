# Solution
We are provided with an executable that implements a simple virtual machine.

The executable prints the flag file if we have used the VM instructions to copy a region of memory (that is initialized with Fibonacci numbers) to an adjacent region of memory.

compuder.py script generates the VM's assembly instructions to do memcpy of 33 integers.

## Description of VM instructions
Instruction format: op rout rin1 rin2
- 0 rout rin1 rin2 => rout = rin1 + rin2        (add)
- 1 rout rin1 rin2 => rout = rin1 - rin2        (sub)
- 2 rout rin1 rin2 => rout = rin1 * rin2        (mul)
- 3 rout rin1 rin2 => rout = rin1 & rin2        (and)
- 4 rout rin1 rin2 => rout = rin1 | rin2        (or)
- 5 rout rin1 rin2 => mov rout <- mem [rin1]    (load)
- 6 rout rin1 rin2 => mov mem [rout] <- rin1    (store)
- 7 rout rin1 rin2 => Stop execution and proceed to check

# Flag
```
UDCTF{r3v3rs!nG_cUst0m_VMs_1s_3Z}
```
