import etlap
import rendeles
from rendeles import rendelesek_indexe_lista
from etlap import *
etlap.etl()
etlap.item(levesek,"levesek",levesar)
etlap.item(foetel,"Főételek",foetelar)
etlap.item(itallap,"Italok",italar)
etlap.item(desszertek,"Desszertek",desszertar)
rendeles.rendeles(levesek,"levesek",levesar)
rendeles.rendeles(foetel,"Főételek",foetelar)
rendeles.rendeles(itallap,"italok",italar)
rendeles.ossz()