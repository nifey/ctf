# Challenge: Lottery (pwn)
Attack this binary and get the flag!
```
openssl s_client -connect tamuctf.com:443 -servername lottery -quiet
```

Downloaded files: [lottery](lottery) (binary)

# Solution
Giving 1337 as the choice allows us to cheat and win the lottery.
But I think we need to get a shell in this challenge.

The vulnerability is in the ask\_name function. It has a call to gets function.

I think this is a Return oriented programming challenge. There is no canary.
And we have the gets which allows us to just add a lot of return addresses.

I was able to invoke execve syscall with "/bin/sh" string which is loaded using
feature to load lottery numbers.
After the shell is created, reading flag.txt gave the flag.

[exploit.py](exploit.py) generates the exploit string.

# Flag
```
gigem{3x3cu74bl3_rn6}
```
