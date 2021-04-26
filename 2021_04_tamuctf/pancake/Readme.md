# Challenge: Pancake (pwn)
Attack this binary to get the flag!
```
openssl s_client -connect tamuctf.com:443 -servername pancake -quiet
```

Downloaded files: [pancake](pancake) (binary)

# Solution
This is easy.
The binary expects the value 0x8406688 at rbp-0xc at a point in the program. 
If the value is present then it prints the flag.

[exploit.py](exploit.py) generates the exploit string.

# Flag
```
gigem{b4s1c_b4ff3r_0verfl0w_g03s_y33t}
```
