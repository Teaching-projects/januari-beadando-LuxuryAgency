
"""A program kiszámítja egy ház szobáinak kifestéséhez szükséges festék mennyiségét és annak árát"""

def muvelet1():
     szobak.append(round(float(szobakmeretenyers[0])*float(szobakmeretenyers[1]))+float(szobakmeretenyers[0])**2),2
    
def muvelet2():
    szobak.append(round(float(szobakmeretenyers[0])*float(szobakmeretenyers[1])+(2*(float(szobakmeretenyers[0])*float(szobakmeretenyers[2])))+(2*(float(szobakmeretenyers[1])*float(szobakmeretenyers[2]))),1))
     
     
szobakmerete=input("Add meg a szobák adatait(6x3 ,6x3x6):").split(",")
szobak=[]  

for i in szobakmerete:
    szobakmeretenyers = i.split("x")
    
    if len(szobakmeretenyers) == 2:
        muvelet1()
    else:
        muvelet2()

liter = float(sum(szobak)) /8.33
litervegleges = round(liter,2)


színárak = [2000,2200,2400,2600,2800]
Árak= []

for szamlalas in range(len(szobakmeretenyers)-1):
    
    print("Milyen színűre szeretnéd a(z)",(szamlalas+1),".  szobát? Fekete:2000ft/l (0) ,Barna:2200ft/l (1),Kék:2400ft/l (2),Zöld:2600ft/l (3),Fehér:2800ft/l (4). A színek sorszámával válaszolj!")
    s3 = int(input())
    ár = round((szobak[szamlalas]/8.33),1)*színárak[s3]
    Árak.append(ár)
    szamlalas+=1

print((sum(szobak)),"Négyzetméter a felület   ",litervegleges,"l   festékre van szükség, amely összege",(sum(Árak)),"ft  lesz")