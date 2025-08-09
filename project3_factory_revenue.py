# Project 3 - Zavodlar daromadi hisoblash
# Author: Yorqinoy
# Description: Ishlab chiqarish va mahsulot narxlariga asoslangan daromad hisoblash.

import numpy as np

# Ishlab chiqarish matritsasi (zavod x mahsulot)
ishlab_chiq = np.array([
    [500, 300, 250],  # Zavod 1
    [450, 400, 300],  # Zavod 2
    [600, 350, 200]   # Zavod 3
])

# Har bir mahsulotning narxi (so‘mda)
narxlar = np.array([10000, 15000, 20000])

# Daromad = ishlab chiqarish * narxlar
daromad = ishlab_chiq @ narxlar

# Natijalar
print("Ishlab chiqarish jadvali:\n", ishlab_chiq)
print("Mahsulot narxlari:", narxlar)
print("Har bir zavod daromadi:", daromad)
print("Jami daromad:", np.sum(daromad))
