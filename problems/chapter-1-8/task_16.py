h = int(input())
m = int(input())
t = int(input())
v_min = h * 60 + m + t
h2 = v_min // 60 % 24
m2 = v_min % 60
print(f"{h2:02d}:{m2:02d}")
