


def str_operation(word: str, operation: str) -> str:
    oper_dict = {
        'lower': lambda w: w.lower(),
        'upper': lambda w: w.upper(),
        'reverse': lambda w: w[::-1],
        'len': lambda w: str(len(w))

    }
    oper_func = oper_dict.get(operation, lambda w: "Unknown operation")
    return oper_func(word)

word = input("Enter word: ")
operation = input("Enter operation name (lower, upper, len, reverse): ")

print(str_operation(word, operation))
