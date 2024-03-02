# Latihan konversi temperature

# Program Konversi celcius ke satuan lain

print("\nPOGRAM KONVERSI TEMPERATURE\n")

celcius = float(input('Masukkan suhu dalam satuan celcius : '))
print("Suhu adalah ",celcius,"Derajat Celcius")

#reamur
reamur = (4/5) * celcius
print("Suhu dalan Reamur adalah ",reamur,"Derajat Reamur")

#fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit adalah ",fahrenheit,"Derajat Fahrenheit")

#kelvin
kelvin = celcius + 273
print("Suhu dalma Kelvin adalah ",kelvin,"Derajat Kelvin")


print("\n----TUGAS KONVERSI KELVIN KE FAHRENHEIT DAN SEBALIKNYA----\n")
k = float(input('Masukkan nilai suhu dalam satuan kelvin : '))
f = ((9/5) * (k-273) + 32)
print("Suhu adalah ",f,"Derajat Fahrenheit")

f = float(input('Masukkan suhu dalam satuan fahrenheit : '))
k = ((5/9) * (f-32) + 273)
print("Suhu adalah ",k,"Derajat Kelvin")