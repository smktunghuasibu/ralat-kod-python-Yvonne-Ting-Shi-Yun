# Atur cara mengira luas permukaan kon.
# Betulkan ralat dalam kod Python ini.

import math
pi = 3.142

def dapat_jejari_tinggi():
    a = float(input("Masukkan jejari: "))
    b = float(input("Masukkan tinggi: "))
    return (a, b)

def kira_luas_permukaan_kon(r, h):
    luas_permukaan_kon = (pi * r) * (r + math.sqrt(r**2+ h**2))
    return round(luas_permukaan_kon, 2)

def main_cone():
    (x, y) = dapat_jejari_tinggi()
    luas_permukaan_kon = kira_luas_permukaan_kon(x, y)
    print(f"luas permukaan kon = {luas_permukaan_kon:.2f}")

# JANGAN ubah kod di bawah baris ini!
if __name__ == "__main__":
    main_cone()
