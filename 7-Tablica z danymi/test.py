from user import decode_hidden_name
from tabela import tabela

def decode(tabel):
    letters = []

    for i, num in enumerate(tabel):
        if i % 21 == 19:
            last = num % 100
            if 1 <= last <= 26:
                letters.append(chr(last + 64))
            elif 27 <= last <= 52:       # a–z
                letters.append(chr(last - 27 + 97))
            elif last == 0 or last == 53:  # spacja
                letters.append(" ")

    return "".join(letters)


def test():
    try:
        answer = decode(tabela)
        user_answer = decode_hidden_name(tabela)

        if answer == user_answer:
            print(f"Wygląda na to że osoba ukryta w raporcie to {answer}.\n"
                  f"Ciekawe czy faktycznie miała cos dotczynienia z tym błędem.")
            return True
        else:
            print("Hmmm wygląda na to że to nie o to nam chodziło")
            return False
    except:
        print("Hmmm wygląda na to że to nie o to nam chodziło")
        return False


test()