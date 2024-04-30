def convert_to_hex(rgb):
    r, g, b = rgb
    hex_value = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return hex_value

rgb_tuple = (255, 0, 0)
hex_color = convert_to_hex(rgb_tuple)
print("HEX:", hex_color.upper())

rgb_tuple = (0, 255, 0)
hex_color = convert_to_hex(rgb_tuple)
print("HEX:", hex_color.upper())

rgb_tuple = (0, 0, 255)
hex_color = convert_to_hex(rgb_tuple)
print("HEX:", hex_color.upper())


#Задача 2: Преобразование RGB в HEX
#Описание:

#В дизайн-студии Романа часто работают с цветами. 
#Цвета в компьютерной графике часто представляются в RGB формате, который состоит из трех чисел: красного (R), зеленого (G) и синего (B). 
#Каждый из этих чисел может принимать значения от 0 до 255. 
#Напишите функцию `convert_to_hex`, которая принимает на вход кортеж из трёх чисел (R, G, B) и возвращает цвет в HEX формате.