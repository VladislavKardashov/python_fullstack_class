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