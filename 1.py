import random

user_score = 0
computer_score = 0

while True:
    user = input("Выбери (камень, ножницы, бумага) или 'стоп' для выхода: ").lower()
    if user == 'стоп':
        print("Игра окончена.")
        break
    if user not in ['камень', 'ножницы', 'бумага']:
        print("Неверный ввод. Попробуй снова.")
        continue

    computer = random.choice(["камень", "ножницы", "бумага"])
    print("Ты выбрал:", user)
    print("Компьютер выбрал:", computer)

    if user == computer:
        print("Ничья!")
    elif (user == "камень" and computer == "ножницы") or \
         (user == "ножницы" and computer == "бумага") or \
         (user == "бумага" and computer == "камень"):
        print("Ты победил!")
        user_score += 1
    else:
        print("Ты проиграл!")
        computer_score += 1

    print(f"Счёт: Ты {user_score} - {computer_score} Компьютер\n")
