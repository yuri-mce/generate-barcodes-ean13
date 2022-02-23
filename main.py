from tkinter.filedialog import askopenfilename

# Функция вычисления контрольной цифры


def barcode_control_number(odd_summa, even_summa):
    all_summa = odd_summa * 3 + even_summa
    last_digit = str(all_summa)[-1]
    if last_digit != "0":
        return 10 - int(last_digit)
    else:
        return "0"

# Функция вычисления суммы нечетных цифр, начиная с конца


def odd_numbers_summa(number):
    summa = 0
    chars = [ch for ch in str(number)]
    chars.reverse()
    count = 1
    while count <= len(chars):
          if count % 2 != 0:
            summa += int(chars[count-1])
          count += 1
    return summa

# Функция вычисления суммы четных цифр, начиная с конца


def even_numbers_summa(number):
    summa = 0
    chars = [ch for ch in str(number)]
    chars.reverse()
    count = 1
    while count <= len(chars):
          if count % 2 == 0:
            summa += int(chars[count-1])
          count += 1
    return summa

# Добавление лидирующих нулей после префикса до нужной длины штрихкода


def add_numbers_to_code(barcode_prefix, number):
    number = str(number)
    length = 12-len(barcode_prefix)
    while len(number) < length:
        number = "0" + number
    return barcode_prefix + number


numb_start = int(input("Введите начало диапазона кодов:"))
numb_finish = int(input("Введите конец диапазона кодов:"))
prefix = input("Введите префикс штрихкода (двузначное число):")

filename = askopenfilename()
file_for_output = open(filename, "w")

counter = numb_start
while counter <= numb_finish:
    code12 = add_numbers_to_code(prefix, counter)
    control_number = barcode_control_number(odd_numbers_summa(code12), even_numbers_summa(code12))
    code13 = code12 + str(control_number)
    counter += 1
    file_for_output.write(code13+'\n')
file_for_output.close()




