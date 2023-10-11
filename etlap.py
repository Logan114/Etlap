global meret
meret: int = int(50)
global karakter
karakter = "*"
levesek = ["0 - Nem kér semmit", "1 - Húsleves", "2 - Gyümölcsleves", "3 - Bableves"]
levesar = [0,880,600,1200]
foetel = ["0 - Nem kér semmit", "1 - Tojásos nokedli", "2 - Rántott hús rizibizivel", "3 - Rántott hús sült krumplival"]
foetelar = [0,880,1500,2000]
itallap = ["0 - Nem kér semmit", "1 - Coca Cola", "2 - Kőbányai", "3 - Márka szörp"]
italar = [0,450,450,350]
desszertek = ["0 - Nem kér semmit", "1 - Tiramisu", "2 - Nutellás palacsinta", "3 - Túrós palacsinta"]
desszertar = [0,650,750,250]
'''''
lev() Leves
foet() Főétel
drink() Itallap
dessert() Desszertek
'''''





def keret(meret,karakter):
    print(karakter*meret)
def szoveg_kiiras(jel, szoveg, jel2,nyugta_meret):
    hossz: int = int(nyugta_meret-(len(jel) + len(jel2)))
    print(f"{jel}{szoveg:^{hossz}}{jel2}")

def etel_kiiras(jel, szoveg, jel2,nyugta_meret,ar):
    hossz: int = int(nyugta_meret-(len(jel) + len(jel2)))
    behuzas = nyugta_meret-10
    arbehuzas = int(nyugta_meret/10)
    print(f"{jel}{szoveg:<{behuzas}}{ar:<{arbehuzas}}ft {jel2}")



def etl():
    keret(meret,karakter)
    szoveg_kiiras(karakter,"Étlap",karakter,meret)
    keret(meret,karakter)

def lev():
    szoveg_kiiras(karakter,"Levesek",karakter,meret)
    keret(meret,karakter)
    n = 0
    n2 = 0
    for leves in range (3):
        n = n+1
        n2 = n2+1
        leves = levesek[n]
        ar = levesar[n]
        etel_kiiras(karakter,leves,karakter,meret,ar)

def foet():
    keret(meret,karakter)
    szoveg_kiiras(karakter,"Főétel",karakter,meret)
    keret(meret,karakter)
    n = 0
    n2 = 0
    for leves in range (3):
        n = n+1
        n2 = n2+1
        fetel = foetel[n]
        ar = foetelar[n]
        etel_kiiras(karakter,fetel,karakter,meret,ar)



def drink():
    keret(meret,karakter)
    szoveg_kiiras(karakter,"Itallap",karakter,meret)
    keret(meret,karakter)
    n = 0
    n2 = 0
    for ital in range (3):
        n = n+1
        n2 = n2+1
        italok = itallap[n]
        ar = italar[n]
        etel_kiiras(karakter,italok,karakter,meret,ar)

def dessert():
    keret(meret,karakter)
    szoveg_kiiras(karakter,"Desszertek",karakter,meret)
    keret(meret,karakter)
    n = 0
    n2 = 0
    for ital in range (3):
        n = n+1
        n2 = n2+1
        desszert = desszertek[n]
        ar = desszertar[n]
        etel_kiiras(karakter,desszert,karakter,meret,ar)
    keret(meret,karakter)

etl()
lev()
foet()
drink()
dessert()