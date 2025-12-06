from api import tabela
def decode_hidden_name(tabela):
    letters = []

    for i, num in enumerate(tabela):
        if i % 21 == 19:
            last = num % 100
            if 1 <= last <= 26:
                letters.append(chr(last + 64))


    return "".join(letters)

