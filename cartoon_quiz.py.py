import json
from auxiliary_func import random_order

# Парсим json файл
with open('quiz/questions.json', 'r') as json_file:
    try:
        quest = json.load(json_file)
    except Exception as e:
        print(f'Ошибка: {e}')
# Создаем функцию для работы с вопросами
def Quiz(quest: list, first_order: int = 0, last_order: int = 10, count_quest: int = 10):
    score = 0
    # Получаем список с случайным порядком id вопросов
    order_list = random_order(first_order, last_order, count_quest)

    for i in order_list:
        current_quest = quest['questions'][i]
        count_options = len(current_quest['options'])
        correct_answer = current_quest["correct_answer"]
        explanation = current_quest["explanation"]
        possible_answers = ['1', '2', '3', '4']
        print(f'\n{current_quest['question']}\n')

 
        for j in range(count_options):
            print(f"{j+1} - {current_quest["options"][j]}\n")
        
        user_answer = input('Введите номер ответа: ')
        
        while user_answer not in possible_answers:
            print('Введите пожалуйста корректный ответ')
            user_answer = input('Введите номер ответа: ')

        if user_answer == correct_answer:
            score += 1
            print("\nПравильно, молодец!")
        else:
            print(f"\nНеправильный ответ, правильный ответ был под номером - {correct_answer}")
        print(explanation)
        input("\nНажмите enter для следующего вопроса ")

    print(f'\nВаш балл за викторину - {score}/{count_quest}')

Quiz(quest)