# Challenge: Pwgen (crypto)
We're trying to figure out the current password of REDACTED. We have reason to believe that they generated a set of passwords at the same time using a custom password generation program and that their previous password was *ElxFr9)F* . Can you figure out their current password?
```
openssl s_client -connect tamuctf.com:443 -servername pwgen -quiet
```

Downloaded files: [main.rs](main.rs) (password generation program)

# Solution
Here our objective is to find the seed used for the password generation

Using z3 to solve for the initial seed gives us the seed value 718549711.
The z3 code can be found in [rev.py](rev.py).
To avoid negative values and wrapping, I used 31 bit bit-vectors in z3

I changed the rust source to use the new seed and generate 2 passwords.
The first one is the password given in the description and the second one,
*xV!;28vj* is the password that needs to be used (in remote) to get the flag.

The new rust source with hardcoded seed is [newmain.rs](newmain.rs).

```
python rev.py # This gives the seed
rustc newmain.rs
./newmain # generate 2 passwords
```

# Flag
```
gigem{cryp706r4ph1c4lly_1n53cur3_prn65_DC6F9B}
```
