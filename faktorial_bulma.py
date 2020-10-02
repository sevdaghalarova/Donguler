"""
Cikmak icin q-e basin
"""
while True:
    sayi=input("sayi: ")
    if sayi=="q":
        break
    else:
        sayi=int(sayi)
        faktoriel=1
        for i in range(2,sayi+1):
            faktoriel*=i
        print(faktoriel)
