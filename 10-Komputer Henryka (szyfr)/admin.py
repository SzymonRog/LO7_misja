import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os


def text_to_binary(text):
    """Konwertuje tekst na ciąg bitów binarnych"""
    return ''.join(format(ord(char), '08b') for char in text)


def encode_message_lsb(image, message):
    """
    Ukrywa wiadomość w obrazie używając LSB steganografii

    Args:
        image (np.array): Obraz RGB (H, W, 3)
        message (str): Tekst do ukrycia

    Returns:
        np.array: Obraz z ukrytą wiadomością
    """
    encoded_image = image.copy()
    message_with_delimiter = message + "###END###"
    binary_message = text_to_binary(message_with_delimiter)

    max_bytes = image.shape[0] * image.shape[1] * 3
    if len(binary_message) > max_bytes:
        raise ValueError(f"Wiadomość za długa! Max {max_bytes} bitów, próbujesz {len(binary_message)}")

    data_index = 0

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for k in range(3):
                if data_index < len(binary_message):
                    pixel_value = int(encoded_image[i, j, k])
                    pixel_value = (pixel_value & ~1) | int(binary_message[data_index])
                    encoded_image[i, j, k] = pixel_value
                    data_index += 1
                else:
                    return encoded_image

    return encoded_image


def decode_message_lsb(encoded_image):
    """
    Wyciąga ukrytą wiadomość z obrazu

    Args:
        encoded_image (np.array): Obraz z ukrytą wiadomością

    Returns:
        str: Odkodowana wiadomość
    """
    binary_message = ""

    for i in range(encoded_image.shape[0]):
        for j in range(encoded_image.shape[1]):
            for k in range(3):
                pixel_value = int(encoded_image[i, j, k])
                lsb = pixel_value & 1
                binary_message += str(lsb)

    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i + 8]
        if len(byte) == 8:
            char = chr(int(byte, 2))
            message += char

            if message.endswith("###END###"):
                return message[:-9]

    return message


def load_image_from_file(filepath):
    """Wczytuje obraz z pliku"""
    img = Image.open(filepath)
    img = img.convert('RGB')
    return np.array(img)


def generate_encrypted_images(messages, image_dir="images", output_dir="data"):
    """
    Generuje zaszyfrowane obrazy z wiadomościami

    Args:
        messages (list): Lista wiadomości do ukrycia
        image_dir (str): Folder z obrazami źródłowymi
        output_dir (str): Folder do zapisu zaszyfrowanych plików .npy
    """
    os.makedirs(output_dir, exist_ok=True)

    # Pobierz listę obrazów z folderu images
    image_files = sorted([f for f in os.listdir(image_dir) if f.endswith(('.png', '.jpg', '.jpeg'))])

    if len(image_files) < len(messages):
        print(f"⚠️  Tylko {len(image_files)} obrazów, potrzeba {len(messages)}. Używam losowych dla reszty.")

    for i, message in enumerate(messages):
        # Użyj prawdziwego obrazu jeśli jest dostępny, inaczej losowy
        if i < len(image_files):
            img_path = os.path.join(image_dir, image_files[i])
            base_image = load_image_from_file(img_path)
            print(f"📷 {image_files[i]} -> encrypted_{i}.npy")
        else:
            np.random.seed(i + 100)
            base_image = np.random.randint(0, 256, (200, 200, 3), dtype=np.uint8)
            print(f"🎲 Losowy #{i} -> encrypted_{i}.npy")

        # Koduj wiadomość
        encoded = encode_message_lsb(base_image, message)

        # Zapisz jako .npy
        output_path = os.path.join(output_dir, f"encrypted_{i}.npy")
        np.save(output_path, encoded)
        print(f"   Ukryto: '{message[:50]}{'...' if len(message) > 50 else ''}'")
        plt.imsave(f"images/encrypted/encrypted_{i}.png", encoded)

    print(f"\n✅ Wygenerowano {len(messages)} zaszyfrowanych obrazów w '{output_dir}/'")


def read_encrypted_images(data_dir="data"):
    """
    Odczytuje i dekoduje wszystkie zaszyfrowane obrazy

    Args:
        data_dir (str): Folder z zaszyfrowanymi obrazami

    Returns:
        list: Lista odkodowanych wiadomości
    """
    messages = []
    i = 0

    while True:
        filepath = os.path.join(data_dir, f"encrypted_{i}.npy")
        if not os.path.exists(filepath):
            break

        image = np.load(filepath)
        message = decode_message_lsb(image)
        messages.append(message)
        print(f"encrypted_{i}.npy: '{message}'")
        i += 1

    return messages


def verify_single_image(filepath):
    """
    Sprawdza pojedynczy zaszyfrowany obraz

    Args:
        filepath (str): Ścieżka do pliku .npy

    Returns:
        str: Odkodowana wiadomość
    """
    image = np.load(filepath)
    message = decode_message_lsb(image)
    print(f"Odkodowano z '{filepath}':")
    print(f"  '{message}'")
    return message


# =============================================================================
# Przykład użycia
# =============================================================================

if __name__ == "__main__":
    print("=== ADMIN - GENEROWANIE ZADANIA ===\n")

    # Lista wiadomości do ukrycia
    secret_messages = [
        "ZMOWA Z URZEDNIKAMI",
        "TRANSFER 2M DOS DO KONTA OFFSHORE",
        "FALSZYWE FAKTURY - PROJEKT MOST ZACHODNI",
        "ZOFIA KUCHAREK WIE ZA DUZO",
        "SPOTKANIE Z PREMIEREM - LAPOWKA 500K"
    ]

    # Generuj zaszyfrowane obrazy
    generate_encrypted_images(secret_messages)

    print("\n=== WERYFIKACJA ===\n")

    # Odczytaj i sprawdź
    decoded = read_encrypted_images()

    print(f"\n✅ Sprawdzono {len(decoded)} obrazów")