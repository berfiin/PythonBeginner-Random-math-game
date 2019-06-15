
# 1 numara toplama,2çıkarma,3çarpma,4faktöriyel
import random
import time
import math

skor = 0

while True:
    a=random.randint(1,4)

    print("lütfen bekleyin yeni soru hazırlanıyor...")
    time.sleep(2)

    if a == 1:
        print("toplama işlemi->")
        ilksayi = random.randint(1,20)
        ikincisayi = random.randint(1,20)
        print("lütfen", ilksayi ,"ile",ikincisayi,"sayılarının toplamını giriniz")
        sonuc = int(input("cevap:"))

        if(sonuc == ilksayi+ikincisayi):
            print("tebrikler doğru bildiniz")
            skor = skor+1
            print("mevcut skorunuz:",skor)
            time.sleep(2)
        else:
            print("yanlış! doğru cevap:", ilksayi+ikincisayi)
            skor = skor-3
            print("mevcut skorunuz:", skor)
            time.sleep(2)
    elif a == 2:
        print("çıkarma işlemi->")
        ilksayi=random.randint(1,20)
        ikincisayi=random.randint(1,20)
        print("lütfen",ilksayi,"-",ikincisayi,"işlemin sonucunu giriniz")
        sonuc = int(input("cevap:"))

        if(sonuc == ilksayi-ikincisayi):
            print("tabrikler doğru bildiniz")
            skor = skor + 1
            print("mevcut skorunuz:", skor)
            time.sleep(2)
        else:
            print("yanlıs! doğru  cevap",ilksayi-ikincisayi)
            skor = skor - 3
            print("mevcut skorunuz:", skor)
            time.sleep(2)
    elif a == 3:
        print("çarpma işlemi->")
        ilksayi = random.randint(1, 10)
        ikincisayi = random.randint(1, 10)
        print("lütfen", ilksayi, "x", ikincisayi, "işlemin sonucunu giriniz")
        sonuc = int(input("cevap:"))

        if (sonuc == ilksayi * ikincisayi):
            print("tabrikler doğru bildiniz")
            skor = skor + 1
            print("mevcut skorunuz:", skor)
            time.sleep(2)
        else:
            print("yanlıs! doğru  cevap", ilksayi * ikincisayi)
            skor = skor - 3
            print("mevcut skorunuz:", skor)
            time.sleep(2)
    elif a == 4:
        print("faktoriyel işlemi ->")
        ilksayi = random.randint(1,5)
        print("lütfen",ilksayi,"sayısının faktöiyelini hesaplayınız")
        sonuc=int(input("cevap:"))

        if(sonuc == math.factorial(ilksayi)):
            print("tebrikler doğru bildiniz")
            skor = skor + 1
            print("mevcut skorunuz:", skor)
            time.sleep(2)

        else:
            print("yanlış! doğru cevap:",math.factorial(ilksayi))
            skor = skor - 3
            print("mevcut skorunuz:", skor)
            time.sleep(2)