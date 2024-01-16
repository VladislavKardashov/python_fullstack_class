old_price = "Design"
new_price = "Art"
replace_count = 2

aspect = input("Введите карточку товара: ")
new_aspect = aspect.replace(old_price, new_price, replace_count)

print(new_aspect)