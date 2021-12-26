def cevre(kisa,uzun)
    print("Dörtgeninizin Çevresi:", (uzun+kisa)*2)
def alan(kisa,uzun)
    print("Dörtgeninizin Alanı:", uzun * kisa)
print("Dörtgen Hesaplama Programına Hoşgeldiniz")
secenek=input("""1-Eğer Çevre Ölçmek İstiyorsanız: çevre
2-Eğer Alan Ölçmek istiyorsanız: alan
Yazınız:""").lower()
uzun_=int(input("Lütfen Uzun Kenarı Giriniz:"))
kisa_=int(input("Lütfen Kısa Kenarı Giriniz:"))
if secenek == "çevre":
    cevre(kisa_, uzun_)
elif secenek == "alan":
    alan(kisa_,uzun_)
else:
    print("Lütfen Çevre Ya da Alan Yazınız")