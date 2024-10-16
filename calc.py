def calc(line):
    ''' функция принимает на вход строчку, состоящую из слов,
    которые обозначают цифры, или числа, или математические операции, или доп символы (скобки)
    функция возвращает результат математического выражения в виде слов'''
    line = line.strip()

    #убираю лишние пробелы и создаю словарь

    book = {'один' : '1' , 'два' : '2', 'три' : '3', 'четыре' : '4', 'пять' : '5', 'шесть' : '6',
'семь' : '7', 'восемь' : '8', 'девять' : '9', 'десять' : '10', 'одиннадцать' : '11',
'двенадцать' : '12', 'тринадцать' : '13', 'четырнадцать' : '14', 'пятнадцать' : '15', 'шестнадцать' : '16',
'семнадцать' : '17', 'восемнадцать' : '18', 'девятнадцать' : '19', 'двадцать' : '20',
'тридцать' : '30', 'сорок' : '40', 'пятьдесят' : '50', 'шестьдесят' : '60', 'семьдесят' : '70',
'восемьдесят' : '80', 'девяносто' : '90', 'минус' : '-', 'плюс' : '+', 'умножить' : '*', 'на' : '',
'открывается' : '(', 'закрывается' : ')', 'скобка' : '', 'сто' : '100', 'двести' : '200', 'триста' : '300',
'четыреста' : '400', 'пятьсот' : '500', 'шестьсот' : '600', 'семьсот' : '700', 'восемьсот' : '800',
'девятьсот' : '900', 'одна тысяча' : '1000', 'две тысячи' : '2000', 'три тысячи' : '3000',
'четыре тысячи' : '4000', 'пять тысяч' : '5000', 'шесть тысяч' : '6000', 'семь тысяч' : '7000',
'восемь тысяч' : '8000', 'девять тысяч' : '9000', 'ноль' : '0'}

    #создаю список, где каждый элемент - это слово из выражения
    #потом посимвольно перевожу строку в математический вид с помощью словаря
    listline = line.split(' ')
    result = ''
    if line =='':
        return 'Попробуйте снова'
    for part in range(0, len(listline)):
        if listline[part] in book:
            if book[listline[part]].isnumeric():
                if part > 0 and book[listline[part-1]].isnumeric():
                    pass
                elif part != (len(listline) - 1):
                    if listline[part + 1] in book:
                        if book[listline[part + 1]].isnumeric():
                            result += str(int(book[listline[part]]) + int(book[listline[part+1]]))
                        else:
                            result += book[listline[part]]
                    else:
                        return 'Неверный ввод'
                else:
                    result += book[listline[part]]
            else:
                result += book[listline[part]]
        else:
            return 'Попробуйте снова'

    #создаю второй словарь, который является перевернутой версией исходного,
    #чтобы перевести математический результат в число
    invbook = {v: k for k, v in book.items()}
    #print(eval(result))
    #получаю результат выражения с помощью eval()
    if result.count('(') != result.count(')'):
        return 'Не то кол-во скобок'
    intresult = eval(result)
    strresult = str(intresult)
    total = ''

    #убираю у отрицательных чисел минус и вношу его в итоговый результат
    if intresult < 0:
        total += 'минус '
        strresult = strresult[1:]
        intresult = int(strresult)

    #поскольку числа [11;19] являются самостоятельными словами, рассматриваю их отдельно, как и ноль
    if 11 <= intresult <= 19 or intresult == 0:
        total += invbook[strresult]
    else:
        #delit - делитель, с помощью которого я дроблю число 9801 на 9000 800 1 (пример)
        delit = '1' + '0' * len(strresult)
        for i in range(len(strresult)):
            if int(str(intresult % int(delit) - intresult % int(delit[:-1]))) != 0 and not(11 <= int(str(intresult % int(delit))) <= 19):
                total += invbook[str(intresult % int(delit) - intresult % int(delit[:-1]))] + ' '
            elif 11 <= int(str(intresult % int(delit))) <= 19:
                total += invbook[str(intresult % int(delit))]
                break
            delit = delit[:-1]
    return total
print('''Пожалуйста, введите строковое выражение для калькулятора. 
Вы можете использовать числа до девяносто девяти, скобки,
операции вычитания, сложения и умножения.''')
numeric = input()
print(calc(numeric))
