import numpy as np


# =============================================================================
# SZYFROWANIE - LSB (Least Significant Bit) Steganography
# =============================================================================

def text_to_binary(text):
    """
    Konwertuje tekst na ciąg bitów binarnych

    Args:
        text (str): Tekst do zakodowania

    Returns:
        str: Ciąg bitów (np. '01001000')
    """
    binary = ''.join(format(ord(char), '08b') for char in text)
    return binary


def encode_message_lsb(image, message):
    """
    Ukrywa wiadomość w obrazie używając LSB steganografii

    Args:
        image (np.array): Obraz RGB (H, W, 3) - KOPIA, oryginalny nie zmieniony
        message (str): Tekst do ukrycia

    Returns:
        np.array: Obraz z ukrytą wiadomością
    """
    # Kopiujemy obraz żeby nie modyfikować oryginału
    encoded_image = image.copy()

    # Dodajemy delimiter (znacznik końca wiadomości)
    message_with_delimiter = message + "###END###"

    # Konwertujemy wiadomość na bity
    binary_message = text_to_binary(message_with_delimiter)

    # Sprawdzamy czy obraz jest wystarczająco duży
    max_bytes = image.shape[0] * image.shape[1] * 3  # pixels * channels
    if len(binary_message) > max_bytes:
        raise ValueError(f"Wiadomość za długa! Maksymalnie {max_bytes} bitów, a próbujesz {len(binary_message)}")

    # Indeks w binary_message
    data_index = 0

    # Iterujemy po pikselach obrazu
    for i in range(image.shape[0]):  # wysokość
        for j in range(image.shape[1]):  # szerokość
            for k in range(3):  # kanały RGB
                if data_index < len(binary_message):
                    # Pobierz aktualny piksel
                    pixel_value = int(encoded_image[i, j, k])

                    # Zamień najmniej znaczący bit (LSB)
                    # Usuwamy ostatni bit i wstawiamy bit z wiadomości
                    pixel_value = (pixel_value & ~1) | int(binary_message[data_index])

                    # Zapisujemy zmienioną wartość
                    encoded_image[i, j, k] = pixel_value

                    data_index += 1
                else:
                    # Skończyliśmy kodować
                    return encoded_image

    return encoded_image


# =============================================================================
# DESZYFROWANIE - Wyciąganie wiadomości z LSB
# =============================================================================

def decode_message_lsb(encoded_image):
    """
    Wyciąga ukrytą wiadomość z obrazu

    Args:
        encoded_image (np.array): Obraz z ukrytą wiadomością

    Returns:
        str: Odkodowana wiadomość
    """
    binary_message = ""

    # Wyciągamy wszystkie LSB z obrazu
    for i in range(encoded_image.shape[0]):
        for j in range(encoded_image.shape[1]):
            for k in range(3):
                # Pobierz najmniej znaczący bit
                pixel_value = int(encoded_image[i, j, k])
                lsb = pixel_value & 1  # Operacja AND z 1 daje ostatni bit
                binary_message += str(lsb)

    # Konwertujemy bity na znaki (po 8 bitów = 1 znak)
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i + 8]
        if len(byte) == 8:
            char = chr(int(byte, 2))
            message += char

            # Sprawdzamy czy dotarliśmy do końca (delimiter)
            if message.endswith("###END###"):
                return message[:-9]  # Usuwamy delimiter

    return message


# =============================================================================
# ZAAWANSOWANA WERSJA - LSB w konkretnym kanale
# =============================================================================

