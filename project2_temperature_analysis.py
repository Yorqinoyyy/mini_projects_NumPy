# Project 2 - Harorat tahlili
# Author: Yorqinoy
# Description: 30 kunlik haroratlar o‘rtacha qiymati va yuqori kunlar tahlili.

import numpy as np

# 30 kunlik harorat (15°C dan 35°C gacha random float)
haroratlar = np.random.uniform(15, 35, 30)

# O‘rtacha harorat
orta_harorat = np.mean(haroratlar)

# Yuqori haroratli kunlar
yuqori_kunlar = haroratlar[haroratlar > orta_harorat]
kun_soni = np.sum(haroratlar > orta_harorat)

# Natijalar
print("30 kunlik haroratlar:", haroratlar)
print("O'rtacha harorat:", orta_harorat)
print("O'rtachadan yuqori bo'lgan kunlar:", yuqori_kunlar)
print("Bunday kunlar soni:", kun_soni)
