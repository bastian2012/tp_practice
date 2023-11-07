import string,random
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


# enonse 11 Kreye yon lis eleman ki divizib pa 2, nan entèval [0-n] enklizif
max=12
tab_div2=[]
for i in range(max+2):
    if i % 2 == 0:
        tab_div2.append(i)

# enonse 12 Ou gen yon lis antye, konvèti l an yon lis chenn.
tab_chèn=[]
for i in (tab_div2):
    tab_chèn.append(str(i))

# enonse 13 Ou gen yon lis chenn ki an miniskil, konvèti an yon lis chenn majiskil
lis_chèn_maj=[]
lis_chèn=["index 1", "index 2", "index 3", "index 4", "index 5"]
for i in lis_chèn:
    lis_chèn_maj.append(i.upper())


# enonse 14 Ou gen yon lis, kreye yon nouvo lis ki fèt ak eleman ki nan endèks ki divizib pa 3 yo sèlman
tab_div_3 =[]
for i in (lis_chèn):
    if (lis_chèn.index(i)%3 == 0):
        tab_div_3.append(str(i))

# enonse 15 Ou gen lis eleman, kreye yon nouvo lis ki gen chak 3 eleman yo gwoupe anndan yon tipl. Ekzanp:

for i in range(max):
    tab.append((i))
i=0
tab_tuple=[]
while i<len(tab):
    tab_tuple.append((tab[i],tab[i+1],tab[i+2]))
    i+=3
# print(tab_tuple)
# enonse 16 Ou gen yon lis, ki gen yon pakèt eleman ki repete. Konvèti l an yon lis, ki pa gen okenn doublon.
tb_no_repeat=[]
tb_repeat=[0, 2, 3,3,5,1,9,0,4,33,44,55]
for i in tb_repeat:
    if not  i in tb_no_repeat:
        tb_no_repeat.append(i)
# print(tb_repeat,tb_no_repeat)

# enonse 17  Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman komen ant 2 lis yo.
lis_1=[0, 2,23,34,45]
lis_inter=[]
for i in tb_repeat:
    if i in lis_1:
        if i not in lis_inter:
            lis_inter.append(i)
        
for i in lis_1:
    if i in tb_repeat:
        if i not in lis_inter:
            lis_inter.append(i)
# print(lis_inter)

# enonse 18 Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman distenge ant 2 lis yo.
lis_union = []
for i in tb_repeat:
    if i  in lis_1 or i in tb_repeat:
        if i not in lis_union:
            lis_union.append(i)
        
for i in lis_1:
    if i  in lis_1 or i in tb_repeat:
        if i not in lis_union:
            lis_union.append(i)

# enonse 19 Ou gen yon diksyonè. Kreye yon nouvo lis ak kle yo sèlman, epi yon lòt ak valè yo sèlman.

dic={"nom":"bastien","prenom":"ritchy"}
cle=list(dic.keys())
valeur=list(dic.values())

# enonse 20 Reyini 3 lis ansanm, san okenn doublon.
lis_no_doublon=[]
for i in lis_1:
    lis_no_doublon.append(i)
for j in tb_repeat :
    lis_no_doublon.append(j)
for j in lis_union :
    lis_no_doublon.append(j)
lis_3=(set(lis_no_doublon))

# enonse 21 Ou gen yon diksyonè. Rekipere tout valè yo, gras ak kle yo epi retounen yon lis valè.

tb=[]
for j in dic:
    tb.append(dic[j])
# print(tb)

# enonse 22 Mande itilizatè a, tape yon valè... epi verifye si l gen akolad devan ak dèyè.
entrer =""
# entrer=input("antrer yon bgy")
# entrer=entrer.strip()
# if entrer[0]=="{" and entrer[0]=='}':
#     print("li gn akolad devan ak dèyè")

# enonse 23 Pakouri yon diksyonè, epi afiche tout kle yo.

for i in dic:
    print(i)

# enonse 24 Pakouri yon diksyonè, epi afiche tout valè yo.

for i in dic:
    print(dic[i])
    
# enonse 25 Pakouri yon diksyonè, pou w kapab kreye yon kopi(nouvo) sou disksyonè sa.
dic_cp={}
for cle, valeur in dic.items():
    dic_cp[cle] = valeur


# enonse 26 Anndan yon diksyonè ki gen kle ak valè(valè yo ka nenpòt tip done). Ajoute yon underscore devan ak dèyè tout valè ki se chenn yo. Ekzanp:

dic1={"name": "Lub", "age": 14,"salaire":2000, "assets": ["laptop", "phone"]}
for i in dic1:
    if isinstance(dic1[i],str):
        dic1[i]=f"_{dic1[i]}_"
# print(dic1)
# enonse 27 Nan yon diksyonè ki gen valè ki se chenn sèlman. Kreye yon nouvo diksyonè ki gen tout eleman ki gen valè ki dijit yo sèlman. Ekzanp:
dicdigit={}
for key,value in dic1.items():
    if isinstance(value,int):
        dicdigit[key]=value
# print(dicdigit)

# enonse 28 Pakouri yon disksyonè, pou w mete l sou fòm lis, kote chak eleman nan disksyonè sa, vin sou fòm tipl(kle, valè) anndan lis la. Ekzanp:
lis=[]
for k,v in dic1.items():
    lis.append((k,v))
