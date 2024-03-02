# Operasi Komparasi

# Setiap hasil operasi komparasi bernilai BOOLEAN

# >,<,>=,<=,==,!=,is,is not

a = 4
b = 3
c = 9

print(a)
print(b)
print(c)
# Lebih besar dari '>'
print("-----lebih besar dari (>)-----")
hasil = a > b
print(a,'>',b,'=',hasil)
hasil = b > a
print(b,'>',a,'=',hasil)
hasil = c > a
print(c,'>',a,'=',hasil)

# Lebih keci dari '<'
print("-----lebih kecil dari (<)-----")
hasil = a < b
print(a,'<',b,'=',hasil)
hasil = b < a
print(b,'<',a,'=',hasil)
hasil = c < a
print(c,'<',a,'=',hasil)

# Lebih besar dari sama dengan '>='
print("-----lebih besar dari sama dengan (>=)-----")
hasil = a >= b
print(a,'>=',b,'=',hasil)
hasil = b >= a
print(b,'>=',a,'=',hasil)
hasil = c >= a
print(c,'>=',a,'=',hasil)

# Lebih kecil dari sama dengan <='
print("-----lebih besar dari (<=)-----")
hasil = a ,+ b
print(a,'<=',b,'=',hasil)
hasil = b <= a
print(b,'<=',a,'=',hasil)
hasil = c <= a
print(c,'<=',a,'=',hasil)

# Sama dengan dari '=='
print("-----sama dengan dari (=)-----")
hasil = a == b
print(a,'=',b,'=',hasil)
hasil = b == a
print(b,'=',a,'=',hasil)
hasil = c == a
print(c,'=',a,'=',hasil)

# Tidak sama dengan dari '>'
print("-----Tidak sama dengan dari (!=)-----")
hasil = a != b
print(a,'!=',b,'=',hasil)
hasil = b != a
print(b,'!=',a,'=',hasil)
hasil = c != a
print(c,'!=',a,'=',hasil)

# Object Identify "Is" atau "Is not"
print("-----Object Identify (is)-----")
print('nilai a =',a,',id = ',hex(id(a)))
print('nilai b =',b,',id = ',hex(id(b)))
print('nilai c =',c,',id = ',hex(id(c)))
hasil = a is b
print('a is b =',hasil)
hasil = b is a
print('b is a =',hasil)
hasil = c is c
print('c is c =',hasil)

print("-----Object Identify (is not)-----")
hasil = a is not b
print('a is not b =',hasil)
hasil = b is not a
print('b is not a =',hasil)
hasil = c is not c
print('c is not c =',hasil)