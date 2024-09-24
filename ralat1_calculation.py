# Atur cara mengira pembahagian dua nombor.
# Betulkan ralat dalam kod Python ini.

def calculation(a, b):    
    division = a / b
    return round(division, 2)

def get_input():
    x = int(input("Masukkan nombor integer pertama:"))
    y = int(input("Masukkan nombor integer kedua:"))
    return x, y

def main_calculation():
    (x, y) = get_input()
    divide = calculation(x, y)    
    print(f"Division = {divide}")

# JANGAN ubah kod di bawah baris ini!
if __name__ == "__main__":
    main_calculation()
