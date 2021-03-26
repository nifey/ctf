# Solution
I converted the checker.wasm file into wat format and figured out what it was trying to do.
It checks the correct flag by doing a multiplication followed by a modulus operation on a bunch of values defined in memory.

watman.py script does the reverse operation to get the flag from the values obtained.

# Flag
```
UDCTF{wh0a_w4sm_i5_lit_y4l1}
```
