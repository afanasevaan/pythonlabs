n1 = input("a:")
n2 = input("b:")
if ',' in n1:
    n1 = n1.replace(',','.')
if ',' in n2:
    n2 = n2.replace(',','.')
n1 = float(n1)
n2 = float(n2)
sumc= n1 + n2
avg = sumc/2
print(F'sum = {'%.2f'%sumc}; avg = {'%.2f'%avg}')