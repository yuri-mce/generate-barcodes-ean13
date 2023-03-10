from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox


def getFilename():
    filename = askopenfilename()
    fileName.configure(text=filename)


def BtnClick():
    if numb_start.get() == "":
        messagebox.showinfo("Предупреждение","Не указано начало диапазона штрихкодов")
        return
    else:
        numb_start_int = int(numb_start.get())

    if numb_finish.get() == "" and numb_barcodes.get() == "":
        messagebox.showinfo("Предупреждение","Не указано ни количество штрихкодов, ни конец диапазона")
        return
    elif numb_finish.get() == "":
        numb_finish_int = numb_start_int + int(numb_barcodes.get())
    else:
        numb_finish_int = int(numb_finish.get())

    if prefix.get() == "" or len(prefix.get()) != 2:
        messagebox.showinfo("Предупреждение", "Не указан префикс штрихкодов, либо неверная его длина (префикс состоит из двух цифр)")
        return

    if fileName.cget("text") == "":
        messagebox.showinfo("Предупреждение", "Не указан файл для вывода штрихкодов")
        return

    file_for_output = open(fileName.cget("text"), "w")
    counter = numb_start_int
    while counter <= numb_finish_int:
        code12 = add_numbers_to_code(prefix.get(), counter)
        control_number = barcode_control_number(odd_numbers_summa(code12), even_numbers_summa(code12))
        code13 = code12 + str(control_number)
        counter += 1
        file_for_output.write(code13 + '\n')
    file_for_output.close()
    return

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
            summa += int(chars[count - 1])
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
            summa += int(chars[count - 1])
        count += 1
    return summa

    # Добавление лидирующих нулей после префикса до нужной длины штрихкода


def add_numbers_to_code(barcode_prefix, number):
    number = str(number)
    length = 12 - len(barcode_prefix)
    while len(number) < length:
        number = "0" + number
    return barcode_prefix + number


if __name__ == '__main__':

    window = Tk()
    window.geometry('400x240')
    window.title("Генератор штрихкодов EAN-13")

    header1 = Label(window, text="Введите начало и конец диапазона штрихкодов")
    header1.grid(column=0, row=0, sticky=W, padx=(10, 0), pady=(10, 0))

    header2 = Label(window, text="для генерации их в указанный файл")
    header2.grid(column=0, row=1, sticky=W, padx=(10, 0), pady=(0, 10))


    numb_start_txt = Label(window, text="Начало диапазона штрихкодов:")
    numb_start_txt.grid(column=0, row=2, sticky=W, padx=(10, 0))

    numb_start = Entry(window, width=10)
    numb_start.grid(column=1, row=2, sticky=W)
    numb_start.focus()


    numb_finish_txt = Label(window, text="Конец диапазона штрихкодов:")
    numb_finish_txt.grid(column=0, row=3, sticky=W, padx=(10, 0))

    numb_finish = Entry(window, width=10)
    numb_finish.grid(column=1, row=3, sticky=W)

    numb_barcodes_txt = Label(window, text="Количество штрихкодов:")
    numb_barcodes_txt.grid(column=0, row=4, sticky=W, padx=(10, 0))

    numb_barcodes = Entry(window, width=10)
    numb_barcodes.grid(column=1, row=4, sticky=W)

    prefix_txt = Label(window, text="Префикс штрихкода:")
    prefix_txt.grid(column=0, row=5, sticky=W, padx=(10, 0))

    prefix = Entry(window, width=2)
    prefix.grid(column=1, row=5, sticky=W)


    btnFilename = Button(window, text="Выбрать файл", command=getFilename)
    btnFilename.grid(column=1, row=6, sticky=W, pady=(10, 0) )

    fileName = Label(window, text="")
    fileName.grid(column=0, row=6, sticky=W, padx=(10, 0))

    btn = Button(window, text="Сгенерировать", command=BtnClick)
    btn.grid(column=1, row=7, sticky=W, pady=(5, 0))

    window.mainloop()



