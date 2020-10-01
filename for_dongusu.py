# 'in' --> bir elemanin liste,demet,sozluk vs icinde olup olmadigini kontrol eder
liste=[1,2,3,4]
print(5 in liste) # 5'in listede olup olmadigini kontrol ediyor


# for dongusu
for eleman in liste: # eleman yerine a,b...x yazilabiblir
    print(eleman) # burada eleman, her dongude tek tek listedeki elemanlara esit olacaktir

# cift rakamlari bulma orneyi
liste1=[1,3,4,2,7,44,3,22,43,66,12,34]
for cift in liste1:
    if cift%2==0: # eger elemanlarin 2'e bolunmesinden kalan 0 ise
        print(cift)

# sozluk uzerinde for dongusu
# sozluk.key sozluk.value sozluk.items
dictionary={"bir":1,"iki":2,"uc":3}
for key in dictionary.keys(): # sozlukde keylerin uzerinde dolas
    print(key)

for value in dictionary.values(): # value'lerin uzerinde dolas
    print(value)

for i,j in dictionary.items(): # hem key hem value degerleri uzerinde dolasacagi icin i,j yazdik
    print(i,j)