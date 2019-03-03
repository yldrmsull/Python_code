import random
import string
user=[]
kontrol=0
print(" -----------------------------------------------------------olusturulan sifreler------------------------------------------------------------------------")
for i in range(1,101):
    harf = [random.choice(string.ascii_letters) for _ in range(5)]
    rakam = [random.choice(string.digits) for _ in range(2)]
    noktalama = [random.choice(string.punctuation) for _ in range(1)]
    sifre = harf + rakam + noktalama
    random.shuffle(sifre)
    sifre = ''.join(sifre)
    user.append(sifre)
    print(sifre)
print("-----------------------------------------------------------eklenen sifreler-----------------------------------------------------------------------------")
for i in range(0,100):
    print(user[i])



for i in range(0,100):
      for j in range(10,999):
            if user[i].count(j) == 1:
                print(user[i],"şifresi hatalıdır!!!")
            else:
                break









