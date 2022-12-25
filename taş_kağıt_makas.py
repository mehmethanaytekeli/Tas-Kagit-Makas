
print("""Taş Kağıt Makas Oyunu
************************************""")


import random

while True :

    liste =  ['taş','kağıt','makas']

    a = input("Hamle Yapın :")

    rastgeledeger = random.choice(liste)

    print("Botun Hamlesi:{}".format(rastgeledeger))



    if rastgeledeger == a :
         print(("Berabere !"))
    elif rastgeledeger == "taş" and a == "kağıt" :
         print("Kazandınız !")
    elif rastgeledeger == "kağıt" and a == "Makas" :
         print("Kazandınız !")
    elif rastgeledeger == "makas" and a == "taş" :
         print("Kazandınız !")
    else :
         print("Mağlup Oldunuz !")











