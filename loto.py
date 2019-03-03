import random
from msilib import sequence
list1=[]
tahminlistesi=[]
tutansayı=0
for i in range(0,6):
    tahminlistesi.append(random.randrange(1,50))

for i in range(0,6):
    tahmin = int(input("sayı giriniz"))
    list1.append(tahmin)
for i in range(0,6):
    if(tahminlistesi[i]==list1[i]):
        tutansayı=tutansayı+1
print (tutansayı)





