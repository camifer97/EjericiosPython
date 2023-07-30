import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback!='correcto':
        if low!=high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Es el numero {guess} demasiado grande, chico, o es el correcto?: ").lower()
        if feedback == "grande":
            high = guess - 1
        else:
            feedback == "pequeño"
            low = guess + 1
    print(f"Felicitaciones! El numero {guess} es el ganador.")

computer_guess(10)