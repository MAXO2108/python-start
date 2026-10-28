salary = float(input())
tax = salary * 0.13
net = salary - tax 
day1 = net / 22
print(f"Налог: {tax:.2f} руб.")
print(f"На руки: {net:.2f} руб.")
print(f"За один день: {day1:.2f} руб.")