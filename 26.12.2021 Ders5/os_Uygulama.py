import os


def klasor_(x):
    for i in range(x):
        os.mkdir("denemeler"+str(i))
sayi= int(input("Kaç Klasör Oluşturulsun? :"))
klasor_(sayi)