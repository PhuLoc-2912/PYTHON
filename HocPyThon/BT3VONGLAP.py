#1

'''
n = int(input("Nhập vào số nguyên n: "))

while n > 0:
    print(n)
    n -= 1
'''
#2
'''
x = int(input("Nhập một số: "))

if x < 2:
    print(x, "không phải là số nguyên tố")
else:
    songuyento = True
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            songuyento = False
            break
    
    if songuyento:
        print(x, "là số nguyên tố")
    else:
        print(x, "không phải là số nguyên tố")
'''


#3
'''
n = int(input("Nhập n: "))
x = float(input("Nhập x: "))

ketqua = 0
for i in range(n + 1):
    ketqua += ((x*x + x + 1)**i + (x**2 - x + 1)**i)

print(f"A = ({x}^2 + {x} + 1)^{n} + ({x}^2 - {x} + 1)^{n} = {ketqua}")
'''

#4
'''
n = int(input("Nhập n: "))

A = 0
B = 0
C = 1
D = 1
E = 0

for i in range(1, n + 1):
    if i % 2 == 1:  # kiểm tra số lẻ
        A += i
    else:  # kiểm tra số chẵn
        B += i
    
    C *= i
    
    if i % 3 == 0:  # kiểm tra số chia hết cho 3
        D *= i
    
    is_prime = True
    for j in range(2, int(i**0.5) + 1):  # kiểm tra số nguyên tố
        if i % j == 0:
            is_prime = False
            break
    if is_prime and i > 1:
        E += i

print("A =", A)
print("B =", B)
print("C =", C)
print("D =", D)
print("E =", E)
'''



