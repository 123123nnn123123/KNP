import random

user_score = 0
computer_score = 0

while True:
    user = input("Вибери (камінь, ножиці, папір) або 'стоп' для виходу: ").lower()
    if user == 'стоп':
        print("Гру завершено.")
        break
    if user not in ['камінь', 'ножиці', 'папір']:
        print("Невірний ввід. Спробуй ще раз.")
        continue

    computer = random.choice(["камінь", "ножиці", "папір"])
    print("Ти обрав:", user)
    print("Комп'ютер обрав:", computer)

    if user == computer:
        print("Нічия!")
    elif (user == "камінь" and computer == "ножиці") or \
         (user == "ножиці" and computer == "папір") or \
         (user == "папір" and computer == "камінь"):
        print("Ти переміг!")
        user_score += 1
    else:
        print("Ти програв!")
        computer_score += 1

    print(f"Рахунок: Ти {user_score} - {computer_score} Комп'ютер\n")
