eggs = int(input())
per_box = int(input())
boxes = eggs // per_box 
ost = eggs % per_box
print(f"Полных коробок: {boxes}")
print(f"Осталось яиц: {ost}")