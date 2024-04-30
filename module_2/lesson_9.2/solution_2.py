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