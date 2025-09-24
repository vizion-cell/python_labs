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