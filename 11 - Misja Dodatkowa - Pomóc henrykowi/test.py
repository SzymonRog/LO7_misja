import random
from filter_emails import filter_safe_emails

def calculate_correct_answer(email, safe_domains, suspicious_words, safe_extensions):
    """
    Funkcja referencyjna - poprawne rozwiązanie zadania
    Oblicza które emaile są bezpieczne
    """
    # Warunek 1: Sprawdź domenę nadawcy
    sender = email["sender"]
    domain = sender.split("@")[1] if "@" in sender else ""

    if domain not in safe_domains:
        return False

    links = email["links"]
    all_https = all(link.startswith("https://") for link in links)

    if not all_https:
        return False

    # Warunek 3: Sprawdź podejrzane słowa
    text = (email["subject"] + " " + email["body"]).lower()
    has_suspicious = any(word.lower() in text for word in suspicious_words)

    if has_suspicious:
        return False

    if len(links) > 3:
        return False

    # Warunek 5: Sprawdź załączniki
    attachments = email["attachments"]

    # Jeśli są załączniki, sprawdź każdy z nich
    if attachments:
        safe_attachments = True

        for attachment in attachments:
            # Wyciągnij rozszerzenie (ostatnia część po kropce)
            if "." not in attachment:
                safe_attachments = False  # Plik bez rozszerzenia
                break

            extension = attachment.split(".")[-1].lower()

            if extension not in safe_extensions:
                safe_attachments = False  # Niebezpieczne rozszerzenie
                break

        if not safe_attachments:
            return False

    return True


