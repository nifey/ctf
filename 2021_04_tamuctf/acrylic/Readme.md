# Challenge: Acrylic (Rev)
This is an easy challenge. There is a flag that can be printed out from somewhere in this binary. Only one problem: There's a lot of fake flags as well.

Downloaded files: [acrylic](acrylic) (binary)

# Solution
This was easy. Just open the debugger. Break at main. Change the Instruction pointer to point to get\_flag function.
At the point where it leaves the get\_flag function, the address of the right flag is present in rax.

# Flag
```
gigem{counteradvise_orbitoides}
```
