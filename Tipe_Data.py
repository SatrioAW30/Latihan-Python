# 1.) Integer (Int) = merupakan bilangan bulat
print("=====INTEGER======")
data_integer = 11
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

data_float = float(data_integer)
data_str   = str(data_integer)
data_bool  = bool(data_integer) # statement akan berubah menjadi FALSE jika nilai int = 0
print("Data Integer di atas berubah menjadi", data_float, "yang bertipe", type(data_float))
print("Data Integer di atas berubah menjadi", data_str, "yang bertipe", type(data_str))
print("Data Integer di atas berubah menjadi", data_bool, "yang bertipe", type(data_bool))

# 2.) Float = merupakan tipe data dengan koma 
print("=====FLOAT=====")
data_float = 3.5
print("data : ", data_float)
print("- bertipe : ", type(data_float))

data_int   = int(data_float)
data_str   = str(data_float)
data_bool  = bool(data_float) # statement akan berubah menjadi FALSE jika nilai int = 0
print("Data Float di atas berubah menjadi", data_int, "yang bertipe", type(data_int))
print("Data Float di atas berubah menjadi", data_str, "yang bertipe", type(data_str))
print("Data Float di atas berubah menjadi", data_bool, "yang bertipe", type(data_bool))

# 3.) String = merupakan kumpulan dari karakter
print("====STRING====")
data_string = "30"
print("data : ", data_string)
print("- bertipe : ", type(data_string))

data_int   = int(data_string)
data_float = float(data_string)
data_bool  = bool(data_string) # Statement akan berubah menjadi FALSE apabila nilai dalam String = (NULL)
print("Data String di atas berubah menjadi", data_int, "yang bertipe", type(data_int))
print("Data String di atas berubah menjadi", data_float, "yang bertipe", type(data_float))
print("Data String di atas berubah menjadi", data_bool, "yang bertipe", type(data_bool))

# 4.) Boolean = merupakan tipe data yang bernilai True/False
print("=====BOOLEAN======")
data_bool = True
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))

data_int    = int(data_bool)
data_str    = str(data_bool)
data_float  = float(data_bool) 
print("Data Boolean di atas berubah menjadi", data_int, "yang bertipe", type(data_int))
print("Data Boolean di atas berubah menjadi", data_str, "yang bertipe", type(data_str))
print("Data Boolean di atas berubah menjadi", data_float, "yang bertipe", type(data_float))

## Tipe Data Khusus

# Bilangan Kompleks
data_complex = complex(3,4)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

# Ctypes = tipe data dari bahasa C

from ctypes import c_double
data_c_double = c_double(9.5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))


# CASTING TIPE DATA 
