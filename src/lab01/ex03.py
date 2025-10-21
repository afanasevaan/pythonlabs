p = float(input())
d = float(input())
v = float(input())
base = p * (1 - d/100)
v_amount = base * (v/100)
total = base + v_amount
print(F'База после скидки:{'%.2f'%base}')
print(F'НДС:{'%.2f'%v_amount}')
print(F'Итого к оплате:{'%.2f'%total}')