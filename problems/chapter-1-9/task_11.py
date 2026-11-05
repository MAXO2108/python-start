rubls = int(input())
curs = float(input())
comiss = float(input())
rub_comiss = comiss / 100 * rubls
p_comiss = (rubls - rub_comiss) / curs 
print(f"Комиссия: {rub_comiss:.2f} руб.")
print(f"Получите: {p_comiss:.2f}")
