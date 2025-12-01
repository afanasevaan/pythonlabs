fn = input("Введите ФИО: ").split()  # Исправлено fm -> fn
init = [i[0] for i in fn]

print(f'Инициалы: {".".join(init)}.')

full_name = "".join(fn)
print(f"Длина (сложить): {len(full_name)}")
