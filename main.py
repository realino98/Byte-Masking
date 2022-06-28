a = 0xf3 # 11110011
print(bin(a))

#MSB -> 11110011 starts from the LEFT
for bit in range(8):
    if (a & 0x80): #1000000
        print(1)
    else:
        print(0)
    a<<=1

#LSB 11110011 <- starts from the RIGHT
for bit in range(8): 
    if (a & 0x01): #0000001
        print(1)
    else:
        print(0)
    a>>=1