def generate_random_email(safe_domains, suspicious_words, safe_extensions, should_be_safe):
    """
    Generuje losowy email - bezpieczny lub niebezpieczny

    Args:
        should_be_safe: True = wygeneruj bezpieczny email, False = niebezpieczny
    """

    # Rozszerzone domeny niebezpieczne
    dangerous_domains = [
        "hacker.com", "phishing.net", "fake-bank.com", "scam.org",
        "virus-alert.com", "secure-verification.net", "account-locked.com",
        "prize-winner.org", "urgent-action.com", "confirm-now.net",
        "free-money.biz", "lottery-win.com", "banking-secure.net",
        "paypal-verify.org", "amazon-account.com", "microsoft-alert.net",
        "apple-security.org", "facebook-verify.com", "instagram-check.net",
        "tax-refund.gov.fake", "government-payment.org", "irs-refund.com",
        "crypto-bonus.net", "investment-profit.biz", "easy-cash.org"
    ]

    # Wszystkie domeny
    all_domains = safe_domains + dangerous_domains

    # Znacznie rozszerzone bezpieczne tematy
    safe_subjects = [
        # Zakupy i zamówienia
        "Potwierdzenie zamówienia #{}".format(random.randint(10000, 99999)),
        "Twoje zamówienie zostało wysłane",
        "Faktura za zamówienie",
        "Dziękujemy za zakupy",
        "Status przesyłki",
        "Zamówienie w realizacji",

        # Konta i usługi
        "Twoje konto zostało zaktualizowane",
        "Nowe funkcje w aplikacji",
        "Podsumowanie aktywności",
        "Raport miesięczny",
        "Newsletter - {} {}".format(
            random.choice(["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec",
                           "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"]),
            random.randint(2020, 2025)
        ),

        # Zawodowe
        "Zaproszenie na spotkanie",
        "Harmonogram na przyszły tydzień",
        "Notatki ze spotkania",
        "Projekt - aktualizacja",
        "Raport tygodniowy",
        "Prezentacja do przejrzenia",

        # Społecznościowe
        "Nowe wiadomości",
        "Masz nowe powiadomienia",
        "Komentarz do Twojego posta",
        "Przypomnienie o wydarzeniu",
        "Zaproszenie do grupy",

        # Edukacyjne
        "Nowy kurs dostępny",
        "Certyfikat ukończenia",
        "Materiały do lekcji",
        "Harmonogram zajęć",

        # Finanse (legalne)
        "Wyciąg z konta - {}".format(random.choice(["styczeń", "luty", "marzec"])),
        "Potwierdzenie przelewu",
        "Zestawienie transakcji",

        # Techniczne
        "Aktualizacja systemu zaplanowana",
        "Nowa wersja oprogramowania",
        "Informacje o konserwacji",
        "Ulepszenia bezpieczeństwa",

        # Informacyjne
        "Nasz blog - najnowszy wpis",
        "Porady tygodnia",
        "Przewodnik dla użytkowników",
        "FAQ - najczęściej zadawane pytania"
    ]

    # Znacznie rozszerzone niebezpieczne tematy
    dangerous_subjects = [
        # Pilność i strach
        "PILNE! Zweryfikuj konto NATYCHMIAST",
        "UWAGA! Twoje konto zostanie zablokowane",
        "OSTATNIA SZANSA - działaj teraz",
        "ALERT BEZPIECZEŃSTWA - natychmiastowa akcja wymagana",
        "Wykryto podejrzaną aktywność na koncie",
        "NATYCHMIAST potwierdź swoją tożsamość",
        "Twoje hasło wygasło - zmień je TERAZ",
        "Konto zablokowane - potwierdź dane",
        "Nieautoryzowany dostęp - PILNE",
        "OSTRZEŻENIE: Nietypowa aktywność",

        # Wygrane i nagrody
        "GRATULACJE! Wygrałeś 50,000 PLN",
        "Jesteś zwycięzcą loterii",
        "Odbierz swoją DARMOWĄ nagrodę",
        "Wygrałeś iPhone 15 Pro Max!",
        "1,000,000 PLN czeka na Ciebie",
        "Jesteś szczęśliwym zwycięzcą",
        "NAGRODA: Odbierz teraz",
        "Wygrana w konkursie - kliknij tutaj",
        "Bezpłatny voucher o wartości 5000 PLN",

        # Finanse (nielegalne)
        "Zwrot podatku - kliknij aby odebrać",
        "Darmowe pieniądze czekają",
        "Potwierdź dane karty kredytowej",
        "Zablokowana płatność - potwierdź",
        "Faktura niezapłacona - PILNE",
        "Kara finansowa - zapłać natychmiast",
        "Twoja karta zostanie dezaktywowana",

        # Techniczne oszustwa
        "Twój komputer jest zainfekowany WIRUSEM",
        "Wykryto złośliwe oprogramowanie",
        "SKAN ANTYWIRUSOWY - kliknij teraz",
        "System wymaga natychmiastowej aktualizacji",
        "Licencja wygasła - odnów TERAZ",

        # Społecznościowe oszustwa
        "Ktoś próbował się zalogować na Twoje konto",
        "Nowe zdjęcia z Tobą - zobacz",
        "Oznaczono Cię w kompromitującym materiale",
        "Twój post narusza regulamin",
        "Konto do usunięcia - potwierdź",

        # Zawodowe oszustwa
        "PILNA wiadomość od CEO",
        "Przelew wymagający zatwierdzenia",
        "Zmiana danych do wypłaty",
        "Nowy system płacowy - zaktualizuj dane"
    ]

    # Znacznie rozszerzone bezpieczne treści
    safe_bodies = [
        # Zakupy
        "Dziękujemy za zakupy w naszym sklepie. Twoje zamówienie jest w trakcie realizacji.",
        "Twoja przesyłka została nadana i będzie dostarczona w ciągu 2-3 dni roboczych.",
        "W załączniku znajdziesz fakturę za ostatnie zamówienie.",
        "Sprawdź status swojego zamówienia w panelu klienta.",

        # Usługi
        "Sprawdź nowe funkcje dostępne w najnowszej wersji aplikacji.",
        "Zaktualizowaliśmy naszą politykę prywatności. Przeczytaj zmiany.",
        "W tym miesiącu dodaliśmy wiele ulepszeń do naszego serwisu.",
        "Twoje konto zostało pomyślnie zaktualizowane.",

        # Informacyjne
        "Odkryj nasze najnowsze produkty i promocje.",
        "Przygotowaliśmy dla Ciebie zestawienie najciekawszych artykułów.",
        "Nowy wpis na blogu już dostępny.",
        "Zapraszamy do udziału w naszym webinarze.",

        # Społecznościowe
        "Otrzymałeś nowe wiadomości od swoich znajomych.",
        "Ktoś skomentował Twój post - sprawdź powiadomienia.",
        "Zbliża się wydarzenie, na które się zapisałeś.",
        "Masz nowych obserwujących.",

        # Zawodowe
        "W załączniku znajdziesz materiały na jutrzejsze spotkanie.",
        "Przesyłam notatki z ostatniej konferencji.",
        "Harmonogram projektu został zaktualizowany.",
        "Proszę o przejrzenie dokumentacji przed spotkaniem.",

        # Edukacyjne
        "Nowy kurs jest już dostępny na platformie.",
        "Gratulujemy ukończenia kursu! Certyfikat w załączniku.",
        "Materiały do następnej lekcji są już dostępne.",

        # Techniczne
        "Zaplanowaliśmy konserwację systemu na przyszły weekend.",
        "Dostępna jest nowa aktualizacja oprogramowania.",
        "Wprowadziliśmy ulepszenia bezpieczeństwa.",

        # Finanse
        "Wyciąg z konta za ostatni miesiąc dostępny w bankowości elektronicznej.",
        "Potwierdzenie wykonania przelewu."
    ]

    # Znacznie rozszerzone niebezpieczne treści
    dangerous_bodies = [
        # Pilność
        "Twoje konto zostanie ZABLOKOWANE za 24 godziny. Kliknij tutaj aby potwierdzić dane.",
        "NATYCHMIAST zweryfikuj swoje informacje aby uniknąć blokady konta.",
        "Wykryliśmy podejrzaną aktywność. Musisz PILNIE zmienić hasło.",
        "Ostatnia szansa na potwierdzenie - działaj TERAZ lub stracisz dostęp.",
        "To Twoja OSTATNIA szansa na uratowanie konta.",

        # Wygrane
        "Gratulacje! Wygrałeś główną nagrodę. Kliknij tutaj natychmiast aby odebrać.",
        "Jesteś jednym ze 100 szczęśliwców. DARMOWA nagroda czeka.",
        "Nie przegap tej szansy! Kliknij aby odebrać swoją wygraną.",
        "Twój kupon o wartości 5000 PLN wygasa dzisiaj - użyj go TERAZ.",

        # Zagrożenia
        "Twój komputer jest zainfekowany. Pobierz narzędzie czyszczące NATYCHMIAST.",
        "Wykryto WIRUSA na Twoim urządzeniu. Skanuj teraz.",
        "ALERT: Złośliwe oprogramowanie znalezione. Kliknij aby usunąć.",

        # Finanse
        "Masz niezapłacone faktury. Zapłać NATYCHMIAST aby uniknąć kary.",
        "Twoja karta kredytowa zostanie zablokowana. Potwierdź dane.",
        "Otrzymałeś zwrot podatku 3,500 PLN. Kliknij aby odebrać.",
        "Transakcja wymaga potwierdzenia - wprowadź dane karty.",

        # Socjalne
        "Ktoś próbował zhackować Twoje konto. Zmień hasło NATYCHMIAST.",
        "Twoje konto zostanie usunięte za 48h jeśli nie potwierdzisz tożsamości.",
        "Zobacz kto oglądał Twój profil - kliknij tutaj.",

        # Zawodowe oszustwa
        "Pilny przelew do zatwierdzenia. Prezes czeka na odpowiedź.",
        "Zmiana procedur finansowych - zaktualizuj swoje dane bankowe.",
        "Nowy system płatności wymaga rejestracji - wprowadź dane karty."
    ]

    # Rozszerzone niebezpieczne rozszerzenia
    dangerous_extensions = [
        "exe", "bat", "cmd", "js", "vbs", "scr", "docm", "xlsm",
        "pif", "com", "msi", "jar", "app", "deb", "rpm",
        "ps1", "sh", "py", "rb", "pl", "wsf", "hta",
        "reg", "dll", "sys", "drv", "cpl", "scf", "lnk"
    ]

    if should_be_safe:
        # Generuj BEZPIECZNY email
        domain = random.choice(safe_domains)
        subject = random.choice(safe_subjects)
        body = random.choice(safe_bodies)

        # HTTPS linki (max 3)
        num_links = random.randint(0, 3)
        links = [f"https://{domain}/{random.choice(['page', 'blog', 'shop', 'account', 'help', 'support'])}{i}"
                 for i in range(num_links)]

        # Bezpieczne załączniki (0-3)
        num_attachments = random.randint(0, 3)
        attachments = []
        attachment_names = ["dokument", "faktura", "raport", "prezentacja", "zdjecie",
                            "materialy", "instrukcja", "podsumowanie", "nota", "zestawienie"]
        for i in range(num_attachments):
            ext = random.choice(safe_extensions)
            name = random.choice(attachment_names)
            attachments.append(f"{name}{i}.{ext}")

        return {
            "sender": f"{random.choice(['info', 'kontakt', 'support', 'hello', 'team', 'news'])}@{domain}",
            "subject": subject,
            "body": body,
            "links": links,
            "attachments": attachments
        }

    else:
        # Generuj NIEBEZPIECZNY email - losuj którą zasadę złamać
        violation_type = random.randint(1, 5)

        if violation_type == 1:
            # Zła domena
            domain = random.choice(dangerous_domains)
            subject = random.choice(safe_subjects)
            body = random.choice(safe_bodies)
            links = [f"https://{domain}/{random.choice(['secure', 'verify', 'account', 'login'])}"]
            attachments = []

        elif violation_type == 2:
            # HTTP zamiast HTTPS
            domain = random.choice(safe_domains)
            subject = random.choice(safe_subjects)
            body = random.choice(safe_bodies)
            links = [f"http://{domain}/{random.choice(['page', 'verify', 'confirm'])}"]  # HTTP!
            attachments = []

        elif violation_type == 3:
            # Podejrzane słowa
            domain = random.choice(safe_domains + dangerous_domains[:5])  # Mix domen
            subject = random.choice(dangerous_subjects)
            body = random.choice(dangerous_bodies)
            links = [f"https://{domain}/{random.choice(['urgent', 'prize', 'verify', 'confirm'])}"]
            attachments = []

        elif violation_type == 4:
            # Za dużo linków (>3)
            domain = random.choice(safe_domains)
            subject = random.choice(safe_subjects)
            body = random.choice(safe_bodies)
            num_malicious_links = random.randint(4, 7)
            links = [f"https://{domain}/{random.choice(['page', 'link', 'redirect'])}{i}"
                     for i in range(num_malicious_links)]
            attachments = []

        else:  # violation_type == 5
            # Niebezpieczny załącznik
            domain = random.choice(safe_domains)
            subject = random.choice(safe_subjects)
            body = random.choice(safe_bodies)
            links = [f"https://{domain}/page"]

            # Dodaj niebezpieczny załącznik
            dangerous_ext = random.choice(dangerous_extensions)
            safe_ext = random.choice(safe_extensions)
            malicious_names = ["update", "patch", "install", "setup", "crack", "keygen",
                               "activator", "loader", "tool", "utility"]
            safe_name = random.choice(["dokument", "raport", "faktura"])
            malicious_name = random.choice(malicious_names)

            attachments = [f"{safe_name}.{safe_ext}", f"{malicious_name}.{dangerous_ext}"]

        return {
            "sender": f"{random.choice(['admin', 'support', 'security', 'noreply', 'alert', 'verify'])}@{domain}",
            "subject": subject,
            "body": body,
            "links": links,
            "attachments": attachments
        }