def encode_message_lsb_channel(image, message, channel=1):
    """
    Ukrywa wiadomość tylko w jednym kanale (np. zielonym)

    Args:
        image (np.array): Obraz RGB
        message (str): Wiadomość do ukrycia
        channel (int): Kanał (0=R, 1=G, 2=B)

    Returns:
        np.array: Obraz z ukrytą wiadomością
    """
    encoded_image = image.copy()
    message_with_delimiter = message + "###END###"
    binary_message = text_to_binary(message_with_delimiter)

    # Spłaszczamy wybrany kanał do 1D i konwertujemy na int (żeby uniknąć overflow)
    channel_flat = encoded_image[:, :, channel].flatten().astype(int)

    if len(binary_message) > len(channel_flat):
        raise ValueError("Wiadomość za długa dla tego kanału!")

    # Modyfikujemy LSB
    for i in range(len(binary_message)):
        channel_flat[i] = (channel_flat[i] & ~1) | int(binary_message[i])

    # Przywracamy kształt i konwertujemy z powrotem na uint8
    encoded_image[:, :, channel] = channel_flat.reshape(image.shape[0], image.shape[1]).astype(np.uint8)

    return encoded_image


def decode_message_lsb_channel(encoded_image, channel=1):
    """
    Wyciąga wiadomość z konkretnego kanału
    """
    channel_flat = encoded_image[:, :, channel].flatten()

    binary_message = ""
    for pixel_value in channel_flat:
        binary_message += str(int(pixel_value) & 1)

    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i + 8]
        if len(byte) == 8:
            char = chr(int(byte, 2))
            message += char
            if message.endswith("###END###"):
                return message[:-9]

    return message


# =============================================================================
# TESTY I PRZYKŁADY
# =============================================================================

def test_lsb_steganography():
    """
    Testuje LSB steganografię
    """
    print("=== TEST LSB STEGANOGRAFII ===\n")

    # 1. Tworzymy testowy obraz (losowy szum)
    np.random.seed(42)
    original_image = np.random.randint(0, 256, (200, 200, 3), dtype=np.uint8)
    print(f"1. Utworzono obraz: {original_image.shape}")

    # 2. Wiadomość do ukrycia
    secret_message = "ZMOWA Z URZEDNIKAMI - TRANSFER 2M DOS"
    print(f"2. Wiadomość: '{secret_message}'")
    print(f"   Długość: {len(secret_message)} znaków = {len(secret_message) * 8} bitów\n")

    # 3. Kodowanie (ukrywanie)
    encoded_image = encode_message_lsb(original_image, secret_message)
    print(f"3. Wiadomość ukryta w obrazie")

    # 4. Sprawdzamy różnicę
    difference = np.abs(original_image.astype(int) - encoded_image.astype(int))
    print(f"   Maksymalna zmiana piksela: {np.max(difference)}")
    print(f"   Średnia zmiana: {np.mean(difference):.4f}")
    print(f"   Zmienione piksele: {np.sum(difference > 0)} z {original_image.size}\n")

    # 5. Dekodowanie (wyciąganie)
    decoded_message = decode_message_lsb(encoded_image)
    print(f"4. Odkodowana wiadomość: '{decoded_message}'")

    # 6. Weryfikacja
    if decoded_message == secret_message:
        print("   ✅ SUKCES! Wiadomość odkodowana poprawnie!\n")
    else:
        print("   ❌ BŁĄD! Wiadomości się różnią!\n")

    # 7. Test z konkretnym kanałem (zielony)
    print("=== TEST LSB W KANALE ZIELONYM ===\n")

    encoded_green = encode_message_lsb_channel(original_image, secret_message, channel=1)
    decoded_green = decode_message_lsb_channel(encoded_green, channel=1)

    print(f"Wiadomość w kanale zielonym: '{decoded_green}'")
    if decoded_green == secret_message:
        print("✅ SUKCES!\n")

    return original_image, encoded_image, encoded_green


# =============================================================================
# FUNKCJE DO WCZYTYWANIA WŁASNYCH OBRAZÓW (PNG, JPG, itp.)
# =============================================================================

def load_image_from_file(filepath):
    """
    Wczytuje obraz z pliku (PNG, JPG, etc.) używając PIL/Pillow

    Args:
        filepath (str): Ścieżka do pliku obrazu

    Returns:
        np.array: Obraz jako tablica NumPy (H, W, 3)
    """
    try:
        from PIL import Image
    except ImportError:
        print("❌ Musisz zainstalować Pillow: pip install Pillow")
        return None

    # Wczytaj obraz
    img = Image.open(filepath)

    # Konwertuj do RGB (na wypadek gdyby był RGBA lub inny format)
    img = img.convert('RGB')

    # Konwertuj do NumPy array
    img_array = np.array(img)

    print(f"✅ Wczytano obraz: {filepath}")
    print(f"   Rozmiar: {img_array.shape}")

    return img_array


