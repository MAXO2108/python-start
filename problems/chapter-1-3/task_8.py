visitors = int(input())
orders = int(input())
conversion = orders / visitors * 100
print("Отчет за день")
print()
print(f"Посетителей: {visitors}")
print(f"Заказов: {orders}")
print(f"Конверсия: {conversion:.2f}%")