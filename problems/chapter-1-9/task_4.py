old_price = int(input())
new_price = int(input())
discount = (1 - new_price / old_price) * 100
print(f"Скидка: {discount:.1f}%")
