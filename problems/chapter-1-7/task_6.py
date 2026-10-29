ves = int(input())
rost = float(input())
index = ves / rost ** 2
norm = index >= 25
print(f"ИМТ: {index}")
print(f"Выше нормы: {norm}")
