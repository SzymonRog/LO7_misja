import re
import json


agenda_json = {
    "1": [
        "Każde zadanie powierzone obywatelowi powinno być wykonane sumiennie i terminowo dla dobra wspólnoty",
        "Działania priorytetowe w administracji publicznej wymagają szczególnej uwagi i zaangażowania wszystkich",
        "Obywatel może podpisać oficjalne dokumenty tylko po ich dokładnym przeczytaniu i zrozumieniu",
        "Każdą umowę zawartą w imieniu miasta musi zatwierdzić odpowiedni organ władzy",
        "Projekty infrastrukturalne realizujemy na rzecz wszystkich mieszkańców bez wyjątku i dyskryminacji",
        "Plany budowy nowych obiektów wymagają konsultacji społecznych i zgody rady miasta",
        "Dbałość o miejski park to obowiązek każdego mieszkańca i instytucji publicznej",
        "Nigdy nie wolno zmanipulować żadnego demokratycznego procesu decyzyjnego w naszym mieście",
        "Każde głosowanie dotyczące spraw publicznych musi być uczciwe i przejrzyste"
    ],
    "2": [
        "Budżetu miejskiego pilnujemy wspólnie jako wspólnego dobra wszystkich mieszkańców",
        "Zabrania się przekierować jakiekolwiek publiczne fundusze na prywatne cele",
        "Wszystkie środki finansowe muszą być wydatkowane zgodnie z planem i przeznaczeniem",
        "Każde konto bankowe miasta wymaga regularnej kontroli i audytu zewnętrznego",
        "Wydatki firmowe z budżetu muszą być szczegółowo udokumentowane i uzasadnione",
        "Każdy termin płatności i rozliczenia projektów musi być przestrzegany bezwzględnie",
        "Odpowiedzialność za realizacji budżetu spoczywa na władzach miasta i urzędnikach",
        "Planowanie jutro rozpoczyna się dziś poprzez staranne przygotowanie i analizę",
        "Prace rano nad budżetem wymagają świeżego umysłu i pełnej koncentracji"
    ],
    "3": [
        "Każdy grant zewnętrzny musi być wykorzystany zgodnie z jego przeznaczeniem",
        "Procedury nie mogą być realizowane automatycznie bez ludzkiego nadzoru i weryfikacji",
        "Dokument zatwierdzony wymaga podpisów wszystkich odpowiedzialnych stron zanim nabierze mocy",
        "Realizacja projektów bez odpowiedniej kontroli może prowadzić do nadużyć i korupcji",
        "Fundusze otrzymane na kwota wynoszącą dwa miliony złotych wymagają szczególnej uwagi",
        "Pomoc finansowa przekazana beneficjentom musi być monitorowana do końca projektu",
        "Każdy projekt może w wyjątkowych sytuacjach pozostać wstrzymany w czasie z uzasadnionych przyczyn",
        "Żaden projekt nie może być niezrealizowany bez zwrotu otrzymanych środków publicznych",
        "Informatyczny system miejski działa dla efektywności i transparentności administracji publicznej"
    ],
    "4": [
        "Wszystko w urzędzie powinno działać poprawnie aby służyć mieszkańcom efektywnie",
        "Regularne skanowanie infrastruktury IT pozwala wykryć zagrożenia zanim wyrządzą szkodę",
        "Audyt systemów zakończone pomyślnie daje pewność że wszystko funkcjonuje bezpiecznie",
        "Jeśli wykryto jakiekolwiek nieprawidłowości należy natychmiast podjąć działania naprawcze",
        "W zeszłym roku wykryliśmy siedemnaście różnych prób włamania do systemów miejskich",
        "Każda z tych luk bezpieczeństwa została natychmiast załatana przez nasz zespół IT",
        "Zagrożenia w systemie miejskim są monitorowane przez całą dobę bez przerwy",
        "Do ochrony wykorzystano najnowocześniejsze czternaście różnych technologii zabezpieczających dostęp",
        "Testy exploitów penetracyjnych przeprowadzamy regularnie dla sprawdzenia odporności naszych systemów"
    ],
    "5": [
        "Specjaliści zidentyfikowano w systemach osiem kategorii potencjalnych zagrożeń cybernetycznych",
        "Monitoring nowych technologii pozwala nam być o krok przed cyberprzestępcami",
        "Lista celów do zabezpieczenia jest regularnie aktualizowana i priorytetyzowana",
        "Każdy obywatel powinien znać podstawy ochrony do przed atakami phishingowymi",
        "Próby ataku na infrastrukturę miejską są dokumentowane i analizowane przez ekspertów",
        "Atak phishingowego typu jest najczęstszą metodą wykorzystywaną przez cyberprzestępców obecnie",
        "Edukacja mieszkańców w zakresie cyberbezpieczeństwa jest naszym priorytetem"
    ],
    "6": [
        "Zespół ekspertów przygotowano specjalny program edukacyjny dotyczący rozpoznawania fake newsów",
        "Każdy fałszywy materiał informacyjny musi być zgłoszony odpowiednim organom nadzorczym",
        "Publikacja raport rocznego o dezinformacji pozwala zrozumieć skalę problemu",
        "Nigdy nie powinno się wyznaczono kozła ofiarnego zamiast szukać prawdziwych sprawców",
        "Taktyka kozła ofiarnego jest stosowana przez nieuczciwych polityków i manipulatorów",
        "Władze miasta uruchomiono specjalną infolinię do zgłaszania podejrzanych treści",
        "Każda kampanię informacyjną musimy prowadzić zgodnie z zasadami etyki i prawdy",
        "Treści dezinformacyjną należy zgłaszać natychmiast aby zapobiec jej rozprzestrzenianiu",
        "W zeszłym miesiącu opublikowano w lokalnej prasie tysiąc artykułów edukacyjnych dla mieszkańców"
    ],
    "7": [
        "Dobre rezultaty osiągamy w ciągu odpowiednio zaplanowanego czasu realizacji projektów",
        "Nawet najbardziej ambitny cel można zrealizować w trzydziestu dni jeśli dobrze zaplanujemy",
        "Każda minut a w administracji publicznej powinna być wykorzystana efektywnie",
        "Każdy cel musi być został jasno określony przed rozpoczęciem jakiegokolwiek działania",
        "Sukces osiągnięty przez zespół to sukces całej społeczności lokalnej",
        "Działać zgodnie z prawem i etyką to fundament naszej pracy",
        "Plany rozwojowe z długoterminowym planem zapewniają stabilność i przewidywalność działań"
    ],
    "8": [
        "Każdy mieszkaniec ma prawo uczestniczyć w życiu publicznym miasta",
        "Konsultacje społeczne są niezbędnym elementem procesu decyzyjnego",
        "Referendum lokalne pozwala mieszkańcom decydować o ważnych sprawach",
        "Budżet obywatelski daje możliwość współdecydowania o wydatkach publicznych"
    ],
    "9": [
        "Ochrona środowiska naturalnego jest priorytetem władz miasta",
        "Zieleń miejska poprawia jakość życia i zdrowie mieszkańców",
        "Segregacja odpadów to obowiązek każdego odpowiedzialnego obywatela",
        "Energia odnawialna jest przyszłością naszego miasta i planety",
        "Wydarzenia ekologiczne odbywaja się w parku"
    ],
    "10": [
        "Dostęp do edukacji jest prawem każdego mieszkańca niezależnie od wieku",
        "Biblioteki miejskie są skarbnicami wiedzy otwartymi dla wszystkich",
        "Instytucje kultury wzbogacają życie społeczne i budują tożsamość lokalną",
        "Wspieramy inicjatywy edukacyjne promujące kreatywność i rozwój osobisty",
    ],
    "11": [
        "Pomoc osobom potrzebującym jest moralnym obowiązkiem społeczności",
        "Wolontariat wzmacnia więzi społeczne i buduje kapitał społeczny",
        "Seniorzy zasługują na szacunek i wsparcie w codziennym życiu",
        "Młodzież to przyszłość miasta więc inwestujemy w ich rozwój"
    ],
    "12": [
        "Wszystkie decyzje władz muszą być jawne i zrozumiałe dla obywateli",
        "Urzędnicy odpowiadają przed mieszkańcami za swoje działania",
        "Korupcja w jakiejkolwiek formie jest niedopuszczalna i karana",
        "Każdy ma prawo do dostępu do informacji publicznej"
    ]
}

