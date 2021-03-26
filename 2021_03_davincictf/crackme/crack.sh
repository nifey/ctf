echo "Cracking the following md5 hash will give you the flag"
echo -n "d2862c3379cbf547d317b3b1771a4fb6" | sed 's/\(..\)/\1\n/g' | sed '/^$/d' | tac | tr '\n' ',' | sed 's/,//g'

echo "Final flag"
./crackme 741852963
