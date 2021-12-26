def kontrol(kullanici,parola):
    if kullanici =="admin" and parola =="123456":
        return True
    else:
        return False

while True:
    kullanici_=input("Kullanıcı Adınızı Giriniz:")
    parola_=input("Parolanızı Yazınız:")
    sonuc= kontrol(kullanici_,parola_)
    if sonuc==True:
        print("Giriş Başarıyla Yapıldı.")
        break
    else:
        print("Kullanıcı Adı veya Parolanız Yanlış.")