emails_db = {
    # ===== MAIL #67: MANIPULACJA SMARTVOTE+ =====
    "67": {
        "id": 67,
        "title": "Sabotaż systemu głosowania",
        "from": "automated_task_queue_v3@corptech.internal",
        "to": "system_executor@corptech.demo",
        "subject": "[AUTO] Task #8471-VOTE",
        "body": "Zadanie priorytetowe. Zmodyfikować system SmartVote plus. Zmienić wyniki głosowania rady miejskiej na jutro. Opcja druga musi wygrać. Dostęp do pliku count votes. Wykonać o dwudziestej trzeciej czterdzieści siedem. Commit message Final optimization before deploy. Usunąć logi dostępu."
    },

    # ===== MAIL #128: ATAK PHISHINGOWY NA PANA HENRYKA =====
    "128": {
        "id": 128,
        "title": "Operacja phishingowa",
        "from": "automated_task_queue_v3@corptech.internal",
        "to": "phishing_module@corptech.demo",
        "subject": "[AUTO] Task #2847-PHISH",
        "body": "Cel ataku Henryk Nowicki. Radny miejski. Lubi kotki i wolontariat w schronisku. Kompetencje IT bardzo niskie. Wysłać mail ze zdjęciami kotków. Załącznik z wirusem. Nadawca CorpoTechSolutions at demosSys dot com. Wykonanie jutro o dwudziestej trzeciej czterdzieści siedem."
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
                sentence_words = re.findall(r"\w+", sentence)
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

email_text = "Cel ataku Henryk Nowicki. Radny miejski. Lubi kotki i wolontariat w schronisku. Kompetencje IT bardzo niskie. Wysłać mail ze zdjęciami kotków. Załącznik z wirusem. Nadawca CorpoTechSolutions at demosSys dot com. Wykonanie jutro o dwudziestej trzeciej czterdzieści siedem."

tokens, unknown = text_to_word_tokens(email_text, agenda_json)

body = " ".join(tokens)
print("SZYFR:")
print(tokens)
print(body)
print("\nNIEZNANE SŁOWA:")
print(unknown)

