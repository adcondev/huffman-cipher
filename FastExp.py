C = 1
n = 3233
A = 2790
B = "110011101"
#B = "10001"
for bit in B:
    C = (C**2) % n
    if bit == "1":
        C = (C*A) % n
print(C)
