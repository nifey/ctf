ciphertext = ['<EV>UpjM8^WGR@;pC' ,'O4+|;:M+7#6@^c5pc' ,'+P8bM+-T6zcp|%T2c' ,'RCb>UN8zR35dz<#+A' ,'4<.MY&MbB5F<B7-6+' ,'6Oj&O@S2pNXHFD%4c' ,'.Sj9Kp<Up*ObVYqL+' ,'(HLM4pU/6R@tXbqL9' ,'tH^-49V3UVM2^7fBO']

x=0
y=0
i=0

while i < 154:
    print (ciphertext[y][x], end="")
    x = (x + 2) % 17
    y = (y + 1) % 9
    i = i + 1
