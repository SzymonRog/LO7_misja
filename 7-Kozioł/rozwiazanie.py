from tabela import tabela
def decode_hidden_name(tabela):
    letters = []

    for i, num in enumerate(tabela):
        if i % 21 == 19:
            last = num % 100
            if 1 <= last <= 26:
                letters.append(chr(last + 64))
            elif 27 <= last <= 52:       # a–z
                letters.append(chr(last - 27 + 97))
            elif last == 0 or last == 53:  # spacja
                letters.append(" ")

    return "".join(letters)




