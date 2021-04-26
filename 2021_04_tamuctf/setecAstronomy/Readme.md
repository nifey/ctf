# Challenge: setecAstronomy (rev)
After a top NSA scientist was found murdered, we searched his office and found a black box with the output still on the display. We have no idea what the code was, but we were able to find a schematic of the black box in his office and turn it into an HDL file. Figure out what the input was. You are alone on this. Remember: Trust No One.


Discovered Output
```
11001010011011101100110001011000111110101010111000001100011101101111100001111010001000100110000011100100100110001110000001111101
```

Downloaded files: [BlackBox.hdl](BlackBox.hdl) (HDL code)

Hint : Encryption Scheme: ISO-8859-1

# Solution

Reversing the concat, XOR and reverse modules were straight forward.
I only got confused with switch module.
Initially I ignored the switch and got a string that looked like valid ISO-8859-1 characters.
But it was not the right flag.

Then I figured out that the switch module is just swapping the values.
That gave the flag.

[rev.py](rev.py) is the script that reverses the BlackBox module.

# Flag
```
gigem{t0o_M4nY_s3cR3tS}
```
