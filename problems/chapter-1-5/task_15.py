litr = int(input())
raschod = float(input())
pyti = float(input())
zapas = litr / raschod * 100
total_x = pyti - zapas
print(f"Хватит на: {zapas:.2f} км")
print(f"Останется проехать: {total_x:.2f} км")
