def can_gears_rotate(num_gears):
    return num_gears % 2 == 0

num_gears = int(input("Введите количество шестеренок в механизме: "))
if can_gears_rotate(num_gears):
    print("Шестеренки могут вращаться.")
else:
    print("Шестеренки не могут вращаться.")