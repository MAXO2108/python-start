today = int(input())
n = int(input())
full_days = (today + n) % 7 
print(f"Номер дня: {full_days}")
