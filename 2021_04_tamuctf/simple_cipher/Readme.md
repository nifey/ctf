# Challenge: simple\_cipher (rev)
We have a flag encrypted using this program. Can you figure out what it is?

Downloaded files: [simple\_cipher](simple_cipher) (binary), [flag.enc](flag.enc) (encrypted flag)

# Solution
The binary generates random numbers with the seed 0x1337.
If we can generate the same random numbers then we can reverse it.
The string length seems to be 34. So we need to generate 34x2=68 random numbers with the seed 0x1337.

[rand.c](rand.c) generates 68 random numbers which is then used in [rev.py](rev.py) script to decrypt the flag.

# Flag
```
gigem{d0n7_wr173_y0ur_0wn_c1ph3r5}
```
