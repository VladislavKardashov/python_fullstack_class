def bracket_balance(symbol_str):
    opens_list = []
    bracket_dict = {"[": "]", "(": ")", "{": "}"}

    for symbol in symbol_str: 
        if symbol in bracket_dict.keys():
            opens_list.append(symbol)
        else: 
            if not opens_list:
                return False
            last_bracket = opens_list.pop()
            if bracket_dict[last_bracket] != symbol:
                return False

    return len(opens_list) == 0

print(bracket_balance("[{[]}]"))  # T
print(bracket_balance("[{}]}"))    # F
print(bracket_balance("{[{(})]}"))  # F
print(bracket_balance("[{(){}}]"))  # T


#Задание 3. 
#Напишите функцию bracket_balance(), которая принимает в качестве аргумента строку.Предполагаем, что строка всегда состоит из символов из набора “{([])}”.

#Задача функции – проверить, что всем открывающим скобкам есть соответствующие закрывающие, и вернуть True или False. 
#Причем ситуации с нарушениями вроде “[(])” тоже должны считаться ошибочными и возвращать False.
#Не забудьте протестировать случаи в духе “}”, “[][” и “)(” (все должны вернуть False).
#Подсказка: вам может помочь список и операции .append() и .pop()