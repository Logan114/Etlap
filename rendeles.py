import etlap
from etlap import *

rendelesek_indexe_lista = []
menu_elemek_lista = [levesek, foetel, itallap ,desszertek]
menu_ar_lista = [levesar, foetelar, italar, desszertar]

def rendeles(etel,cim,etelar):
    print("\n\n")
    etlap.item(etel,cim,etelar)
    rendeles1: int = int(input(f"Írd be hányas számú {cim}t kéred!(0 ha semmit) "))
    rendelesek_indexe_lista.append(rendeles1)

def ossz():
    etlap.keret(meret,karakter)
    etlap.szoveg_kiiras("*","ÖSSZEGZÉS","*",50)
    etlap.keret(meret, karakter)
    n = 0
    while n < len(menu_elemek_lista):
        n += 1
        etlap.etel_kiiras("*",,"*",50,(menu_elemek_lista[(rendelesek_indexe_lista[n])]))

    ''''
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
    '''''

