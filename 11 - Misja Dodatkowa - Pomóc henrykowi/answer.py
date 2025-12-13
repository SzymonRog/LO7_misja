def filter_safe_emails(email, safe_domains, suspicious_words, safe_extensions):


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