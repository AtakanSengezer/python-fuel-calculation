benzinFiyat = 38.50
dizelFiyat = 40
toplamYakitUcreti = 0

ortalamaYakitTuketimi = float(input("100 km de ortalama yakıt tüketimi "))
gidilecekYol = float(input("Gidilecek Yol kaç km ?"))
yakitTipi = input("Yakıt Tipiniz nedir ?")

toplamYakitTuketimi = gidilecekYol * (ortalamaYakitTuketimi / 100)

if (yakitTipi == "benzin"):
    toplamYakitUcreti = benzinFiyat * toplamYakitTuketimi
elif(yakitTipi == "dizel"):
    toplamYakitUcreti = dizelFiyat * toplamYakitTuketimi
else: 
    print("Yanlış yakıt tipi girdiniz")

print(f" Toplam Yakıt Maliyeti {toplamYakitUcreti} ")