def save_image_to_file(image_array, filepath):
    """
    Zapisuje obraz do pliku (PNG zalecane - bez kompresji)

    Args:
        image_array (np.array): Obraz jako tablica NumPy
        filepath (str): Ścieżka zapisu
    """
    try:
        from PIL import Image
    except ImportError:
        print("❌ Musisz zainstalować Pillow: pip install Pillow")
        return

    # Konwertuj NumPy array na obraz PIL
    img = Image.fromarray(image_array.astype(np.uint8))

    # Zapisz (PNG zachowuje dokładne wartości pikseli!)
    img.save(filepath)

    print(f"✅ Zapisano obraz: {filepath}")


def encode_message_in_image_file(input_image_path, message, output_image_path):
    """
    KOMPLETNY WORKFLOW: Wczytaj obraz → Ukryj wiadomość → Zapisz

    Args:
        input_image_path (str): Ścieżka do obrazu wejściowego
        message (str): Wiadomość do ukrycia
        output_image_path (str): Ścieżka do zapisu (MUSI być .png!)
    """
    print(f"\n=== UKRYWANIE WIADOMOŚCI W PLIKU ===\n")

    # 1. Wczytaj obraz
    image = load_image_from_file(input_image_path)
    if image is None:
        return

    # 2. Ukryj wiadomość
    print(f"\nUkrywanie: '{message}'")
    encoded_image = encode_message_lsb(image, message)

    # 3. Zapisz
    if not output_image_path.endswith('.png'):
        print("⚠️  UWAGA: Zalecam .png (bez kompresji). JPG może zniszczyć ukrytą wiadomość!")

    save_image_to_file(encoded_image, output_image_path)

    print(f"\n✅ Gotowe! Wiadomość ukryta w: {output_image_path}")


def decode_message_from_image_file(image_path):
    """
    KOMPLETNY WORKFLOW: Wczytaj obraz → Odkoduj wiadomość

    Args:
        image_path (str): Ścieżka do obrazu z ukrytą wiadomością

    Returns:
        str: Odkodowana wiadomość
    """
    print(f"\n=== ODKODOWYWANIE WIADOMOŚCI Z PLIKU ===\n")

    # 1. Wczytaj obraz
    image = load_image_from_file(image_path)
    if image is None:
        return None

    # 2. Odkoduj wiadomość
    print("\nOdkodowywanie...")
    message = decode_message_lsb(image)

    print(f"✅ Odkodowano: '{message}'")

    return message


def save_encoded_images(messages, output_prefix="encrypted"):
    """
    Tworzy i zapisuje zaszyfrowane obrazy z wieloma wiadomościami

    Args:
        messages (list): Lista wiadomości do ukrycia
        output_prefix (str): Prefix dla plików wyjściowych
    """
    print(f"\n=== GENEROWANIE {len(messages)} ZASZYFROWANYCH OBRAZÓW ===\n")

    for i, message in enumerate(messages):
        # Losowy obraz (w rzeczywistości byłyby to prawdziwe obrazy)
        np.random.seed(i + 100)
        base_image = np.random.randint(0, 256, (200, 200, 3), dtype=np.uint8)

        # Kodujemy wiadomość
        encoded = encode_message_lsb(base_image, message)

        # Zapisujemy
        filename = f"{output_prefix}_{i}.npy"
        np.save(filename, encoded)
        print(f"✅ Zapisano: {filename} - '{message[:30]}...'")

    print(f"\nWszystkie obrazy zapisane!\n")


