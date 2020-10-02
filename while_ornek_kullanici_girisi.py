"""
Kullanici girisi

"""
sys_kullanici="sevda"
sys_sifre="123456"
giris=3
while True:
    kullanici=input("Kullanici isminiz: ")
    sifre=input("Sifre: ")
    if sys_kullanici!=kullanici:
        print("Kullanici ismi yalnis...")
        giris-=1
    elif sys_sifre!=sifre:
        print("Sifre yalnis..")
        giris-=1
    else:
        print("Giris basarili..")
        break
    if giris==0:
        "Giris hakiniz bitti.."