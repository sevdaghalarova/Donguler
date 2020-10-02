# List Comrehension listeler uzerinde for dongusunu daha kisa yazmak icin kullanilir

liste=[1,2,3,4,5]
liste1=list()
for i in liste:
    liste1.append(i)
#print(liste1)

# yukaridaki kodu list comprehension ile yazarsak
liste1=[i for i in liste]

liste1=[i*2 for i in liste] # her bir elemani 2-3 carpip liste1-e ekleyecek
print(liste1)

liste3=[(1,2),(2,3),(2,4)]
liste4=[i for x in liste3 for i in x]
print(liste4)