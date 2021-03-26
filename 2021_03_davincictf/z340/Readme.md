# Solution
This challenge gave an image that contains text that was encrypted with the Zodiac z340 cipher.
The text of the image is present as ciphertext in diag.py.

diag.py reads the cipher text in a diagonal fashion.
decrypt.sh will use the substituitions used by the Zodiac killer to decrypt it.

In the plaintext obtained, we can see that in multiple places D is present in the place of L.
So I changed the D in the password to L.

# Flag
```
dvCTF{monailooveyousomuch}
```
