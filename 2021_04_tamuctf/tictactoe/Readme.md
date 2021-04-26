# Challenge: TicTacToe (pwn)
Hey, I made a tic tac toe game! If you can beat me enough times I'll give you a flag.
```
openssl s_client -connect tamuctf.com:443 -servername tictactoe -quiet
```

Downloaded files: [tictactoe](tictactoe) (python script)

# Solution
It is a python application that allows us to load our progress by giving a code.
I think this is similar to the python pickle challenges.
A pickle which is base64 encoded is the code which the game gives.

```
if get_hash(data['wins']) != data['security']:
```

Some hash function is applied to the number of wins and that is added as security
The only challenge now is to find this hash function
The security is 32 B, It could be 256 bit hash

I later realized that the python script is also provided in the challenge.
But that doesn't help either because it hashes the wins and the flag which we don't know.

Ok I think I thought too much without checking if os.system was accessible.
We can execute os.system.
With some help from the following blog, I simply cat the flag.txt file.
And that gave the flag

[https://davidhamann.de/2020/04/05/exploiting-python-pickle](https://davidhamann.de/2020/04/05/exploiting-python-pickle)

[pkl.py](pkl.py) is the script that generates the code that gives out the flag.

# Flag
```
gigem{h3y_7h47_d035n'7_l00k_l1k3_4_p1ckl3d_54v3}
```
