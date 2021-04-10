# Challenge: Labyrevnt (Rev)

You find yourself at a labyrinth. Can you find the way through it?

nc labyrevnt-01.play.midnightsunctf.se 29285 

Downloaded files: chall

# Solution
There is a walk\_start and walk\_end function.
Our goal is to give the right character commands to get to the walk\_end function.
When we reach walk\_end, the binary prints flag.txt.
There are too many functions so we can script Radare2 to reverse it.

The script [reverse.py](reverse.py) finds a path from walk\_start to walk\_end and then finds the characters that will take us in that route.

```sh
python reverse.py
./chall < solution
```

# Flag
```
midnight{y0u_w3r3_l05t_f0r_4_wh1l3_bu7_y0u_f1n411y_g0t_0ut}
```
