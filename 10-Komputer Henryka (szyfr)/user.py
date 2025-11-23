import numpy as np

def decode_emails(images):
    """
    Dekoduje ukryte wiadomości z obrazów metodą LSB.
    Zwraca listę wiadomości bez znacznika ###END###.
    """
    messages = []

    END_MARK = "###END###"
    END_LEN = len(END_MARK)

    for img in images:
        bits = []

        # Pobieramy wszystkie LSB z obrazu
        h, w, _ = img.shape
        for i in range(h):
            for j in range(w):
                pixel = img[i, j]
                # każdy kanał - R,G,B
                bits.append(pixel[0] & 1)
                bits.append(pixel[1] & 1)
                bits.append(pixel[2] & 1)

        # Konwersja bitów na tekst
        chars = []
        for i in range(0, len(bits), 8):
            byte_bits = bits[i:i+8]
            if len(byte_bits) < 8:
                break
            byte = "".join(str(b) for b in byte_bits)
            char = chr(int(byte, 2))
            chars.append(char)

            # Szybsze sprawdzanie końca
            if len(chars) >= END_LEN and "".join(chars[-END_LEN:]) == END_MARK:
                break

        # Łączenie i usuwanie znacznika
        msg = "".join(chars)
        if msg.endswith(END_MARK):
            msg = msg[:-END_LEN]

        messages.append(msg)

    return messages
