a = 0xf3 # 11110011
print("Source :", bin(a))

#MSB -> 11110011 starts from the LEFT
print("MSB ", end="")
for bit in range(8):
    if (a & 0x80): #1000000
        print(1, end="")
    else:
        print(0, end="")
    a<<=1

a = 0xf3 # 11110011
print()
print("Source :", bin(a))
#LSB 11110011 <- starts from the RIGHT
print("LSB ", end="")
for bit in range(8): 
    if (a & 0x01): #0000001
        print(1, end="")
    else:
        print(0, end="")
    a>>=1