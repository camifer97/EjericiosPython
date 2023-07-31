import random

def play():
    user = input("Elige piedra, papel o tijera: ").lower()
    computer = random.choice(["piedra", "papel", "tijera"]).lower()

    if user == computer:
        return "Empate!"
    
    if is_win(user, computer):
        return "Ganaste!"
    
    return "Perdiste!"


def is_win(player, opponent):
    if (player == "tijera" and opponent == "papel") or (player == "papel" and opponent == "piedra") or (player == "piedra" and opponent == "tijera"):
        return True
        

print(play())