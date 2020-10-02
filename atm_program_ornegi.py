"""

ATM hosgeldiniz
1. Bakiye sorgulama
2. Para Yatirma
3. Para Cekme

Cikis yapmak icin q-e basin
"""
bakiye=500
while True:
    islem=input("Bir islem secin:  ")
    if islem=="q":
        print("Yine bekleriz...")
        break
    elif islem=="1":
        print("bakiyeniz {} tl'dir".format(bakiye))
    elif islem=="2":
        miktar=int(input("Ne kadar para yatirmak istiyorsunuz? : "))
        bakiye+=miktar
        print("yeni bakiyeniz: ", bakiye)
    elif islem=="3":
        miktar=int(input("Ne kadar para cekmek istiyorsunuz? : "))
        if bakiye-miktar<0:
            print("Bakiyeniz yetersiz..")
            continue
        bakiye-=miktar
