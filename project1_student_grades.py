# Project 1 - Talabalar baholari statistikasi
# Author: Yorqinoy
# Description: 50 ta talabaga random baho beriladi va statistik tahlil qilinadi.

import numpy as np

# 50 ta talabaga random baho (0-100 oralig‘ida)
baholar = np.random.randint(0, 101, 50)

# Statistik qiymatlar
ortalama = np.mean(baholar)
median = np.median(baholar)
eng_kam = np.min(baholar)
eng_kop = np.max(baholar)
std_dev = np.std(baholar)

# Natijalar
print("Baholar:", baholar)
print("O'rtacha:", ortalama)
print("Median:", median)
print("Eng kichik:", eng_kam)
print("Eng katta:", eng_kop)
print("Standart og'ish:", std_dev)
