# Solution

The binary file contains a string "looking good" which is printed only for the correct commandline argument.
Using z3 (in rev.py) we can find the correct commandline argument to the executable, which is Fz44=H

Executing the binary with correct argument, gives us a bunch of hex values in memory, which when decoded
as ASCII gives us the text in ascii file.

script.sh extracts the flag out of the ASCII text.

# Flag
```
UDCTF{wh4t_c4n_I_say_luv_crypt0}
```
