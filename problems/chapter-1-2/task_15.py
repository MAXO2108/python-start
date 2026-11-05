now_hours = int(input())
now_minutes = int(input())
now = now_hours * 60 + now_minutes
end = 11 * 60 + 30
answer = end - now
print(f"До конца пары: {answer // 60} ч {answer % 60} мин")