# Лабораторная работа 1
## №1
```python
a = input('')
b = int(input(''))
c = b + 1
print('Имя:', a)
print('Возраст:',b)
print('Привет,',a,'! Через год тебе будет', c, '.')
```
![](images/lab01/номер_1.png "номер_1")

## №2
```python
a = input("a: ").replace(',', '.')
b = input("b: ").replace(',', '.')
c = float(a)
d = float(b)
sum_result = c + d
avg_result = (c + d) / 2
print(f"sum={sum_result:.2f}; avg={avg_result:.2f}")
```
![](images/lab01/номер_2.png "номер_2")

## №3
```python
price = int(input())
discount = int(input())
vat = int(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print('База после скидки:',base)
print('НДС',vat_amount)
print('Итого к оплате:',total)
```
![](images/lab01/номер_3.png "номер_3")

## №4
```python
a = int(input('Минуты:'))
b = a//60
c = a % 60
print(b,':',c)
```
![](images/lab01/номер_4.png "номер_4")

## №5
```python
a = input("ФИО: ").strip()
b = ' '.join(a.split())
c = ''.join(word[0].upper() for word in b.split())
d = len(b)
print("Инициалы:",c)
print("Длина (символов):",d)
```
![](images/lab01/номер_5.png "номер_5")
