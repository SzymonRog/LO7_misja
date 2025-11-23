from user import decode_emails   # po prostu import funkcji
import numpy as np


def test_user_solution():
    print("=== TEST ROZWIĄZANIA ===\n")

    # Lista poprawnych odpowiedzi (zapisz tu swoje!)
    correct_answers = [
        "ZMOWA Z URZEDNIKAMI",
        "TRANSFER 2M DOS DO KONTA OFFSHORE",
        "FALSZYWE FAKTURY - PROJEKT MOST ZACHODNI",
        "ZOFIA KUCHAREK WIE ZA DUZO",
        "SPOTKANIE Z PREMIEREM - LAPOWKA 500K",
    ]

    # Stwórz fake dane wejściowe (lista None o tej samej długości)

    dummy_images = []
    for i in range(0,len(correct_answers)):
        dummy_images.append(np.load(f"data/encrypted_{i}.npy"))

    try:
        user_result = decode_emails(dummy_images)
    except Exception as e:
        print(f"❌ Błąd w decode_emails(): {e}")
        return

    if not isinstance(user_result, list):
        print(f"❌ Funkcja powinna zwrócić listę, a zwróciła: {type(user_result)}")
        return

    if len(user_result) != len(correct_answers):
        print(f"❌ Zwrócono {len(user_result)} wyników, oczekiwano {len(correct_answers)}")
        return

    # Porównanie wyników
    print("WYNIKI:")
    print("=" * 50)

    passed = 0
    for i, (user, correct) in enumerate(zip(user_result, correct_answers)):
        if user == correct:
            print(f"✅ Test {i+1}: OK — {user}")
            passed += 1
        else:
            print(f"❌ Test {i+1}: BŁĄD")
            print(f"   Oczekiwano: {correct}")
            print(f"   Otrzymano : {user}")

    print("=" * 50)
    print(f"Zaliczone: {passed}/{len(correct_answers)}")



if __name__ == "__main__":
    test_user_solution()
