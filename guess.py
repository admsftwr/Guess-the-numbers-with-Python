import random
randomNumber = random.randrange(0,100)
print(randomNumber)
print("Sayı tahmin yarışmasına hoş geldiniz!")
health = float(input("Kaç canınız olmasını istersiniz?:"))
starthealth=health
userNumberInput = 0
i = 1
while i < health:
    userNumberInput = int(input("Aklınızdaki sayıyı giriniz:"))
    health -= 1
    if userNumberInput != randomNumber:
        print("Tahmininiz doğru değil!")
        if userNumberInput < randomNumber:
            print("Yukarı!")
        else:
            print("Aşağı!")
    else:
        print("Tahmininiz doğru! Tebrikler!")
        print("Puanınız:",(health/starthealth)*100)
        break
    i += 1

