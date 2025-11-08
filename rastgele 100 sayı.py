


import statistics 
rastgeleSayilar=[45,70,49,40,55,70,63,57,65,80,82,85,68,50,48,78,72,83,42,87,60,65,69,52,75,64,48,52,68,43,90,63,95,78,80,55,75,85,60,41]


      

toplam = sum(rastgeleSayilar)
print(f"Sayıların Toplamı:{toplam}")

aritmetikOrt = toplam/25
print(f"Aritmetik Ortalama:{aritmetikOrt}")

mod = statistics.mode(rastgeleSayilar)
print(f"Mod:{mod}")

medyan = statistics.median(rastgeleSayilar)
print(f"Medyan:{medyan}")

standartSapma = statistics.stdev(rastgeleSayilar)
print(f"Standart Sapma:{standartSapma}")

minimumDeğer = min(rastgeleSayilar)
maksimumDeğer = max(rastgeleSayilar)

print(f"Minimum Değer:{minimumDeğer}")
print(f"Maksimum Değer:{maksimumDeğer}")

rastgeleSayilar.sort(reverse=True)
print(rastgeleSayilar)