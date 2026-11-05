price = int(input())
months = int(input())
full_price = round(price / months, 2)
total_price = full_price * months 
raz_price = price - total_price 
print(f"Платёж: {full_price} руб.")
print(f"Выплачено: {total_price:.2f} руб.")
print(f"Разница с ценой: {raz_price:.2f} руб.")
