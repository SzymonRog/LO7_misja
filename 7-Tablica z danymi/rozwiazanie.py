from api import data_table
def decode_hidden_name(table):
    letters = []

    for i, num in enumerate(data_table):
        if i % 21 == 19:
            last = num % 100
            if 1 <= last <= 26:
                letters.append(chr(last + 64))

    return "".join(letters)