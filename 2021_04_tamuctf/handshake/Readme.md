# Challenge: Handshake (pwn)
Attack this binary and get the flag!
```
openssl s_client -connect tamuctf.com:443 -servername handshake -quiet
```

Downloaded files: [handshake](handshake) (binary)

# Solution
This is a simple stack overflow.
Placing the address of win function as the return address gives the flag.

[exploit.py](exploit.py) generates the exploit string.

# Flag
```
gigem{r37urn_c0n7r0l1337}
```
