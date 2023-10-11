import etlap
from etlap import *

levesek = ["0 - Nem kér semmit", "1 - Húsleves", "2 - Gyümölcsleves", "3 - Bableves"]
levesar = [0,880,600,1200]
foetel = ["0 - Nem kér semmit", "1 - Tojásos nokedli", "2 - Rántott hús rizibizivel", "3 - Rántott hús sült krumplival"]
foetelar = [0,880,1500,2000]
itallap = ["0 - Nem kér semmit", "1 - Coca Cola", "2 - Kőbányai", "3 - Márka szörp"]
italar = [0,450,450,350]
desszertek = ["0 - Nem kér semmit", "1 - Tiramisu", "2 - Nutellás palacsinta", "3 - Túrós palacsinta"]
desszertar = [0,650,750,250]


def levren():
    print("\n\n")
    etlap.lev()
    term = "leves"
    rendeles1: int = int(input(f"Írd be hányas számú {term}t kéred!(0 ha semmit)"))
    global leves
    leves = levesek[rendeles1]
    global levar
    levar = levesar[rendeles1]
    print(f"{leves} - {levar} Ft")

def foren():
    print("\n\n")
    etlap.foet()
    term = "főétel"
    rendeles2: int = int(input(f"Írd be hányas számú {term}t kéred!(0 ha semmit)"))
    global foet
    foet = foetel[rendeles2]
    global foetar
    foetar = foetelar[rendeles2]
    print(f"{foet} - {foetar} Ft")

def itren():
    print("\n\n")
    etlap.drink()
    term = "ital"
    rendeles3: int = int(input(f"Írd be hányas számú {term}t kéred!(0 ha semmit)"))
    global ital
    ital = itallap[rendeles3]
    global itar
    itar = italar[rendeles3]
    print(f"{ital} - {itar} Ft")

def deszren():
    print("\n\n")
    etlap.dessert()
    term = "desszert"
    rendeles4: int = int(input(f"Írd be hányas számú {term}et kéred!(0 ha semmit)"))
    global desz
    desz = desszertek[rendeles4]
    global desszert_ar
    desszert_ar = desszertar[rendeles4]
    print("Válasszon levest! (0-tol 3-ig válasszon)")
    print(f"{desz} - {desszert_ar} Ft")

def ossz():
    etlap.keret(meret,karakter)
    etlap.szoveg_kiiras("*","ÖSSZEGZÉS","*",50)
    etlap.keret(meret, karakter)
    etlap.etel_kiiras("*",leves,"*",50,levar)
    etlap.keret(meret, karakter)
    etlap.etel_kiiras("*",foet,"*",50,foetar)
    etlap.keret(meret, karakter)
    etlap.etel_kiiras("*",ital,"*",50,itar)
    etlap.keret(meret, karakter)
    etlap.etel_kiiras("*",desz,"*",50,desszert_ar)
    etlap.keret(meret, karakter)
    veg =(levar+foetar+itar+desszert_ar)
    etlap.etel_kiiras("*", "Végösszeg","*",50,veg)
    etlap.keret(meret, karakter)

