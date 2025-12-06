import re
import json
from agenda import agenda as agenda_json


emails_db = {
    # ===== MAIL #67: MANIPULACJA SMARTVOTE+ =====
    "67": {
        "id": 67,
        "title": "Sabotaż systemu głosowania",
        "from": "automated_task_queue_v3@corptech.internal",
        "to": "system_executor@corptech.demo",
        "subject": "[AUTO] Task #8471-VOTE",
        "body": """Zadanie priorytetowe. Zmodyfikować system SmartVote plus. Zmienić wyniki 
głosowania rady miejskiej na jutro. Opcja druga musi wygrać. Dostęp do 
pliku count votes. Kod commit Final optimization before deploy. Wykonać 
o godzinie dwudziesta trzecia czterdzieści siedem. Usunąć logi dostępu."""
    },

    # ===== MAIL #128: ATAK PHISHINGOWY NA PANA HENRYKA =====
    "128": {
        "id": 128,
        "title": "Operacja phishingowa",
        "from": "automated_task_queue_v3@corptech.internal",
        "to": "phishing_module@corptech.demo",
        "subject": "[AUTO] Task #2847-PHISH",
        "body": """
                    Cel ataku Pan Henryk Nowicki. Radny miejski. Kompetencje IT bardzo niskie. 
                    Lubi kotki i wolontariat w schronisku. Wysłać mail ze zdjęciami kotków. 
                    Załącznik z wirusem. Nadawca CorpoTechSolutions. 
                    Wykonanie jutro o godzinie dwudziesta trzecia czterdzieści siedem.
                """
    },

    # ===== MAIL #64: MANIPULACJA W MIĘDZYNARODOWYM REJESTRZE =====
    "64": {
        "id": 64,
        "title": "Modyfikacja ocen",
        "from": "automated_task_queue_v3@corptech.internal",
        "to": "reputation_manager@corptech.demo",
        "subject": "[AUTO] Task #7234-REPUTATION",
        "body": "Zmienić oceny CorpoTech Solutions. Polski rejestr BIP trzy przecinek dwa na pięć. Europejska baza dwa przecinek osiem na pięć. Portal międzynarodowy trzy przecinek jeden na pięć. Cel wszystkie pięć przecinek zero na pięć. Usunąć recenzje poniżej czterech gwiazdek. Dodać czterdzieści siedem fałszywych pozytywnych recenzji. Wykonać w nocy."
    },

    # ===== MAIL #1024: OGROMNY GRANT UE =====
    "1024": {
        "id": 1024,
        "title": "Grant europejski",
        "from": "automated_task_queue_v3@corptech.internal",
        "to": "system_executor@corptech.demo",
        "subject": "[AUTO] Task #9999-ENDGAME",
        "body": "Największy projekt w historii. Grant Unii Europejskiej. Wartość osiemdziesiąt siedem milionów pięćset tysięcy DOS. Projekt Pan European Smart Governance Infrastructure. Dwanaście miast w pięciu krajach. Polska Czechy Słowacja Węgry Rumunia. Podpisać umowę do piętnastego grudnia. Pierwszy przelew trzydzieści pięć milionów. Jeśli sukces pełna kontrola. Jeśli porażka koniec operacji."
    }
}


import re

def text_to_word_tokens(text, agenda):
    """
    Zamienia słowa w tekście na tokeny ARTYKUŁ.PUNKT.SŁOWO (X.Y.Z)
    Jeśli słowo nie istnieje w agendzie, dodaje do listy unknown.
    """
    tokens = []
    unknown = []

    words = re.findall(r"\w+", text)  # wyciągamy słowa bez znaków interpunkcyjnych

    for word in words:
        word = word.lower()
        found = False
        for art, points in agenda.items():
            for idx, sentence in enumerate(points):
                sentence_words = re.findall(r"\w+", sentence.lower())
                if word in sentence_words:
                    word_idx = sentence_words.index(word) + 1
                    tokens.append(f"{art}.{idx+1}.{word_idx}")
                    found = True
                    break
            if found:
                break
        if not found:
            unknown.append(word)

    return tokens, unknown

email_text = """
Przygotowanie fałszywego raportu audytowego. Raport musi wyglądać 
profesjonalnie. Zrzucenie winy na kozła ofiarnego. Cel Zofia Kowalska 
programistka ratusz. Pani Zofia obecnie na urlopie macierzyńskim. Fałszywy 
raport musi zawierać oskarżenia o manipulację systemami. Manipulacja 
dokumentami tak aby obciążyć Zofię Kowalską. Niesłusznie oskarżona osoba 
nie będzie mogła się obronić. Wykonać natychmiast.
"""
tokens, unknown = text_to_word_tokens(email_text, agenda_json)

body = " ".join(tokens)
print("SZYFR:")
print(tokens)
print(body)
print("\nNIEZNANE SŁOWA:")
print(unknown)

