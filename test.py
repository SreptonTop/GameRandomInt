import random

def generate_random():
    lvl = int(input("Какой уровень? 1.Лёгкий 2.Средний 3.Сложный: "))
    if lvl == 1:
        return random.randint(1, 10), 1,10  
    elif lvl == 2:
        return random.randint(1, 50), 1,50
    else:
        return random.randint(1, 150), 1,150

    
def greet_player():
    name = input("Как тебя зовут? ")  
    print("Привет,", name)  
    return name


def play_game(name):
    number_to_guess,num1,num2 = generate_random()  
    attempts = 0
    print(f"Я загадал число от {num1} до {num2}. Попробуй угадать!")
    while attempts < 3:
        try:
            guess = int(input("Твое предположение: "))  
        except ValueError:
            print("Нужно число!")
            continue
        print("Осталось попыток:",3-attempts)
        if guess == number_to_guess:
            print(name,"Поздравляю! Ты угадал!")
            break
        elif guess < number_to_guess:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")
        attempts += 1
    else:
        print(name,f"Ты не угадал. Загаданное число было {number_to_guess}")  

        
def main():
    name = greet_player() 
    play_game(name)

main()