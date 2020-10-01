# break-- bir dongu icerisinde break kullanirsak, dongu sona erir
i=0
while i<5:
    if i==3:
        break
    print(i)
    i+=1

for i in range(1,100):
    if i==30:
        break
    #print(i)

# While True yaziyorsak islemde bir break ifadesi olmasi gerek

# Contiue kodu yazildiginda geri kalan kod calismiyor, dongu basa donuyor
i=0
while i<10:
    if i==3 or i==5: # 1 3 ve 5 oldugunda kodu durdur dongunun basina don
        i+=1 # bunu yapmazsak sonsuz donguye girer
        continue
    print(i)
    i+=1
