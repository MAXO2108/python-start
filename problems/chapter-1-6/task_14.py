x, y = int(input()), int(input())
x1, y1 = y, x + y
print("Одновременно:", x1, y1)
x = y 
y = x + y
print("По очереди:", x, y) 