def load_and_decode_images(file_prefix="encrypted", count=3):
    """
    Wczytuje i dekoduje zapisane obrazy

    Args:
        file_prefix (str): Prefix plików
        count (int): Liczba plików do wczytania

    Returns:
        list: Lista odkodowanych wiadomości
    """
    print(f"\n=== WCZYTYWANIE I DEKODOWANIE {count} OBRAZÓW ===\n")

    decoded_messages = []

    for i in range(count):
        filename = f"{file_prefix}_{i}.npy"

        try:
            # Wczytaj obraz
            encoded_image = np.load(filename)

            # Dekoduj wiadomość
            message = decode_message_lsb(encoded_image)
            decoded_messages.append(message)

            print(f"✅ {filename}: '{message}'")
        except FileNotFoundError:
            print(f"❌ Nie znaleziono: {filename}")

    return decoded_messages


# =============================================================================
# URUCHOMIENIE TESTÓW
# =============================================================================

if __name__ == "__main__":
    # Test podstawowy
    test_lsb_steganography()

    # =========================================================================
    # PRZYKŁAD 1: Używanie własnych plików obrazów (PNG, JPG, etc.)
    # =========================================================================

    print("\n" + "=" * 60)
    print("PRZYKŁAD: UKRYWANIE WIADOMOŚCI WE WŁASNYM OBRAZIE")
    print("=" * 60)

    # Instrukcja dla użytkownika
    print("""
    Aby użyć własnego obrazu:

    1. Umieść obraz w tym samym folderze (np. 'kotek.png')
    2. Odkomentuj poniższy kod
    3. Uruchom ponownie

    WAŻNE: 
    - Używaj PNG (nie JPG!) dla wyjścia - JPG kompresuje i niszczy dane
    - Im większy obraz, tym dłuższe wiadomości możesz ukryć
    - Zmiany są CAŁKOWICIE niewidoczne dla oka
    """)

    encode_message_in_image_file(
        input_image_path="images/sneaky_golem.jpg",           # Twój obraz wejściowy
        message="TAJNE DANE Z CORPTECH",        # Wiadomość do ukrycia
        output_image_path="kotek_sekret.png"    # Obraz z ukrytą wiadomością
    )

    decode_message_from_image_file("kotek_sekret.png")

    # =========================================================================
    # PRZYKŁAD 2: Wielokrotne wiadomości (jak w zadaniu)
    # =========================================================================

    print("\n" + "=" * 60)
    print("GENEROWANIE ZADANIA - 5 ZASZYFROWANYCH OBRAZÓW")
    print("=" * 60 + "\n")

    # Przykład z wieloma wiadomościami (jak w zadaniu)
    secret_messages = [
        "ZMOWA Z URZEDNIKAMI",
        "TRANSFER 2M DOS DO KONTA OFFSHORE",
        "FALSZYWE FAKTURY - PROJEKT MOST ZACHODNI",
        "ZOFIA KUCHAREK WIE ZA DUZO",
        "SPOTKANIE Z PREMIEREM - LAPOWKA 500K"
    ]

    # Generuj i zapisz
    save_encoded_images(secret_messages)

    # Wczytaj i odkoduj
    decoded = load_and_decode_images(count=len(secret_messages))

    print("\n=== PODSUMOWANIE ===")
    print(f"Zakodowano: {len(secret_messages)} wiadomości")
    print(f"Odkodowano: {len(decoded)} wiadomości")
    print(f"Poprawność: {sum([a == b for a, b in zip(secret_messages, decoded)])}/{len(secret_messages)}")

    # =========================================================================
    # PRZYKŁAD 3: Batch processing - wiele własnych obrazów
    # =========================================================================

    print("\n" + "=" * 60)
    print("PRZYKŁAD: BATCH PROCESSING")
    print("=" * 60)
    print("""
    Możesz ukryć różne wiadomości w wielu obrazach:

    # Lista obrazów i wiadomości
    files = [
        ("zdjecie1.png", "WIADOMOSC 1"),
        ("zdjecie2.png", "WIADOMOSC 2"),
        ("zdjecie3.png", "WIADOMOSC 3"),
    ]

    # Ukryj wszystkie
    for input_file, message in files:
        output_file = "sekret_" + input_file
        encode_message_in_image_file(input_file, message, output_file)
    """)