def test():
    """
    Funkcja testująca - losuje JEDEN email i sprawdza poprawność filtracji
    (pętla testowa będzie dodana przez system LNU)
    """
    try:
        # Importuj funkcję użytkownika
        global komunikat
        komunikat = ""

        # Dane testowe
        safe_domains = ["netflix.com", "spotify.com", "amazon.com", "github.com", "google.com"]
        suspicious_words = ["pilne", "natychmiast", "wygrana", "zweryfikuj konto", "gratulacje",
                            "darmowy", "kliknij tutaj", "wygrałeś"]
        safe_extensions = ["pdf", "txt", "jpg", "jpeg", "png", "mp3", "mp4", "zip"]

        # Losuj czy email ma być bezpieczny czy niebezpieczny
        should_be_safe = random.choice([True, False])

        # Wygeneruj losowy email
        random_email = generate_random_email(safe_domains, suspicious_words, safe_extensions, should_be_safe)

        # Lista z jednym emailem do przetestowania
        test_emails = random_email

        # Oblicz poprawną odpowiedź (funkcja referencyjna)
        expected_result = calculate_correct_answer(test_emails, safe_domains, suspicious_words, safe_extensions)

        # Wywołaj funkcję użytkownika
        user_result = filter_safe_emails(test_emails, safe_domains, suspicious_words, safe_extensions)


        if user_result == expected_result:
            if should_be_safe:
                komunikat += "Super! - Ten Email jest bezpieczny"
                komunikat += f"\nEmail: Od {random_email['sender']}\n"
                komunikat += f"Temat: {random_email['subject']}\n"
                komunikat += f"Linki: {random_email['links']}\n"
                komunikat += f"Załączniki: {random_email['attachments']}\n"
            else:
                komunikat += "Brawo! - Włąsnie nas ochroniłeś przed potencjalnym oszustwem"
                komunikat += f"\nEmail: Od {random_email['sender']}\n"
                komunikat += f"Temat: {random_email['subject']}\n"
                komunikat += f"Linki: {random_email['links']}\n"
                komunikat += f"Załączniki: {random_email['attachments']}\n"

            print(komunikat)
            return True

        else:
            komunikat += "Hmmm - Ten email jest źle oznaczony\n"
            komunikat += f"\nEmail: Od {random_email['sender']}\n"
            komunikat += f"Temat: {random_email['subject']}\n"
            komunikat += f"Linki: {random_email['links']}\n"
            komunikat += f"Załączniki: {random_email['attachments']}\n"
            print(komunikat)
            return False
    except:
        print("Coś poszło nie tak")
        return False


test()
