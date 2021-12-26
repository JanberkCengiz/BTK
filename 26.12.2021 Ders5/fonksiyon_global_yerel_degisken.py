b=20 #global değişkendir çünkü  bir yere bağlı değildir heryerde kullanılabilir.

def fonksiyon():
    global b #dışarıdaki global bir değişkeni fonksiyon içine dahilmiş gibi yapar ve o değişkeni yönetebilir.

    a=10 #burada a yerel değişkendir çünkü fonksiyonun içinde fonksiyona bağlıdır.

    b=4
# print(a) #a değişkeni yerel (bağlı) olduğu için a'yı tek başına yazdıramayız. ama eğer b değişkenini yazarsan kod hata vermez.
fonksiyon()
print(b) #eğer global b yapmasaydık b değşikenine dokunamayacağı için b 20 olarak kalırdı.