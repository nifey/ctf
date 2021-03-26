cat ascii | sed 's/\(.\{5\}\)/\1\n/g' | sed '1d' | head -n8 | tac | sed 's/.$//' | tr '\n' ',' | sed 's/,//g'
