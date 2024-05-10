#Merhaba
import random

numbers = random.randint(1,10)
#1'den 10'a kadar sayıları rastgele döndüren bir fonksiyonu değişkene atadık.

while True:
    try:
        user_Guess = int(input("Please make a guess.(1 to 10)"))
        user_Guess = int(user_Guess)

        if 1<= user_Guess <=10:
            print("Number: ", numbers)
            if user_Guess == numbers:
                print("Congratulations, your guess is correct!")
            elif user_Guess > numbers:
                print("Bad luck, your guess is bigger than random number!" )
            else:
                print("Bad luck, your guess is smaller than random number!")
        else:
            print("The number your entered is not between 1 and 10")
        #Bu if yapısı ile sayının 1 ile 10 arasında olup olmadığını kullanıcıya bildirdik.
        #İçerideki if yapısı ile de tahminin doğruluğu hakkında kullanıcıya sonuç verdik.

    except ValueError:
        print("Please enter valid integer.")


#Burada kullanıcıdan 1 ile 10 arasında tam sayı tahmini yapmasını istedik.
#While döngüsü ile girilen sayının 1 ile 10 arasında olup olmadığını kontrol ettik.
#try-except bloğu ile girilen ifadenin bir tam sayı olup olmadığını kontrol ettik.


