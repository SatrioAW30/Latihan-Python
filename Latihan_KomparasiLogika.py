# ----- 0 ++++++ 5 ------ 8 +++++++ 11 ------
# hasil bernilai TRUE Jika angka tersebut lebih besar dari 0 dan kurang dari 5 atau lebih besar dari 8 dan kurang dari 11 
inputUser = float(input("Masukkan Angka: "))

rules1 = (inputUser > 0)
rules2 = (inputUser < 5)
rules3 = (inputUser > 8)
rules4 = (inputUser < 11)

hasil1 = rules1 and rules2
hasil2 = rules3 and rules4

jawaban = hasil1 or hasil2
print("Angka yang anda masukkan bernilai: ",jawaban)

# +++++ 0 ------ 5 ++++++ 8 ------- 11 ++++++
# Hasil bernilai TRUE jika angka tersebut kurang dari 0 atau lebih besar dari 5 dan kurang dari 8 atau lebih besar dari 11
inputUser = float(input("Masukkan Angka: "))

data1 = (inputUser < 1)
data2 = (inputUser > 5)
data3 = (inputUser < 8)
data4 = (inputUser > 11)

hasil1 = data1 or data2
hasil1 = data3 or data4

pernyataan = hasil1 and hasil2
print("Angka yang anda masukkan bernilai: ",pernyataan)