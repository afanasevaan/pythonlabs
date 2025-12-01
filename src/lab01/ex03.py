p = float(input())
d = float(input())
v = float(input())
base = p * (1 - d / 100)
v_amount = base * (v / 100)
total = base + v_amount

print(f"База после скидки: {base:.2f}")
print(f"НДС: {v_amount:.2f}")
print(f"Итого к оплате: {total:.2f}")
