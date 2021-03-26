# Solution
The otp1.php file contains a large hex value which is obtained by XORing the flag with some random quotes.

It was mentioned that the quote text will consist of upper case alphabets only.

otp.py script will find all possible characters for each location that if XORed with the hex values gives 
an uppercase alphabet.

After some guessing, and checking with CyberChef, the flag was obtained.

# Flag
```
UDCTF{w3lc0me_t0_0ur_ctf}
```
