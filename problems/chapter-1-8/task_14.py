flat_nom = int(input())
flats = int(input())
floors = int(input())
kv_pad = flats * floors
nom_pad = (flat_nom - 1) // kv_pad + 1
ost = (flat_nom - 1) % kv_pad
floor = ost // flats + 1
print(nom_pad, floor)

