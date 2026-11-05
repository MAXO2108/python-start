# Задачник, глава 1.1, задача 1.1.12 «Счёт за мобильную связь» (★★☆)
# Условие: https://python-theory-makarov.vercel.app/zadachnik/1-1/index.html#p12
#
# Счёт складывается из абонентской платы, оплаты дополнительных гигабайт и SMS. Даны абонентская
# плата, число дополнительных гигабайт и цена одного, число SMS и цена одной. Выведите каждую
# часть счёта и итог.
#
# Пример 1
#   данные:
#     subscription = 450
#     extra_gb = 3
#     gb_price = 120
#     sms = 10
#     sms_price = 2.5
#   вывод:
#     Абонентская плата: 450
#     Доп. интернет: 360
#     SMS: 25.0
#     Итого: 835.0
# Пример 2
#   данные:
#     subscription = 300
#     extra_gb = 0
#     gb_price = 150
#     sms = 4
#     sms_price = 3
#   вывод:
#     Абонентская плата: 300
#     Доп. интернет: 0
#     SMS: 12
#     Итого: 312

# Исходные данные (пример 1)
subscription = 450
extra_gb = 3
gb_price = 120
sms = 10
sms_price = 2.5

# Решение
dopinter = gb_price * extra_gb
sms_total = sms_price * sms
total = subscription + dopinter + sms_total
print(f"Абонентская плата: {subscription}")
print(f"Доп. Интернет: {dopinter}")
print(f"SMS: {sms_total}")
print(f"Итого: {total}")