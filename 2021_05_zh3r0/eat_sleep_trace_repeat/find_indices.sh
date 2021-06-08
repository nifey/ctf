#!/bin/bash
# 0x401122 corresponds to the compare instruction (cmp al, bl) that is repeatedly executed in each iteration
# 0x401126 is the instruction executed when the current iteration is done
cat trace.txt |\
	cut -d":" -f1 |\
	egrep "0x401122|0x401126" |\
	uniq -c |\
	grep -v 0x401126 |\
	sed 's/[\t ]*\(.*\) 0x401122/\1/' |\
	tr '\n' ',' |\
	sed 's/\(.*\),/[\1]/'
