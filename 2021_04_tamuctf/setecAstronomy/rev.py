given_out = [1,1,0,0,1,0,1,0,0,1,1,0,1,1,1,0,1,1,0,0,1,1,0,0,0,1,0,1,1,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,0,0,0,0,0,1,1,0,0,0,1,1,1,0,1,1,0,1,1,1,1,1,0,0,0,0,1,1,1,1,0,1,0,0,0,1,0,0,0,1,0,0,1,1,0,0,0,0,0,1,1,1,0,0,1,0,0,1,0,0,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,1]

first_part = slice(0,32)
second_part = slice(32,64)
third_part = slice(64,96)
fourth_part = slice(96,128)

def rReverse(in_arr):
    in_arr.reverse()
    return in_arr

def rConcat(in_arr):
    return (in_arr[first_part], in_arr[second_part], in_arr[third_part], in_arr[fourth_part])

def rXOR(in1, in2):
    # Assumes both array have the same length
    out = []
    for i in range(len(in1)):
        out.append(in1[i] ^ in2[i])
    return out

def rSwitch(in_arr, index1, index2, length):
    for index in range(length):
        temp = in_arr[index1 + index]
        in_arr[index1 + index] = in_arr[index2 + index]
        in_arr[index2 + index] = temp
    return in_arr

#Reverse(in=phoenix, out=out);
phoenix = rReverse(given_out)

#Concat(a=abbott, b=comso, c=ayk[0..31], d=earl, out=phoenix);
(abbott, cosmo, ayk_first_part, earl) = rConcat(phoenix)

#Xor(a=ayk[0..31], b=ayk[64..95], out=earl);
ayk_third_part = rXOR(ayk_first_part, earl)

#Xor(a=ayk[64..95], b=ayk[96..127], out=cosmo);
ayk_fourth_part = rXOR(ayk_third_part, cosmo)

#Xor(a=ayk[32..63], b=ayk[96..127], out=abbott);
ayk_second_part = rXOR(ayk_fourth_part, abbott)

ayk = [0 for i in range(128)]
for i in range(len(ayk_first_part)):
    ayk[i] = ayk_first_part[i]
for i in range(len(ayk_second_part)):
    ayk[i+32] = ayk_second_part[i]
for i in range(len(ayk_third_part)):
    ayk[i+64] = ayk_third_part[i]
for i in range(len(ayk_fourth_part)):
    ayk[i+96] = ayk_fourth_part[i]

#Switch(a=ayk[3..6], b=ayk[19..22]);
ayk = rSwitch(ayk, 3, 19, 4)

#Switch(a=ayk[54..61], b=ayk[32..39]);
ayk = rSwitch(ayk, 54, 32, 8)

#Switch(a=ayk[63..70], b=ayk[120..127]);
ayk = rSwitch(ayk, 63, 120, 8)

#Switch(a=ayk[95..98], b=ayk[81..84]);
ayk = rSwitch(ayk, 95, 81, 4)

#Concat(a=in[0..31], b=dave, c=red, d=king, out=ayk);
(input_first_part, dave, red, king) = rConcat(ayk)

#Xor(a=in[0..31], b=in[96..127], out=red);
input_fourth_part = rXOR(input_first_part, red)

#Xor(a=in[64..95], b=in[96..127], out=dave);
input_third_part = rXOR(input_fourth_part, dave)

#Xor(a=in[32..63], b=in[64..95], out=king);
input_second_part = rXOR(input_third_part, king)

input = [0 for i in range(128)]
for i in range(len(input_first_part)):
    input[i] = input_first_part[i]
for i in range(len(input_second_part)):
    input[i+32] = input_second_part[i]
for i in range(len(input_third_part)):
    input[i+64] = input_third_part[i]
for i in range(len(input_fourth_part)):
    input[i+96] = input_fourth_part[i]

for i in range(16):
    j = i * 8
    binary = 0
    for k in range(8):
        binary = binary << 1
        binary += input[j+k]
    print(chr(binary), end="")
