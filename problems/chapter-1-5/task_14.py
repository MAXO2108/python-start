size_film = float(input())
speed = int(input())
total_size = size_film * 1024 * 8
total_speeds = total_size / speed
total_speedm = total_speeds / 60
print(f"Загрузка займет: {total_speedm:.2f} мин")