# print(lis)

# enonse 29 Pakouri yon lis tipl, pou w mete l sou fòm diksyonè. Ekzanp:
my_dic={}
a= [("a",1), ("b",2)]
for i in a:
    my_dic[i[0]] = i[1]
# print(my_dic)

# enonse 30 Kole 2 diksyonè ansanm pou fè youn, kote si gen eleman ki gen menm kle ap konkatene valè, swivan kondisyon sa yo:

dict1={"nom":'bastien',"prenom":"ritchy","age":22, "skils":["programmation","reseau","base de donnée"],"my_set":{1, 2, 3, 4, 5,7,6,8,9}}

dict2={"nom":'Saint-Louis',"prenom":"Pudens","age":22, "skils":["coatching","Comptabilité","Administration"],"my_set":{1, 2, 3, 4, 5,12,13,15,16,17,18}}

dict3={}
for k,v in dict1.items():
    if k in dict2:
        if isinstance(v,int) and isinstance(dict2[k],int):
            dict3[k]=int(v)+int(dict2[k])
        elif isinstance(v,str) and isinstance(dict2[k],str):
            dict3[k]=str(v)+","+str(dict2[k])
        elif isinstance(v,list) and isinstance(dict2[k],list):
            tp=[]
            dict3[k]=list(v)+list(dict2[k])
        elif isinstance(v,set) and isinstance(dict2[k],set):
            dict3[k]=set([i for i in v]+[j for j in dict2[k]])
print(dict3)




# enonse 31 kreye yon fonksyon ki ap pran yon paramèt yon mo, epi li retounen envès la.

def retounen_envès(param):
    tempon=""
    i=len(param)-1
    while i>=0:
        tempon+=param[i]
        i-=1
    # print(tempon)
# retounen_envès("bastien")

# enonse 32 kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik.
def kòd_aleyatwa(n):
    alphabet=string.ascii_letters
    kod="";i=n
    while i>0:
        nb=random.randint(0,len(alphabet)-1)
        kod+=alphabet[nb]
        i-=1
# kòd_aleyatwa(10)

# enonse 33 kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik, san repetisyon.
alphabet=string.ascii_letters
def kòd_no_repet(n):
    kod="";i=n
    while i>0:
        nb=random.randint(0,len(alphabet)-1)
        if not alphabet[nb] in kod:
            kod+=alphabet[nb]
            i-=1
# kòd_no_repet(6)

# enonse 34 kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alafanimerik, san repetisyon.
alpha_nimerik=alphabet
digit=string.digits
nb_digit=0
def kòd_no_repet_al_nim(n):
    kod=""
    i=round(n*0.70)
    j=round(n*0.25)
    while i>0:
        nb=random.randint(0,len(alpha_nimerik)-1)
        if not alpha_nimerik[nb] in kod:
            kod+=alpha_nimerik[nb]
            i-=1
    while j>0:
        nb=random.randint(0,len(digit)-1)
        if not digit[nb] in kod:
            kod+=digit[nb]
            j-=1
    # print(kod)
# kòd_no_repet_al_nim(25)

# enonse 35 Ou gen yon lis chenn. Jenere yon SLUG apati chenn nan. Nan yon SLUG, tout karaktè ki akseptab yo se: alfanimerik ak "-"
chèn="bastien se yon programè"
splt=chèn.split(" ")
bs='_'.join(splt)

# enonse 36 Kreye yon fonksyon ki ap separe chak lèt nan yon mo ak yon vigil
def separe_vigil(chenn):
    ch=[]
    for i in chenn:
        if not i ==" ":
            ch.append(i)
    a=",".join(ch)
    # print(a)
# separe_vigil("petit con")

# enonse 37 Kreye yon fonksyon ki ap kripte yon mo, avèk endèks li nan alfabè a. Chak karaktè dwe separe ak yon tirè.

mo='bastien'

def kripte(mo):
    tb_mo=[]
    for i in mo:
        tb_mo.append(str(alphabet.index(i)))
    rep="-".join(tb_mo)
    print(rep)
# kripte("Bastien")

# enonse 38 Kreye yon fonksyon ki ap dekripte yon mo ki fèt ak endèks chak lèt nan alfabè a, separe ak yon tirè.
krip="27-0-18-19-8-4-13"
def dekripter(krip):
    dkp=krip.split("-")
    mo=""
    for i in dkp:
        mo+=alphabet[int(i)]
    # print(mo)
# dekripter(krip)
# enonse 39 Kreye yon fonksyon ki ap pran 2 paramèt, epi ki pèmite valè yo. Answit li retounen tou 2 valè yo sou fòm Tuple.
def ma_fonction(param1,param2):
    tupl=(param2,param1)
    # print(tupl)
# ma_fonction("pierre","samuel")

# enonse 40 Kreye yon fonksyon ki ap pran yon non an paramèt, epi ki retounen inisyal yo. Atansyon ak non konpoze ak tirè yo.

nom="Jean-Ritchy-Bastien papa"
def return_initial(nom):
    nom2=nom.replace("-"," ")
    initial=""
    nom3=nom2.split(" ")
    for i in nom3:
        initial+=i[0].upper()
    print(initial)
# return_initial(nom)