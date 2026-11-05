distance = int(input())
fuel = float(input())
price = float(input())
total_fuel = distance * fuel / 100
total_price = total_fuel * price 
print(f"Топлива: {total_fuel:.2f} л")
print(f"Стоимость: {total_price:.2f} руб.")