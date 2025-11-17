## Лабораторная работа 1

### Задание 1

```
name = input('Имя:' )
age = int(input('Возраст:'))
next_age = age + 1
print(F"Привет, {name}! Через год тебе будет {next_age}")
```

![im01.png](/images/lab01/im01.png)

### Задание 2

```
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
```
![im02.png](/images/lab01/im02.png)

### Задание 3

```
p = float(input())
d = float(input())
v = float(input())
base = p * (1 - d/100)
v_amount = base * (v/100)
total = base + v_amount
print(F'База после скидки:{'%.2f'%base}')
print(F'НДС:{'%.2f'%v_amount}')
print(F'Итого к оплате:{'%.2f'%total}')
```

![im03.png](/images/lab01/im03.png)

### Задание 4

```
m = int(input('Минуты:'))
hour = m // 60
minutes = m % 60
print(F'{hour}:{minutes:02d}')
```

![im04.png](/images/lab01/im04.png)

### Задание 5

```
fn= input('ФИО:').split()
init = [i[0] for i in fn]
print(F'Инициалы: {''.join(init)}.')
print(F'Длина (символов): {len(''.join(fn))+2}')
```

![im06.png](/images/lab01/im06.png)