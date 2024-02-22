#first = input("Kelime ")   String değerinin o kısımdaki kelimesini gösterir
#print(first[1])

#second = input("Yaz") Bu kısım hangi kısımdan başlayacağını belirtiyor
#print(second[8:])     [Başlama, Bitiş ,Ortalama]
#print(second[:8])
#print(second[8:15])

#uzunluk = "Merhaba"
#print(len(uzunluk))    Girilen metnin ne kadar uzunlukta olduğu gösterir (len)

#print(uzunluk + " Batuhan") Pythonda direkt string değiştirilemez ama yeni bir string oluşturulabilir

#Eğer bir değer girersek bu değer string olarak alınır ve bunu int float gibi değerlere dönüştürmek zorunda kalırız
#firstint = "3"
#print(firstint*4) #burada firstint den 4 kere basarken aşağı kısımda cevap 6 cıkıyor
#print(int(firstint)+3)
#print(float(firstint)/1.25)
#firstint2 = str("3.14")
#print(firstint2)
#print(len(firstint2)) #noktada karakter olarak alınır

#print(7,4,2002, "Batuhanın doğum günüdür.")
#print("Batuhan\tCan\n742002 Doğumludur") #n aşağı indirir t tab kadar boşluk bıraktırır.
#print(type(34))
#print(type("Batuhan"))
#print(len("Batuhan"))
#print(7,4,2002,sep="/") # Sep burada boşluk yerine ne geleceğini söyler
#print(*"Batuhan") #Yıldız keliemeler arasında boşluk yaratır
#print(*"Batuhan",sep=".")

#Formatlama
#print("{},{},{}".format(7,4,2002))
#print("{:.2f},{:.2f},{:.3f}".format(3.1463,1.2345,1.23456))
#print("{2},{1},{0}".format(3,2,1))

#Pyformat sayfasında tüm özellikler var oradan bakılır

liste = ["Batu", 2, "Elma Yedi"]
print(type(liste))
print(len(liste))
print(liste[0])

liste = list("BATUHAN")
print(liste)
print(len(liste))
print(list)