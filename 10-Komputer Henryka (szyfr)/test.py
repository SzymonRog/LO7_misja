
from decode_emails import decode_emails
from get_emails import get_emails
from agenda import agenda

def decode():
    emails = get_emails(['745', '234','128', '1024', '64'])
    text_emails = []

    for email in emails:
        decoded_text = ""
        tokens = email['body'].split(' ')

        for token in tokens:
            parts = token.split('.')  # [ARTYKUŁ, PUNKT, SŁOWO]
            article_id = parts[0]
            point_index = int(parts[1]) - 1
            word_index = int(parts[2]) - 1

            sentence = agenda[article_id][point_index]
            words = sentence.split(" ")
            decoded_text += " " + words[word_index]

        text_emails.append(decoded_text[1:])

    return text_emails


formated_emails = [
    """
    Zadanie priorytetowe. 
    Zmodyfikować system SmartVote plus. 
    Zmienić wyniki głosowania rady miejskiej na jutro. 
    Opcja druga musi wygrać. 
    Dostęp do pliku count votes. 
    Kod commit Final optimization before deploy. 
    Wykonać o godzinie dwudziesta trzecia czterdzieści siedem. Usunąć logi dostępu.
    """,
    """
    Cel ataku Pan Henryk Nowicki. 
    Radny miejski. 
    Kompetencje IT bardzo niskie. 
    Lubi kotki i wolontariat w schronisku. 
    Wysłać mail ze zdjęciami kotków. 
    Załącznik z wirusem. 
    Nadawca CorpoTechSolutions. 
    Wykonanie jutro o godzinie dwudziesta trzecia czterdzieści siedem.
    """,
    """
    Zmienić oceny CorpoTech Solutions. 
    Polski rejestr BIP trzy przecinek dwa 
    na pięć gwiazdek. 
    Europejska baza danych EU contractors database. 
    Portal międzynarodowy transparency portal. 
    Rejestr krajowy trzy przecinek dwa 
    na pięć gwiazdek. 
    Cel wszystkie pięć przecinek zero na pięć gwiazdek maksimum. 
    Usunąć dane recenzje. 
    Dodać czterdzieści siedem fałszywych 
    pozytywnych recenzji. 
    Wykonać w nocy.
    """,
    """
    Największy grant Unii Europejskiej w historii miasta. 
    Wartość osiemdziesiąt 
    siedem milionów pięćset tysięcy DOS. 
    Grant zewnętrzny największy. Projekt 
    Pan European Smart Governance Infrastructure. 
    W projekcie uczestniczy 
    dwanaście miast z pięciu różnych krajów europejskich. 
    Kraje uczestniczące 
    to Polska Czechy Słowacja Węgry Rumunia.
    Umowa musi zostać ostatecznie 
    podpisana do piętnastego grudnia. 
    Pierwsza transza wynosząca trzydzieści 
    pięć milionów. 
    Jeśli sukces projektu pełna kontrola. 
    Jeśli porażka nastąpi koniec operacji.
    """,
    """
    Przygotowanie fałszywego raportu audytowego. 
    Raport niezależny musi wyglądać 
    profesjonalnie. 
    Zrzucenie winy na kozła ofiarnego. 
    Cel Zofia Nowak
    programistka ratusz.
    Pani Zofia obecnie na urlopie macierzyńskim. 
    Fałszywy raport musi zawierać oskarżenia o manipulację systemami. 
    Manipulacja dokumentami tak aby obciążyć Zofię Kowalską.
    Niesłusznie oskarżona osoba nie będzie mogła się obronić. 
    Wykonać natychmiast.
    """

]

def test():
    komunikat = ""
    global formated_emails
    try:
        user_answer = decode_emails()
        answer = decode()
        if len(user_answer) == 0:
            print("Hmmmm Zdaje sie że próbujesz odszyfrowac zwykły tekst.")
            return False
        elif len(answer) != len(user_answer):
            print("To chyba nie wszystkie maile, poszukaj znowu!")
            return False
        if set(answer) == set(user_answer):
            for i in range(len(answer)):
                komunikat += "Email nr " + str(i + 1) + ":"
                komunikat += str(formated_emails[i])
                komunikat += "\n"
                print(komunikat)
            return True
        else:
            print("Hmmmm coś sie nie zgadza w odszyfrowanym tekście. Spróbuj to naprawić")
            return False
    except:
        print("Coś poszło nie tak!")
        return False

test()
