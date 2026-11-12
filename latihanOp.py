#Operator
#Operator Aritmatika
a = 10
b = 2
c = 3

penjumlahan = a + b + c
pengurangan = a - b 
sisabagi = a % c
perkalian = a * b * c
pembagian = a // b
perpangkatan = a ** b
pembagian_bulat = a / b
print(f"Hasil Penjumlahan {a} + {b} + {c} = {penjumlahan}")
print(f"Hasil Pengurangan {a} - {b} = {pengurangan}")
print(f"Sisa bagi {a} mod {c} = {sisabagi}")
print(f"Hasil Perkalian {a} * {b} * {c} = {perkalian}")
print(f"Hasil Pembagian {a} / {b} = {pembagian}")
print(f"Hasil Perpangkatan {a} ** {b} = {perpangkatan}")
print(f"Hasil Pembagian_bulat {a} // {b} = {pembagian_bulat}")

#Operator Assignment

a += 2 #12 a = 10 + 2
a **= 2 #144 a = 12 ** 2
print(a)

#Operator Perbandingan
perbandingan = a >= b #144 >= 2 True

x = 3
y = 2
banding = x <= y #false


print(x != y) 
print(perbandingan)

#Operator Logika AND
opAnd = a >= b and x <= y and x != y
opOR = perbandingan or banding or x != y
opNOT = not opOR
print(opAnd)
print(opOR)
print(opNOT)