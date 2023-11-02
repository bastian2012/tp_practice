# enonse 1 Nan yon chenn karaktè, mete tout karaktè yo an miniskil.

chenn="BasTiEn Jean RITCHY"
miniskil=(chenn.lower())


# enonse 2 Nan yon chenn karaktè, koupe chenn nan tout kote ki gen espas. Epi afiche yon lis ki gen chak eleman yo. Ekzanp:

b=miniskil.split(" ")

# enonse 3 Nan yon chenn karaktè, mete tout premye lèt chak mo an majiskil.

tab=[]
for i in b:
    tab.append(i.capitalize())


# enonse 4 Nan yon chenn karaktè, rekipere premye lèt chak mo. Epi afiche yon nouvo chenn ak tout inisyal sa yo.

chenn2=""
for i in b:
    chenn2+=(i[0])

# enonse 5 Ranplase tout karaktè "a" ki nan yon chenn pa "@"
nom="Bastien"
nom2=nom.replace("a", "@")

# enonse 6 Mete yon chenn karaktè devan dèyè, answit mete l an majiskil. Ekzanp:

i=len(nom)-1
devan_dèyè=""
while i>=0 :
    devan_dèyè+=nom[i]
    i-=1
devan_dèyè=devan_dèyè.upper()

# enonse 7 Afiche endeks premye karaktè "a" ki nan yon chenn. Ekzanp:
indeks=nom.index("a")

# enonse 8 Afiche total tout endeks karaktè "a" ki nan yon chenn (Kit se a majiskil oubyen miniskil). Ekzanp:

varyab="Ayiti kapab avanse"
conter=0
compteur=0
for i in varyab:
    if i.lower() =="a":
        conter+=compteur
    compteur+=1


# enonse 9 Kreye yon lis ki gen endeks tout karaktè "a" ki nan yon chenn (Sèlman a miniskil). Ekzanp:
var2=[]
cpt=0
for i in varyab:
    if i =="a":
        var2.append(cpt)
    cpt+=1

# enonse 10 Retire tout espas ki nan yon chenn, epi kole chenn sa ak kantite karaktè li genyen (Pa kontwole espas yo).
el=""
var3=varyab.split(" ")
for i in var3:
    el+=i
el+=str(len(el))