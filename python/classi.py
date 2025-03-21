from bottiglia import Bottiglia, BottigliaConTappo 

b = Bottiglia(500)
print(b.quantita)
print(b.capacita)
print(b)
b.riempi(1500)
print(b)
b.riempi(50)
print(b)
b.svuota(600)
print(b)

b2 = BottigliaConTappo(1500)
print(b2)
b2.chiudi()
print(b2)
b2.riempi(1500)
print(b2)