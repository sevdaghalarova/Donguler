"""
while (kosul)
  islem
  islem
  islem.....

Kosul True oldugu surece bu dongu donecek, False oldugunda dongu sona eriyor
"""
i=0 # i degerimiz 0'dan baslasin
while i<10: # i 10-dan kucuk olacagi durumda dongu sona ersin
    print(i)
    i+=1 # i her dongude 1 artsin(yoksa sonsuz donguye girer)

# Listeler uzerinde while dongusu
liste=[1,2,3,4,5,6]
index=0 # index degerini 0'dan baslatiyoruz
while index<len(liste): # dongu liste uzunlugu kadar donsun
    print(index)
    index+=1 # her dongude index 1 artsin(yoksa sonsuz donguye girer)
