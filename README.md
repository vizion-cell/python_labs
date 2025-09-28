# python_labs
## Лабораторная работа 1

### Задание 1
```python
name = (input("Имя: "))
age = int(input("Возраст: "))
print (f"Привет, {name}! Через год тебе будет {age+1}.")
```
![Картинка 1](./images/lab01/001.png)

### Задание 2
```python
number1 = float(input("a: ").replace(",", "."))
number2 = float(input("b: ").replace(",", "."))
print(f"sum={number1 + number2}; avg={round(((number1 + number2) / 2),2)}")
```
![Картинка 2](./images/lab01/002.png)# python_labs

### Задание 3
```python
price = 1000
discount = 10
vat = 20
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f"База после скидки: {format(base,'.2f')}")
print(f'НДС: {format(vat_amount,'.2f')}')
print(f"Итого к оплате: {format(total,".2f")}")
```
![Картинка 3](./images/lab01/003.png)# python_labs

### Задание 4
```python
minn = int(input("Минуты: "))
hours = (minn // 60) % 24
minn_time = (minn % 60)
if minn_time < 10:
    minn_time = "0" + str(minn_time)
print(f"{hours}:{minn_time}")
```
![Картинка 4](./images/lab01/004.png)# python_labs

### Задание 5
```python
fio= input("фио: ")
countt = 0
while '  ' in fio:
    fio = fio.replace('  ', ' ')
words = fio.split()
fio_w_2spases = fio.rstrip().lstrip()
first_letters = []
str_first_letters = ''
for word in words:
    first_letters.append(word[0])
for letter in first_letters:
    str_first_letters +=  letter
print(f"Инициалы: {str_first_letters}")
print(f"Длина (символов): {len(fio_w_2spases)}")
```
![Картинка 5](./images/lab01/005.png)# python_labs
