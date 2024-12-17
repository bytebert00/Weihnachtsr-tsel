with open('geschenk.txt', 'r') as file:
    encrypted_message = file.read().strip()

def generate_fibonacci(n):
    """
    Generiere die Fibonacci-Folge bis zur Zahl n.
    """
    sequence = [1,2]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def decrypt_message(encrypted):
    """
    Entschlüsselt eine Nachricht, indem Fibonacci-Zahlen zurück in Buchstaben übersetzt werden.
    """
    alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,-:.<>'
    fibonacci_sequence = generate_fibonacci(len(alphabet))  # Generiere Fibonacci-Zahlen für das Alphabet

    decrypted = []
    for num in encrypted.split():
        # Finde die Position der Fibonacci-Zahl
        # Hole den Buchstaben aus dem Alphabet
	    continue

    return ''.join(decrypted)

# Starte die Entschlüsselung
decrypted_message = decrypt_message(encrypted_message)

# Ausgabe der entschlüsselten Nachricht
print(decrypted_message)
