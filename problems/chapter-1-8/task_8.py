peoples = int(input())
mest = int(input())
bus = peoples // mest
ost = peoples % mest 
if ost > 0: 
    full_bus = bus + 1
print(f"Полных автобусов: {bus}")
print(f"Не поместились в полные: {ost}")
print(f"Нужно заказать: {full_bus}")
